"""从 OpenArknightsFBS 的 .fbs 生成 pydantic 模型。

    uv run python scripts/gen_gamedata_models.py character_table skill_table
    uv run python scripts/gen_gamedata_models.py --all

读取 thirdparty/OpenArknightsFBS/FBS/<table>.fbs,写出 ptilopsis/gamedata/<table>.py;
``--all`` 重新生成 :data:`TABLES` 里列出的全部表。少数 FBS 文件名不适合做模块名
(``prts___levels``),按 :data:`MODULE_NAMES` 改名。
FBS 是从客户端类型自动生成的,已经吸收了 ``[JsonProperty]`` 改名,是比 dump.cs
更合适的结构来源;dump.cs 只在需要看逻辑(候选选择、隐藏规则)时用。

映射规则:

- ``table clz_Torappu_X``  → ``class X(GameDataModel)``,字段名转 snake_case,
  与 camelCase 无法互转的(``def``、``Key`` 等)显式给 alias。
- string / table / vector 字段 → ``T | None = None``;int/float/bool 按 FBS 默认值。
- ``[dict__K__V]`` → ``dict[K, V]``;``[list_T]`` → ``list[list[T]]``;
  ``kvp__K__V``(JSON 里是 ``[{"Key": .., "Value": ..}]``)→ ``class KvpKV`` 带
  ``key`` / ``value`` 两个字段;``enum__X`` 字段 → ``str``,同时生成
  ``class X(IntEnum)`` 供比较顺序。
- 字段名与关键字或类型注解里会用到的名字(``dict`` / ``list`` 等)撞车时加
  下划线后缀并给 alias。
- ``root_type clz_Torappu_SimpleKVTable_clz_Torappu_X`` 的表在 JSON 里被拆成
  ``{id: X}``,生成 ``<Table> = TypeAdapter(dict[str, X])``。

写出的文件最后统一过一遍 ``ruff format``,长字段不会超出行宽触发 E501。
"""

from __future__ import annotations

import keyword
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from pydantic.alias_generators import to_camel, to_snake

ROOT = Path(__file__).resolve().parent.parent
FBS_DIR = ROOT / "thirdparty" / "OpenArknightsFBS" / "FBS"
OUT_DIR = ROOT / "ptilopsis" / "gamedata"

SCALARS = {
    "string": ("str", None),
    "bool": ("bool", "False"),
    "int": ("int", "0"),
    "uint": ("int", "0"),
    "long": ("int", "0"),
    "ulong": ("int", "0"),
    "short": ("int", "0"),
    "ushort": ("int", "0"),
    "byte": ("int", "0"),
    "ubyte": ("int", "0"),
    "float": ("float", "0.0"),
    "double": ("float", "0.0"),
}

# 泛型实例化出来的名字太长,手工给个可读的
NAME_OVERRIDES = {
    "clz_Torappu_KeyFrames_2_KeyFrame_Torappu_AttributesData_Torappu_AttributesData_": "AttributesKeyFrame",  # noqa: E501
    "clz_Torappu_KeyFrames_2_KeyFrame_Torappu_AttributesDeltaData_Torappu_AttributesData_": "AttributesDeltaKeyFrame",  # noqa: E501
    # Undefinable<T>:去掉下划线后 String_ 与 String___(string[])会撞名
    "clz_Torappu_Undefinable_1_System_Boolean_": "UndefinableBool",
    "clz_Torappu_Undefinable_1_System_Int32_": "UndefinableInt",
    "clz_Torappu_Undefinable_1_System_Single_": "UndefinableFloat",
    "clz_Torappu_Undefinable_1_System_String_": "UndefinableStr",
    "clz_Torappu_Undefinable_1_System_String___": "UndefinableStrList",
    "clz_Torappu_Undefinable_1_Torappu_EnemyLevelType_": "UndefinableEnemyLevelType",
    "clz_Torappu_Undefinable_1_Torappu_MotionMode_": "UndefinableMotionMode",
    "clz_Torappu_Undefinable_1_Torappu_SourceApplyWay_": "UndefinableSourceApplyWay",
}

SIMPLE_KV_PREFIX = "clz_Torappu_SimpleKVTable_"

# FBS 文件名 → 生成的模块名(缺省同名)
MODULE_NAMES = {
    "prts___levels": "level_data",
}

# FBS 文件名 → 数据在 gamedata 里的文件(缺省 <表名>.json),只用于模块文档
JSON_NAMES = {
    "prts___levels": "levels/<levelId>.json",
}

# 项目用到的全部表,``--all`` 时重新生成
TABLES = [
    "activity_table",
    "battle_equip_table",
    "building_data",
    "campaign_table",
    "char_patch_table",
    "character_table",
    "charword_table",
    "crisis_v2_table",
    "enemy_database",
    "enemy_handbook_table",
    "gamedata_const",
    "handbook_info_table",
    "handbook_team_table",
    "item_table",
    "medal_table",
    "mission_table",
    "prts___levels",
    "roguelike_topic_table",
    "sandbox_perm_table",
    "shop_client_table",
    "skill_table",
    "skin_table",
    "stage_table",
    "story_review_meta_table",
    "story_review_table",
    "uniequip_table",
    "zone_table",
]

# 类体里同名字段会遮住这些名字,导致后面的注解(``dict[str, X]``)求值失败
RESERVED_FIELD_NAMES = frozenset(
    {"dict", "list", "str", "int", "float", "bool", "Any", "Field", "TypeAdapter"}
)


@dataclass
class Field_:  # noqa: N801
    name: str
    fbs_type: str


@dataclass
class Table:
    name: str
    fields: list[Field_] = field(default_factory=list)


@dataclass
class Enum_:  # noqa: N801
    name: str
    base: str
    members: list[tuple[str, int]] = field(default_factory=list)


@dataclass
class Schema:
    tables: dict[str, Table] = field(default_factory=dict)
    enums: dict[str, Enum_] = field(default_factory=dict)
    root: str | None = None


_DECL = re.compile(
    r"(?P<kind>table|enum)\s+(?P<name>\w+)\s*(?::\s*(?P<base>\w+))?\s*\{(?P<body>.*?)\}",
    re.S,
)
_FIELD = re.compile(r"(?P<name>\w+)\s*:\s*(?P<type>[\w\[\]]+)\s*(?:\([^)]*\))?\s*;")
_MEMBER = re.compile(r"(?P<name>\w+)\s*=\s*(?P<value>-?\d+)")
_ROOT = re.compile(r"root_type\s+(?P<name>\w+)\s*;")


def parse(text: str) -> Schema:
    text = re.sub(r"//[^\n]*", "", text)
    schema = Schema()
    for match in _DECL.finditer(text):
        name, body = match["name"], match["body"]
        if match["kind"] == "enum":
            if name in schema.enums:
                continue
            enum = Enum_(name=name, base=match["base"] or "int")
            for member in _MEMBER.finditer(body):
                enum.members.append((member["name"], int(member["value"])))
            schema.enums[name] = enum
        else:
            if name in schema.tables:
                continue
            table = Table(name=name)
            for fld in _FIELD.finditer(body):
                table.fields.append(Field_(fld["name"], fld["type"]))
            schema.tables[name] = table
    if root := _ROOT.search(text):
        schema.root = root["name"]
    return schema


def camel_class_name(fbs_name: str) -> str:
    if fbs_name in NAME_OVERRIDES:
        return NAME_OVERRIDES[fbs_name]
    name = fbs_name
    for prefix in ("clz_", "enum__"):
        name = name.removeprefix(prefix)
    name = name.replace("Torappu_", "")
    parts = [part for part in name.split("_") if part and part != "clz"]
    return "".join(part[0].upper() + part[1:] for part in parts)


class Generator:
    def __init__(
        self,
        schema: Schema,
        module_name: str,
        fbs_name: str | None = None,
        json_name: str | None = None,
    ) -> None:
        self.schema = schema
        self.module_name = module_name
        self.fbs_name = fbs_name or module_name
        self.json_name = json_name or f"{module_name}.json"
        # dict__ / list_ 这些容器表不生成类,只当类型构造器用
        self.generated: list[str] = []

    # ---- 类型映射 -------------------------------------------------------

    def is_container_table(self, name: str) -> bool:
        # SimpleKVTable 是 FlatBuffers 根表的包装,JSON 里不存在;
        # kvp__ 在 JSON 里保留成 {"Key", "Value"} 对象,照常生成类
        return name.startswith(("dict__", "list_", SIMPLE_KV_PREFIX))

    def python_type(self, fbs_type: str) -> tuple[str, str | None]:
        """返回 (类型表达式, 默认值表达式);默认值 None 表示可空。"""

        if fbs_type.startswith("[") and fbs_type.endswith("]"):
            inner = fbs_type[1:-1]
            if inner.startswith("dict__"):
                return self.dict_type(inner), None
            if inner.startswith("list_"):
                table = self.schema.tables.get(inner)
                if table and len(table.fields) == 1:
                    element, _ = self.python_type(table.fields[0].fbs_type)
                    return f"list[{element}]", None
                return "list[Any]", None
            element, _ = self.python_type(inner)
            return f"list[{element}]", None
        if fbs_type in SCALARS:
            return SCALARS[fbs_type]
        if fbs_type in self.schema.enums:
            enum = self.schema.enums[fbs_type]
            zero = next((name for name, value in enum.members if value == 0), None)
            return "str", f'"{zero}"' if zero is not None else '""'
        if fbs_type.startswith("hg__internal__"):
            return "Any", None
        if fbs_type in self.schema.tables:
            return camel_class_name(fbs_type), None
        raise ValueError(f"unknown type {fbs_type!r}")

    def dict_type(self, table_name: str) -> str:
        table = self.schema.tables[table_name]
        key_type, value_type = "str", "Any"
        for fld in table.fields:
            if fld.name.lower() == "key":
                key_type = (
                    "int"
                    if fld.fbs_type in SCALARS and SCALARS[fld.fbs_type][0] == "int"
                    else "str"
                )
            elif fld.name.lower() == "value":
                value_type, _ = self.python_type(fld.fbs_type)
        return f"dict[{key_type}, {value_type}]"

    # ---- 输出 -----------------------------------------------------------

    def field_line(self, fld: Field_) -> str:
        py_type, default = self.python_type(fld.fbs_type)
        snake = to_snake(fld.name)
        alias: str | None = None
        if keyword.iskeyword(snake) or snake in RESERVED_FIELD_NAMES:
            snake += "_"
            alias = fld.name
        elif to_camel(snake) != fld.name:
            alias = fld.name
        if default is None:
            py_type = f"{py_type} | None"
            default = "None"
        if alias is not None:
            # default= 写成关键字,pyright 的 dataclass_transform 才认得出它有默认值
            return f'    {snake}: {py_type} = Field(default={default}, alias="{alias}")'
        return f"    {snake}: {py_type} = {default}"

    def enum_block(self, enum: Enum_) -> str:
        lines = [
            f"class {camel_class_name(enum.name)}(IntEnum):",
            f'    """{enum.name}"""',
            "",
        ]
        for name, value in enum.members:
            member = f"{name}_" if keyword.iskeyword(name) else name
            lines.append(f"    {member} = {value}")
        if not enum.members:
            lines.append("    pass")
        return "\n".join(lines)

    def table_block(self, table: Table) -> str:
        class_name = camel_class_name(table.name)
        self.generated.append(class_name)
        lines = [f"class {class_name}(GameDataModel):", f'    """{table.name}"""', ""]
        for fld in table.fields:
            lines.append(self.field_line(fld))
        if not table.fields:
            lines.append("    pass")
        return "\n".join(lines)

    def root_block(self) -> str | None:
        root = self.schema.root
        if root is None:
            return None
        alias = camel_class_name(self.module_name)
        table = self.schema.tables[root]
        if root.startswith(SIMPLE_KV_PREFIX) and len(table.fields) == 1:
            value_type, _ = self.python_type(table.fields[0].fbs_type)
            return (
                f"# root_type {root}\n"
                f"# JSON 里去掉了外层的 {table.fields[0].name},直接是 {{id: ...}}\n"
                f"{alias} = TypeAdapter({value_type})"
            )
        root_class = camel_class_name(root)
        if alias != root_class:
            return f"# root_type {root}\n{alias} = {root_class}"
        return f"# root_type {root}"

    def render(self) -> str:
        seen: dict[str, str] = {}
        for name in self.schema.tables:
            if self.is_container_table(name):
                continue
            class_name = camel_class_name(name)
            if class_name in seen:
                raise ValueError(
                    f"{name} and {seen[class_name]} both map to class {class_name}; "
                    "add a NAME_OVERRIDES entry"
                )
            seen[class_name] = name

        blocks: list[str] = []
        for enum in self.schema.enums.values():
            blocks.append(self.enum_block(enum))
        for table in self.schema.tables.values():
            if self.is_container_table(table.name):
                continue
            blocks.append(self.table_block(table))
        if root := self.root_block():
            blocks.append(root)
        body = "\n\n\n".join(blocks)
        rebuild = "\n".join(f"{name}.model_rebuild()" for name in self.generated)

        stdlib: list[str] = []
        if self.schema.enums:
            stdlib.append("from enum import IntEnum")
        if re.search(r"\bAny\b", body):
            stdlib.append("from typing import Any")
        pydantic_names = [
            name for name in ("Field", "TypeAdapter") if f"{name}(" in body
        ]
        third_party = (
            [f"from pydantic import {', '.join(pydantic_names)}"]
            if pydantic_names
            else []
        )
        groups = [
            ["from __future__ import annotations"],
            stdlib,
            third_party,
            ["from ptilopsis.gamedata._base import GameDataModel"],
        ]
        imports = "\n\n".join("\n".join(group) for group in groups if group)
        header = (
            f'"""{self.json_name} 的数据模型。\n\n'
            f"由 scripts/gen_gamedata_models.py 从 FBS/{self.fbs_name}.fbs 生成,"
            "请勿手改;\n字段语义见 dump.cs 里的同名类。\n"
            '"""\n\n'
        )
        return header + imports + "\n\n\n" + body + "\n\n\n" + rebuild + "\n"


def generate(table_name: str) -> Path:
    schema = parse((FBS_DIR / f"{table_name}.fbs").read_text(encoding="utf-8"))
    module_name = MODULE_NAMES.get(table_name, table_name)
    code = Generator(
        schema, module_name, fbs_name=table_name, json_name=JSON_NAMES.get(table_name)
    ).render()
    out = OUT_DIR / f"{module_name}.py"
    out.write_text(code, encoding="utf-8")
    return out


def format_files(paths: list[Path]) -> None:
    """按仓库的 ruff 配置格式化生成的文件(ruff 在 dev 依赖里)。"""
    subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--quiet", *map(str, paths)],
        cwd=ROOT,
        check=True,
    )


def main(argv: list[str]) -> None:
    if not argv:
        sys.exit(__doc__)
    if argv == ["--all"]:
        argv = TABLES
    written = [generate(table_name) for table_name in argv]
    format_files(written)
    for path in written:
        sys.stdout.write(f"{path}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
