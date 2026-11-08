import importlib.util
import json
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "sync_ellipsis.py"
spec = importlib.util.spec_from_file_location("sync_ellipsis", SCRIPT)
assert spec is not None and spec.loader is not None
se = importlib.util.module_from_spec(spec)
# dataclass 装饰器要通过 sys.modules 找回模块命名空间
sys.modules[spec.name] = se
spec.loader.exec_module(se)


def book(*pairs: tuple[str, str]):
    return se.Rulebook(
        rule
        for index, (old, new) in enumerate(pairs)
        for rule in se.rules_for("t", index, old, new)
    )


def apply(page: str, *pairs: tuple[str, str]) -> str:
    return book(*pairs).apply(page)[0]


def test_changed_texts_pairs_by_text_not_path():
    old = {"a": ["其一......其二", "原样......保留"], "b": "打倒你......！"}
    # 列表顺序变了;“打倒你！”新旧版本都有,不能当成替换结果
    new = {"a": ["原样......保留", "其一……其二"], "b": "打倒你……！", "c": "打倒你！"}
    old["c"] = "打倒你！"
    assert sorted(se.changed_texts(old, new)) == [
        ("其一......其二", "其一……其二"),
        ("打倒你......！", "打倒你……！"),
    ]


def test_changed_texts_falls_back_to_similarity():
    # 同一条文本还删了个逗号
    old = ["然而，我越读正文内容，越觉得不可思议。等等，这是一本......！"]
    new = ["然而我越读正文内容，越觉得不可思议。等等，这是一本……！"]
    assert se.changed_texts(old, new) == [(old[0], new[0])]


def test_archive_lines_with_only_dots():
    # 整行只有点串;游戏顺带删了行尾空格,页面上的空格保留
    old = "......\n已在20593个搜索结果中，为您选择了答案。 \n干员白面鸮\n...... "
    new = "……\n已在20593个搜索结果中，为您选择了答案。\n干员白面鸮\n……"
    page = (
        "|档案3文本=......\n已在20593个搜索结果中，为您选择了答案。 \n"
        "干员白面鸮\n...... \n|档案4=临床诊断分析"
    )
    assert apply(page, (old, new)) == (
        "|档案3文本=……\n已在20593个搜索结果中，为您选择了答案。 \n"
        "干员白面鸮\n…… \n|档案4=临床诊断分析"
    )


def test_newlines_rendered_as_br():
    old = "可露希尔的人工智能小车好棒啊。\n......\n但可露希尔自己也说过"
    new = "可露希尔的人工智能小车好棒啊。\n……\n但可露希尔自己也说过"
    page = "|基础信息=可露希尔的人工智能小车好棒啊。<br>......<br>但可露希尔自己也说过"
    assert apply(page, (old, new)) == (
        "|基础信息=可露希尔的人工智能小车好棒啊。<br>……<br>但可露希尔自己也说过"
    )


def test_json_escaped_text():
    # 换行是 \\n,英文引号是 \\"
    old = '他说"那座圣堂......"\n“那我们就该想点办法破坏它们，对吧？”'
    new = '他说"那座圣堂……"\n“那我们就该想点办法破坏它们，对吧？”'
    page = json.dumps({"desc": old}, ensure_ascii=False)
    assert json.loads(apply(page, (old, new)))["desc"] == new


def test_consecutive_runs_apply_in_order():
    old, new = "啊......嗯......好吧", "啊……嗯……好吧"
    assert apply(f"|台词={old}\n", (old, new)) == f"|台词={new}\n"


def test_short_text_needs_field_boundaries():
    old, new = "“代价......”", "“代价……”"
    page = "|干员简介补充=“代价......”\n"
    assert apply(page, (old, new)) == "|干员简介补充=“代价……”\n"
    # 同样的字出现在别的句子中间时不动
    page = "他说：“代价......”然后走了"
    assert apply(page, (old, new)) == page


def test_one_sided_context_when_other_side_edited():
    old = "们是如何得到这些叙拉古各城邦内部都极少知晓的内幕的......\n下一段"
    new = "们是如何得到这些叙拉古各城邦内部都极少知晓的内幕的……\n下一段"
    page = "内部都极少知晓的内幕的......{{修正|必须|原文=必需}}\n下一段"
    assert apply(page, (old, new)) == (
        "内部都极少知晓的内幕的……{{修正|必须|原文=必需}}\n下一段"
    )


def test_unrelated_and_longer_dot_runs_untouched():
    old, new = "我终于......找到你了。", "我终于……找到你了。"
    page = "我终于.........找到你了。\n别的文本......还是旧的"
    assert apply(page, (old, new)) == page
