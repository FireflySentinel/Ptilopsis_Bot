import re
from collections.abc import Iterable
from typing import Annotated, Any

from ptilopsis.gamedata.battle_equip_table import BattleEquipPack
from ptilopsis.gamedata.building_data import BuildingData
from ptilopsis.gamedata.character_table import (
    AttributesData,
    AttributesDeltaData,
    CharacterData,
    CharacterDataPhaseData,
    ItemBundle,
)
from ptilopsis.gamedata.character_util import (
    MAX_POTENTIAL_RANK,
    phase_index,
    rarity_stars,
    trait_description,
    visible_talent_candidates,
)
from ptilopsis.gamedata.charword_table import CharWordTable
from ptilopsis.gamedata.gamedata_const import GameDataConsts
from ptilopsis.gamedata.handbook_info_table import (
    HandbookInfoTable,
    HandBookStoryViewData,
)
from ptilopsis.gamedata.handbook_team_table import HandbookTeamData
from ptilopsis.gamedata.item_table import InventoryData
from ptilopsis.gamedata.medal_table import MedalData
from ptilopsis.gamedata.skill_table import SkillDataBundle
from ptilopsis.gamedata.skin_table import CharSkinDataDisplaySkin, SkinTable
from ptilopsis.gamedata.uniequip_table import UniEquipTable
from ptilopsis.jobs import params
from ptilopsis.log import logger
from ptilopsis.utils import richtext
from ptilopsis.utils.blackboard import blackboard_values, format_paramed_text
from ptilopsis.utils.job import job
from ptilopsis.utils.wiki import Wiki
from ptilopsis.wikitext import WikiTemplate, inline_template

TeamTable = dict[str, HandbookTeamData]
IdTable = dict[str, dict[str, Any]]
"""wiki 上的干员序号表 ``{干员名: {id, approach, date}}``,见 ``params.CharIdTable``。"""


def phase_attributes(phase: CharacterDataPhaseData) -> list[AttributesData]:
    """一个精英阶段的属性关键帧,按等级顺序;首项是 1 级,末项是满级。"""

    frames = [frame.data for frame in (phase.attributes_key_frames or []) if frame.data]
    if not frames:
        raise ValueError(f"phase {phase.character_prefab_key!r} has no key frames")
    return frames


def favor_attributes(char: CharacterData) -> AttributesDeltaData:
    """满信赖时的加成(信赖关键帧末项)。"""

    frames = [frame.data for frame in (char.favor_key_frames or []) if frame.data]
    return frames[-1] if frames else AttributesDeltaData()


def compile_text(rts: richtext.RichText, text: str | None) -> str:
    return rts.compile(text).replace("\n", "<br/>")


def format_trait(char: CharacterData, phase: int, rts: richtext.RichText) -> str:
    """某个精英阶段满级、满潜能时客户端显示的特性文本。"""

    phases = char.phases or []
    level = phases[phase].max_level if phase < len(phases) else 1
    description, blackboard = trait_description(
        char, level=level, phase=phase, potential=MAX_POTENTIAL_RANK
    )
    if blackboard is not None:
        description = format_paramed_text(description, blackboard_values(blackboard))
    return compile_text(rts, description)


def sub_profession_name(uniequip_table: UniEquipTable, sub_profession_id: str | None):
    sub_prof = (uniequip_table.sub_prof_dict or {}).get(sub_profession_id or "")
    if sub_prof is None:
        return ""
    return sub_prof.sub_profession_name or ""


def item_name(item_table: InventoryData, item_id: str | None) -> str:
    """道具名(未去空白);道具不存在时与旧代码一样抛 ``KeyError``。"""

    if item_id is None or item_table.items is None:
        raise KeyError(item_id)
    return item_table.items[item_id].name or ""


def skin_display(
    skin_table: SkinTable, skin_id: str | None
) -> CharSkinDataDisplaySkin | None:
    """``charSkins[skin_id].displaySkin``,皮肤不存在时为 None。"""

    skin = (skin_table.char_skins or {}).get(skin_id or "")
    return skin.display_skin if skin is not None else None


Params = list[tuple[str, object]]
"""按页面顺序排列的模板参数,键名可能重复。"""


def phase_drawers(skin_table: SkinTable, char_key: str) -> tuple[str, Params, bool]:
    """各精英阶段立绘的画师。

    返回 ``(精英0画师, 与之不同阶段的 |精英N画师= 参数, 是否完整)``。旧实现靠
    异常中断:某阶段皮肤缺画师列表时就停在那里,保留已经得到的部分;这里维持
    同样的语义,``完整`` 为 False 表示中途停下。
    """

    drawer = ""
    phase_params: Params = []
    for skin_p, skin_k in (
        (skin_table.buildin_evolve_map or {}).get(char_key, {}).items()
    ):
        display = skin_display(skin_table, skin_k)
        if display is None or display.drawer_list is None:
            return drawer, phase_params, False
        drawer_temp = ",".join(display.drawer_list)
        if drawer == "":
            drawer = drawer_temp
        elif drawer != drawer_temp:
            phase_params.append((f"精英{skin_p}画师", drawer_temp))
    return drawer, phase_params, True


def cv_params(charword_table: CharWordTable, char_key: str) -> Params:
    """各语言配音的 ``|xx配音=`` 参数;没有配音数据时退化成空的日文配音。

    旧实现同样靠异常中断:某语言缺声优列表时保留已有的参数再补一个空的日文配音。
    """

    voice = (charword_table.voice_lang_dict or {}).get(char_key)
    cv_dict = voice.dict_ if voice is not None else None
    if cv_dict is None:
        return [("日文配音", "")]
    lang_dict: dict[str, str | None] = {
        k: v.name for k, v in (charword_table.voice_lang_type_dict or {}).items()
    }
    lang_dict["CN_MANDARIN"], lang_dict["CN_TOPOLECT"] = "中文", "中文方言"
    params: Params = []
    for k, info in cv_dict.items():
        if info.cv_name is None:
            return [*params, ("日文配音", "")]
        lang = lang_dict.get(k, "未知语言")
        params.append((f"{lang}配音", ",".join(info.cv_name)))
    return params


def attribute_params(prefix: str, attrs: AttributesData) -> dict[str, object]:
    """某个等级的面板属性,键名形如 ``精英0_1级_生命上限``。"""

    return {
        f"{prefix}_生命上限": attrs.max_hp,
        f"{prefix}_攻击": attrs.atk,
        f"{prefix}_防御": attrs.def_,
        f"{prefix}_法术抗性": int(attrs.magic_resistance),
    }


def get_basic_info(
    char: CharacterData,
    char_key: str,
    id_table: IdTable,
    rts: richtext.RichText,
    uniequip_table: UniEquipTable,
    team_table: TeamTable,
    skin_table: SkinTable,
    charword_table: CharWordTable,
) -> str:
    name = char.name or ""
    template = WikiTemplate("CharinfoV2")
    template.add_raw("<!--下方为自动更新部分，您的修改可能会被覆盖-->")
    template.add_all(
        {
            "干员名": name,
            "干员外文名": char.appellation,
            "干员id": char_key,
            "干员序号": id_table[name]["id"] if name in id_table else -1,
        }
    )
    # 特性:各精英阶段满级时的文本,与上一阶段相同则不重复输出
    traits = [format_trait(char, phase, rts) for phase in range(len(char.phases or []))]
    template.add("特性", traits[0] if traits else compile_text(rts, char.description))
    for phase in (1, 2):
        if phase < len(traits) and traits[phase] != traits[phase - 1]:
            template.add(f"特性{phase}", traits[phase])
    template.add_all(
        {
            "稀有度": trans_rarity(char.rarity),
            "职业": trans_profession(char.profession),
            "分支": sub_profession_name(uniequip_table, char.sub_profession_id).strip(),
            "情报编号": char.display_number,
            "所属国家": trans_team(char.nation_id, team_table),
            "所属组织": trans_team(char.group_id, team_table),
            "所属团队": trans_team(char.team_id, team_table),
            "位置": trans_position(char.position),
            "标签": " ".join(char.tag_list or []),
        }
    )
    # 画师
    drawer, drawer_params, _complete = phase_drawers(skin_table, char_key)
    template.add("画师", drawer).add_all(drawer_params)
    # 声优
    template.add_all(cv_params(charword_table, char_key))
    # 常规皮肤description
    phase_skins = (skin_table.buildin_evolve_map or {})[char_key]
    # 旧实现每个阶段都拿精英 0 的画师列表来比较,照旧
    phase_0 = skin_display(skin_table, phase_skins.get(0))
    phase_drawer = (
        ",".join(phase_0.drawer_list)
        if phase_0 is not None and phase_0.drawer_list is not None
        else ""
    )
    for phase_no, skin_id in phase_skins.items():
        display = skin_display(skin_table, skin_id)
        phase_desc = display.content if display is not None else None
        phase_desc = phase_desc.replace("\n", "<br/>") if phase_desc is not None else ""
        template.add(f"精英{phase_no}介绍", phase_desc)
        if phase_drawer != drawer:
            template.add(f"精英{phase_no}画师", phase_drawer)
    # 时装
    skin_counter = 1
    costumes = [
        skin.display_skin
        for skin in (skin_table.char_skins or {}).values()
        if skin.char_id == char_key
        and skin.display_skin is not None
        and skin.display_skin.skin_group_name != "默认服装"
    ]
    for display in sorted(costumes, key=lambda x: x.on_year * 100 + x.on_period):
        template.add(f"时装{skin_counter}名称", display.skin_name)
        if display.drawer_list is not None:
            skin_drawer = ",".join(display.drawer_list)
        else:
            skin_drawer = ""
        if skin_drawer != drawer:
            template.add(f"时装{skin_counter}画师", skin_drawer)
        template.add(f"时装{skin_counter}系列", display.skin_group_name)
        skin_color = display.color_list[0] if display.color_list else ""
        if not skin_color.startswith("#") and len(skin_color) == 6:
            skin_color = "#" + skin_color
        template.add(f"时装{skin_counter}颜色", skin_color)
        skin_desc = re.sub(r"<color name=[^>]*>", "", display.content or "")
        skin_desc = (
            skin_desc.replace("</color>", "").replace("\r", "").replace("\n", "<br/>")
        )
        template.add(f"时装{skin_counter}介绍", skin_desc)
        skin_counter += 1
    template.add_raw("<!--上方为自动更新部分，您的修改可能会被覆盖-->")
    # 原案
    if phase_0 is not None and phase_0.designer_list is not None:
        template.add("原案", ",".join(phase_0.designer_list))
    if name in id_table and id_table[name]["approach"] in ["活动获得", "限定寻访"]:
        template.add("限定", 1)
    return str(template)


def get_char_approach(char: CharacterData, id_table: IdTable) -> str:
    name = char.name or ""
    if name in id_table and id_table[name]["approach"]:
        item_obtain_approach = id_table[name]["approach"]
    else:
        item_obtain_approach = char.item_obtain_approach or ""
    template = WikiTemplate("干员获得方式").add_all(
        {
            "获得方式": item_obtain_approach,
            "上线时间": id_table[name]["date"] if name in id_table else "",
        }
    )
    return str(template)


def get_phases_data(
    char: CharacterData,
    char_key: str,
    uniequip_table: UniEquipTable,
    battle_equip_table: dict[str, BattleEquipPack],
    team_table: TeamTable,
) -> str:
    template = WikiTemplate("属性")
    phases = char.phases or []
    initial = phase_attributes(phases[0])[0]

    block_cnt_2 = initial.block_cnt
    block_data = str(initial.block_cnt)
    cost = initial.cost
    cost_data = str(cost)
    for phases_num in range(1, len(phases)):
        attrs = phase_attributes(phases[phases_num])[0]
        block_cnt_2 = attrs.block_cnt
        block_data += "→" + str(block_cnt_2)
        cost_2 = attrs.cost
        if cost != cost_2 or (phases_num == 1 and cost == cost_2):
            cost_data += "→" + str(cost_2)
            cost = cost_2
    if block_cnt_2 == initial.block_cnt:
        block_data = str(initial.block_cnt)

    template.add_all(
        {
            "再部署": f"{int(initial.respawn_time)}s",
            "部署费用": cost_data,
            "阻挡数": block_data,
            "攻击速度": f"{initial.base_attack_time}s",
        }
    )
    if char.main_power is not None:
        power_list = []
        for power_value in (
            char.main_power.nation_id,
            char.main_power.group_id,
            char.main_power.team_id,
        ):
            if power_value is not None:
                p_trans = trans_team(power_value, team_table)
                if p_trans != "" and p_trans != "?":
                    power_list.append(p_trans)
        if power_list:
            template.add("所属势力", ",".join(power_list))
    if char.sub_power is not None:
        sub_power_list_lv0 = []
        for sub_power_group in char.sub_power:
            if sub_power_group is None:
                continue
            sub_power_list_lv1 = []
            for sub_power_value in (
                sub_power_group.nation_id,
                sub_power_group.group_id,
                sub_power_group.team_id,
            ):
                sp_trans = trans_team(sub_power_value, team_table)
                if sp_trans != "" and sp_trans != "?":
                    sub_power_list_lv1.append(sp_trans)
            if sub_power_list_lv1 != []:
                sub_power_list_lv0.append(",".join(sub_power_list_lv1))
        template.add("隐藏势力", ";;".join(sub_power_list_lv0))
    for phases_num, phase in enumerate(phases):
        frames = phase_attributes(phase)
        if phases_num == 0:
            template.add_all(attribute_params("精英0_1级", frames[0]))
        template.add(f"精英{phases_num}_满级", phase.max_level)
        template.add_all(attribute_params(f"精英{phases_num}_满级", frames[-1]))

    favor = favor_attributes(char)
    template.add_all(
        {
            "信赖加成_生命上限": favor.max_hp,
            "信赖加成_攻击": favor.atk,
            "信赖加成_防御": favor.def_,
        }
    )

    potential_rank_data = []
    potential_rank_type = []
    potential_ranks = char.potential_ranks or []
    for potential_rank in potential_ranks:
        modifiers = (
            potential_rank.buff.attributes.attribute_modifiers
            if potential_rank.buff and potential_rank.buff.attributes
            else None
        )
        if potential_rank.type == "BUFF" and modifiers:
            attribute_type = modifiers[0].attribute_type
            wiki_type = {
                "ATK": "atk",
                "DEF": "def",
                "MAX_HP": "hp",
                "MAGIC_RESISTANCE": "res",
                "COST": "cost",
                "ATTACK_SPEED": "interval",
                "RESPAWN_TIME": "re_deploy",
            }.get(attribute_type)
            if wiki_type is None:
                potential_rank_data.append("")
                potential_rank_type.append("")
                logger.info(
                    f"Error! Char {char.name} attributeType {attribute_type} dont know!"
                )
            else:
                potential_rank_data.append(str(int(modifiers[0].value)))
                potential_rank_type.append(wiki_type)
        else:
            potential_rank_data.append("")
            potential_rank_type.append("")
    if 0 < len(potential_ranks) < 5:
        template.add("潜能上限", len(potential_ranks) + 1)
    elif len(potential_ranks) == 0:
        template.add("潜能上限", 1)
    if any(potential_rank_data):
        template.add("潜能", ",".join(potential_rank_data))
        template.add("潜能类型", ",".join(potential_rank_type))

    equip_dict = uniequip_table.equip_dict or {}
    uniequip_count = 0
    for equip_id in (uniequip_table.char_equip or {}).get(char_key, []):
        equip_info = equip_dict.get(equip_id)
        if equip_info is None:
            continue
        if equip_info.type == "INITIAL":
            template.add("初始模组名", equip_info.uni_equip_name)
        elif equip_info.type == "ADVANCED":
            uniequip_count += 1
            template.add(f"模组{uniequip_count}名", equip_info.uni_equip_name)
            pack = battle_equip_table.get(equip_id)
            if pack is not None and pack.phases:
                template.add(
                    f"模组{uniequip_count}数据",
                    ";".join(
                        f"{x.key}:{x.value:.0f}"
                        for x in pack.phases[-1].attribute_blackboard or []
                    ),
                )

    return str(template)


def get_range_data(char: CharacterData) -> str:
    template = WikiTemplate("干员攻击范围")
    for range_num, phase in enumerate(char.phases or []):
        template.add(f"精英{range_num}范围", phase.range_id)
    return str(template)


def get_talent_list(char: CharacterData, rts: richtext.RichText) -> str:
    if char.talents is None:
        return "该干员没有天赋"
    id_char_list = ["一", "二", "三"]
    template = WikiTemplate("天赋列表")
    for bundle in char.talents:
        candidates = visible_talent_candidates(bundle)
        if not candidates:
            continue
        talent_num = id_char_list.pop(0) if id_char_list else "X"
        for index, talent in enumerate(candidates, start=1):
            condition = talent.unlock_condition
            talent_condition = get_tal_condition(
                talent.required_potential_rank,
                phase_index(condition.phase) if condition else 0,
                condition.level if condition else 1,
            )
            key = f"第{talent_num}天赋{index}"
            template.add_all(
                {
                    key: talent.name,
                    f"{key}条件": talent_condition,
                    f"{key}效果": compile_text(rts, talent.description),
                }
            )
    return str(template)


def get_potential_list(char: CharacterData) -> str:
    if not char.potential_ranks:
        return "该干员无法提升潜能"
    template = WikiTemplate("潜能提升")
    for potential_id, rank in enumerate(char.potential_ranks, start=2):
        template.add(f"潜能{potential_id}", rank.description)
    return str(template)


def get_skill_text(
    skill_table: dict[str, SkillDataBundle], skill_id: str, rts: richtext.RichText
) -> str:
    skill_data = skill_table.get(skill_id)
    if skill_data is None:
        logger.info(f"skillId {skill_id} not found")
        return ""
    levels = skill_data.levels or []
    if all(level.description is None for level in levels):
        # 召唤物/装置的内部技能没有描述,客户端也不展示
        logger.info(f"skillId {skill_id} has no description, skipped")
        return ""
    first = levels[0]
    template = WikiTemplate("技能")
    template.add("技能名", first.name)
    template.add(
        "技能类型1", trans_sp_type(first.sp_data.sp_type if first.sp_data else "")
    )
    template.add_optional("技能类型2", trans_skill_type(first.skill_type))
    if first.range_id:
        template.add("技能范围", first.range_id)
        if any(level.range_id != first.range_id for level in levels):
            logger.info(f"技能 {first.name} 范围随等级变化")
    for idx, level_data in enumerate(levels):
        blackboard = blackboard_values(level_data.blackboard)
        # 暴雨一技能的描述引用了黑板里没有的 duration,客户端会把 {duration} 原样留下
        if skill_data.skill_id == "skchr_zebra_1":
            blackboard.setdefault("duration", level_data.duration)
        skill_description = compile_text(
            rts, format_paramed_text(level_data.description, blackboard)
        )

        if level_data.duration == 0 or level_data.duration == -1:
            skill_duration = ""
        elif level_data.duration == int(level_data.duration):
            skill_duration = str(int(level_data.duration))
        else:
            skill_duration = str(level_data.duration)
        if idx >= 7:
            skill_num = "专精" + str(idx - 6)
        else:
            skill_num = str(idx + 1)
        sp_data = level_data.sp_data
        template.add_all(
            {
                f"技能{skill_num}描述": skill_description,
                f"技能{skill_num}初始": sp_data.init_sp if sp_data else 0,
                f"技能{skill_num}消耗": sp_data.sp_cost if sp_data else 0,
                f"技能{skill_num}持续": skill_duration,
            }
        )
    return str(template)


def get_skill_list(
    char: CharacterData, skill_table: dict[str, SkillDataBundle], rts: richtext.RichText
) -> str:
    skill_list = ""
    if char.skills:
        for skill_id, skill in enumerate(char.skills):
            if skill.skill_id is None:
                continue
            condition = skill.unlock_cond
            skill_list += "\n'''技能{num}（{skill_cond}开放）'''\n".format(
                num=skill_id + 1,
                skill_cond=get_tal_condition(
                    0,
                    phase_index(condition.phase) if condition else 0,
                    condition.level if condition else 1,
                ),
            )
            try:
                skill_list += get_skill_text(skill_table, skill.skill_id, rts)
            except Exception:
                logger.exception(f"{char.name}技能{skill_id + 1}解析出错")
    else:
        skill_list = "\n该干员没有技能"
    return skill_list


async def get_token_info(
    wiki: Wiki,
    char: CharacterData,
    update_token_page: bool,
    character_table: dict[str, CharacterData],
    skill_table: dict[str, SkillDataBundle],
    rts: richtext.RichText,
) -> str:
    # 用 dict 保持顺序:先 displayTokenDict,再技能覆盖的召唤物
    token_keys: dict[str, None] = dict.fromkeys(char.display_token_dict or {})
    for skill in char.skills or []:
        if skill.override_token_key is not None:
            token_keys.setdefault(skill.override_token_key, None)
    token_info = "\n==召唤物信息=="
    if not token_keys:
        return ""
    for token_key in token_keys:
        if token_key not in character_table:
            continue
        token_info += "\n" + inline_template(
            "参阅", character_table[token_key].name, "该持有者的召唤物"
        )
    for token_key in token_keys:
        token = character_table.get(token_key)
        if token is None:
            continue
        token_phases = token.phases or []
        template = WikiTemplate("召唤物信息").add_all(
            {
                "中文名称": token.name,
                "外文名称": token.appellation,
                "持有者": char.name,
                "使用条件": "—",
                "部署位置": {"MELEE": "近战位", "RANGED": "远程位", "ALL": "全部位"}[
                    token.position
                ],
                "攻击范围": token_phases[0].range_id,
            }
        )
        if any(phase.range_id != token_phases[0].range_id for phase in token_phases):
            logger.info(f"召唤物{token.name} rangeId changes.")
        for phases_num, phase in enumerate(token_phases):
            frames = phase_attributes(phase)
            template.add_all(attribute_params(f"精英{phases_num}_1级", frames[0]))
            template.add(f"精英{phases_num}_满级", phase.max_level)
            template.add_all(attribute_params(f"精英{phases_num}_满级", frames[-1]))
        final = phase_attributes(token_phases[0])[-1]
        template.add_all(
            {
                "再部署时间": f"{final.respawn_time}s",
                "部署费用": final.cost,
                "阻挡数": final.block_cnt,
                "攻击间隔": f"{final.base_attack_time}s",
                "嘲讽等级": final.taunt_level,
                "部署占用数": "?",
            }
        )
        token_page = f"==召唤物信息==\n{template}"
        skill_list, id_count = "\n==召唤物技能==", 0
        for skill_data in token.skills or []:
            if skill_data.skill_id is None:
                continue
            id_count += 1
            condition = skill_data.unlock_cond
            skill_list += "\n'''技能{num}（{skill_cond}开放）'''\n".format(
                num=id_count,
                skill_cond=get_tal_condition(
                    0,
                    phase_index(condition.phase) if condition else 0,
                    condition.level if condition else 1,
                ),
            )
            try:
                skill_list += get_skill_text(skill_table, skill_data.skill_id, rts)
            except Exception:
                logger.exception(f"召唤物{token.name}技能解析出错")
        if id_count > 0:
            token_page += skill_list
        token_page += "\n==召唤物模型==\n" + inline_template(
            "SpineId", f"id={token_key}"
        )

        if update_token_page:
            await wiki.edit(title=token.name, text=token_page, summary="update")
        else:
            await wiki.edit(
                title=token.name,
                text=token_page,
                summary="init",
                createonly="1",
            )
        logger.info(f"Created: {token.name}.")
    return token_info


# 同名后勤技能在 wiki 上按房间 / 精英阶段区分的显示名
BUILDING_BUFF_NAME_OVERRIDES = {
    "control_dorm_rec[000]": "领袖(控制中枢)",
    "dorm_rec_all[013]": "领袖(宿舍)",
    "train_spd_doubleProf[100]": "红龙之血(精英0)",
    "train_spd_doubleProf[110]": "红龙之血(精英2)",
    "control_token_prod_spd2[000]": "以身作则(控制中枢)",
    "train_spd&profession2[440]": "以身作则(训练室)",
    "manu_prod_spd&limit&cost[200]": "得心应手(制造站)",
    "meet_spd_condChar[000]": "得心应手(会客室)",
    "control_prod_bd_spd[000]": "丰富工作经验(精英0)",
    "control_prod_bd_spd[010]": "丰富工作经验(精英2)",
    "power_rec_spd[008]": "澎湃紊流(精英0)",
    "power_rec_spd[009]": "澎湃紊流(精英1)",
    "meet_spd[1020]": "线索搜集·β(行箸)",
    "recycle_spd&cost[000]": "拾荒者(回收站)",
}


def get_building_skill(
    building_data: BuildingData, char_key: str, rts: richtext.RichText
) -> str:
    char_building_skill = (building_data.chars or {}).get(char_key)
    if char_building_skill is None:
        return "该干员无后勤技能"
    slots = char_building_skill.buff_char or []
    if not any(slot.buff_data for slot in slots):
        return "该干员无后勤技能"
    buffs = building_data.buffs or {}
    rooms = building_data.rooms or {}
    template = WikiTemplate("后勤技能")
    for building_skill_id, slot in enumerate(slots):
        for building_skill_id_2, temp in enumerate(slot.buff_data or []):
            key = f"后勤技能{building_skill_id + 1}-{building_skill_id_2 + 1}"
            if temp.buff_id is None:
                raise KeyError(temp.buff_id)
            buff = buffs[temp.buff_id]
            buff_name = buff.buff_name
            display_name = BUILDING_BUFF_NAME_OVERRIDES.get(temp.buff_id)
            if display_name is None:
                template.add(key, buff_name)
            else:
                # 同名技能用区分后的名字,游戏内的原名放进显示名
                template.add(key, display_name).add(f"{key}显示名", buff_name)
            template.add_all(
                {
                    f"{key}ID": temp.buff_id,
                    f"{key}排序": buff.sort_id,
                    f"{key}房间": rooms[buff.room_type].name,
                    f"{key}图标": buff.skill_icon,
                    f"{key}描述": rts.compile(buff.description),
                }
            )
            cond = temp.cond
            phase = trans_phase(cond.phase) if cond is not None else 0
            template.add(f"{key}阶段", f"精英{phase}")
            if cond is not None and cond.level != 1:
                template.add(f"{key}等级", f"{cond.level}级")
    return str(template)


def material_cost(item_table: InventoryData, costs: Iterable[ItemBundle]) -> str:
    return " ".join(
        inline_template("材料消耗", item_name(item_table, cost.id).rstrip(), cost.count)
        for cost in costs
    )


def get_phase_list(
    char: CharacterData, gamedata_const: GameDataConsts, item_table: InventoryData
) -> str:
    phases = char.phases or []
    if len(phases) < 2:
        return "该干员无法精英化"
    template = WikiTemplate("精英化材料")
    for phase_id in range(1, len(phases)):
        evolve_cost = phases[phase_id].evolve_cost
        if evolve_cost is None:
            return "该干员无精英化材料需求"
        money = (gamedata_const.evolve_gold_cost or [])[rarity_stars(char.rarity) - 1][
            phase_id - 1
        ]
        if int(money / 10000) == money / 10000:
            money_str = str(int(money / 10000))
        else:
            money_str = str(float(money / 10000))
        materials = [inline_template("材料消耗", "龙门币", f"{money_str}w")]
        if evolve_cost:
            materials.append(material_cost(item_table, evolve_cost))
        template.add(f"精{phase_id}", " ".join(materials))
    return str(template)


def get_skill_levelup_list(char: CharacterData, item_table: InventoryData) -> str:
    if not char.skills:
        return "该干员没有技能"
    template = WikiTemplate("技能升级材料")
    for level_id, level_cost in enumerate(char.all_skill_lvlup or []):
        if level_cost.lvl_up_cost is None:
            return "该干员无技能升级材料需求"
        template.add(
            str(level_id + 2), material_cost(item_table, level_cost.lvl_up_cost)
        )
    for skill_id, skill in enumerate(char.skills):
        if skill.level_up_cost_cond:
            for i in [8, 9, 10]:
                cost = skill.level_up_cost_cond[i - 8].level_up_cost or []
                template.add(
                    f"{trans_id(skill_id + 1)}{i}", material_cost(item_table, cost)
                )
    return str(template)


EQUIP_ATTR_NAMES = {
    "max_hp": "生命",
    "atk": "攻击",
    "def": "防御",
    "magic_resistance": "法术抗性",
    "respawn_time": "再部署",
    "cost": "部署费用",
    "block_cnt": "阻挡数",
    "attack_speed": "攻击速度",
}

# 模组解锁所需信赖值(favor point)→ 页面上的信赖百分比,其余值留给编辑者补
FAVOR_PERCENT: dict[int | None, str] = {0: "0", 2732: "50", 10070: "100"}


def favor_percent(favor: int | None) -> str:
    return FAVOR_PERCENT.get(favor, "?")


def get_battle_equip(
    char: CharacterData,
    char_key: str,
    battle_equip_table: dict[str, BattleEquipPack],
    uniequip_table: UniEquipTable,
    item_table: InventoryData,
    rts: richtext.RichText,
) -> list[str]:
    equip_ids = (uniequip_table.char_equip or {}).get(char_key)
    if equip_ids is None:
        return []
    content = ["\n==模组=="]
    equip_dict = uniequip_table.equip_dict or {}
    mission_dict = uniequip_table.mission_list or {}
    for equip in equip_ids:
        equip_info = equip_dict.get(equip)
        if equip_info is None:
            continue
        equip_name = (equip_info.uni_equip_name or "").strip()
        b_info = (equip_info.uni_equip_desc or "").strip().replace("\n", "<br>")
        template = WikiTemplate("模组").add("名称", equip_name)
        if equip_info.type == "INITIAL":
            template.add_all(
                {
                    "基础证章": "yes",
                    "分支": sub_profession_name(uniequip_table, char.sub_profession_id),
                    "模组图标": equip_info.uni_equip_icon,
                    "类型图标": equip_info.type_icon,
                    "基础信息": b_info,
                }
            )
            content.append(f"\n==={equip_name}===\n{template}")
            continue

        template.add("类型", f"{equip_info.type_name_1}-{equip_info.type_name_2}")
        if equip_info.equip_shining_color != "grey":
            template.add("类型颜色", equip_info.equip_shining_color)
        template.add("模组图标", equip_info.uni_equip_icon)
        template.add("类型图标", equip_info.type_icon)
        # 属性、特性、天赋各自按阶段排列,三组依次输出
        attrs: Params = []
        traits: Params = []
        talents: Params = []
        pack = battle_equip_table.get(equip)
        for e_lv, e_lv_data in enumerate(pack.phases or [] if pack else []):
            idx = "" if e_lv == 0 else str(e_lv + 1)
            for i in e_lv_data.attribute_blackboard or []:
                attr_name = EQUIP_ATTR_NAMES.get(i.key or "", "其他")
                attrs.append((f"{attr_name}{idx}", f"{i.value:.0f}"))
            for e in e_lv_data.parts or []:
                trait_bundle = e.override_trait_data_bundle
                if trait_bundle and trait_bundle.candidates and e_lv == 0:
                    candidate = trait_bundle.candidates[0]
                    trait_text = ""
                    if candidate.additional_description is not None:
                        traits.append((f"特性{idx}追加", "yes"))
                        trait_text = candidate.additional_description
                    elif candidate.override_descripton is not None:
                        trait_text = candidate.override_descripton
                    trait_text = compile_text(
                        rts,
                        format_paramed_text(
                            trait_text, blackboard_values(candidate.blackboard)
                        ),
                    )
                    if trait_text != "":
                        traits.append((f"特性{idx}", trait_text))
                talent_bundle = e.add_or_override_talent_data_bundle
                if talent_bundle and talent_bundle.candidates:
                    upgrade = talent_bundle.candidates[0].upgrade_description
                    if upgrade:
                        talents.append((f"天赋{idx}", rts.compile(upgrade)))
        template.add_all(attrs).add_all(traits).add_all(talents)
        for idx, mission_id in enumerate(equip_info.mission_list or [], start=1):
            mission = mission_dict.get(mission_id)
            desc = (mission.desc if mission else None) or ""
            result = re.search(r"通关主题曲(.+?)；", desc)
            if result:
                desc = desc.replace(result.group(1), f"[[{result.group(1)}]]")
            template.add(f"任务{idx}", desc)
        template.add("解锁等级", equip_info.unlock_level)
        favors = equip_info.unlock_favors
        if favors is not None:
            template.add_all(
                {
                    "解锁信赖": favor_percent(favors.get("1")),
                    "解锁信赖2": favor_percent(favors.get("2")),
                    "解锁信赖3": favor_percent(favors.get("3")),
                }
            )
        else:
            template.add("解锁信赖", 0)
        for idx, lv_cost in enumerate((equip_info.item_cost or {}).values()):
            materials = [
                inline_template(
                    "材料消耗",
                    item_name(item_table, i.id),
                    i.count if i.count < 10000 else f"{i.count / 10000:.0f}万",
                )
                for i in lv_cost
            ]
            if materials:
                suffix = "" if idx == 0 else idx + 1
                template.add(f"材料消耗{suffix}", " ".join(materials))
        template.add("基础信息", b_info)
        content.append(
            f"\n==={equip_name}===\n<section begin=专属模组 />"
            f"\n{template}\n<section end=专属模组 />"
        )
    return content


def get_related_item(char: CharacterData, item_table: InventoryData) -> str:
    template = WikiTemplate("相关道具").add_all(
        {"干员简介": char.item_usage, "干员简介补充": char.item_desc}
    )
    potential_item = (item_table.items or {}).get(char.potential_item_id or "")
    if char.potential_item_id and potential_item is not None:
        template.add_all(
            {"信物用途": potential_item.usage, "信物描述": potential_item.description}
        )
    return str(template)


def first_story_text(view: HandBookStoryViewData) -> str:
    """档案某一节的正文(每节只有一段)。"""

    return (view.stories or [])[0].story_text or ""


def get_stories_list(
    char: CharacterData, stories_table: HandbookInfoTable, char_key: str
) -> tuple[str, str]:
    handbook = (stories_table.handbook_dict or {}).get(char_key)
    if handbook is None:
        return "", "该干员无人员档案"
    story_views = handbook.story_text_audio or []
    stories1 = first_story_text(story_views[0])
    stories2 = first_story_text(story_views[1])
    stories3 = ""
    for i in story_views:
        if i.story_title == "临床诊断分析":
            stories3 = first_story_text(i)

    _doc_exp, doc2 = replace_doc_exp(stories1)
    doc7 = replace_basic_doc(stories1, "矿石病感染情况")
    result = re.search(r"确认为(.*)感染者", doc7)
    if result:
        doc8 = result.group(1) + "感染者"
    else:
        doc8 = doc7

    # 基础档案、综合体检测试、临床诊断分析三组字段之间各空一行
    info = WikiTemplate("人员档案set")
    info.add_all(
        {
            "性别": replace_basic_doc(stories1, "性别"),
            "战斗经验": doc2,
            "出身地": replace_basic_doc(stories1, "出身地"),
            "生日": replace_basic_doc(stories1, "生日"),
            "种族": replace_basic_doc(stories1, "种族"),
            "身高": replace_basic_doc(stories1, "身高"),
            "矿石病感染情况": doc7,
            "是否感染者": doc8,
        }
    )
    info.add_raw("")
    info.add_all(
        {
            key: replace_basic_doc(stories2, key)
            for key in (
                "物理强度",
                "战场机动",
                "生理耐受",
                "战术规划",
                "战斗技巧",
                "源石技艺适应性",
            )
        }
    )
    info.add_raw("")
    info.add_all(
        {
            key: replace_basic_doc(stories3, key).replace(" ", "")
            for key in ("体细胞与源石融合率", "血液源石结晶密度")
        }
    )

    stories = WikiTemplate("人员档案")
    for stories_id, view in enumerate(story_views, start=1):
        story = (view.stories or [])[0]
        story_text = (story.story_text or "").replace("\r\n", "\n")
        if char.name == "伊芙利特":
            story_text = handle_ifrit(story_text)
        story_title = view.story_title
        story_condition_id = story.un_lock_type
        if story_condition_id == "DIRECT":
            story_condition = "初始开放"
        elif story_condition_id == "AWAKE":
            story_condition = "提升至精英阶段2以查看"
        elif story_condition_id == "FAVOR":
            story_condition = f"提升信赖至{story.un_lock_param}%以查看"
        elif story_condition_id == "PATCH":
            story_condition = "升变解锁"
        else:
            story_condition = ""
        stories.add_all(
            {
                f"档案{stories_id}": story_title,
                f"档案{stories_id}条件": story_condition,
                f"档案{stories_id}文本": story_text,
            }
        )
    return str(info), f"\n{stories}"


def get_handbook_avg(
    char: CharacterData,
    stories_table: HandbookInfoTable,
    char_key: str,
    medal_table: MedalData,
) -> str:
    handbook = (stories_table.handbook_dict or {}).get(char_key)
    if handbook is None or not handbook.handbook_avg_list:
        return ""
    # 外层 {{干员密录|list=...}} 的唯一参数紧跟模板名,里面是逐条的 /list 调用
    avg_content = "\n==干员密录==\n{{干员密录|list="
    for avg in handbook.handbook_avg_list:
        phase: int | str | None = -1
        lv: int | str | None = -1
        favor: int | str | None = -1
        for p in avg.unlock_param or []:
            if p.unlock_type == "AWAKE":
                phase = p.unlock_param_1
                lv = p.unlock_param_2
            elif p.unlock_type == "FAVOR":
                favor = p.unlock_param_1
            else:
                logger.info(f"Unknown handbook_avg unLock condition for {char.name}.")
        template = WikiTemplate("干员密录/list").add_all(
            {"精英化": phase, "等级": lv, "信赖": favor}
        )
        for medal in medal_table.medal_list or []:
            if medal.medal_type == "storyMedal" and avg.story_set_id in (
                medal.unlock_param or []
            ):
                template.add("蚀刻章override", medal.medal_id)
                break
        template.add("storySetName", avg.story_set_name)
        avg_list = avg.avg_list or []
        for idx, story in enumerate(avg_list, start=1):
            story_txt = f"{inline_template('FULLPAGENAME')}/干员密录/{avg.sort_id}"
            if len(avg_list) > 1:
                story_txt += f"-{story.story_sort}"
            template.add(f"storyIntro{idx}", story.story_intro)
            template.add(f"storyTxt{idx}", story_txt)
        avg_content += f"\n{template}"
    avg_content += "\n}}"
    return avg_content


def get_handbook_stage(
    char: CharacterData,
    char_key: str,
    stories_table: HandbookInfoTable,
    item_table: InventoryData,
    rts: richtext.RichText,
) -> str:
    stage_info = (stories_table.handbook_stage_data or {}).get(char_key)
    if stage_info is None:
        return ""
    unlock_params = stage_info.unlock_param or []
    if len(unlock_params) != 1 or unlock_params[0].unlock_type != "AWAKE":
        logger.info(f"Unknown handbook_stage unLock condition for {char.name}.")
        unlock_phase, unlock_lv = "", ""
    else:
        unlock_phase = unlock_params[0].unlock_param_1
        unlock_lv = unlock_params[0].unlock_param_2
    # zoneName / stageName / picId 数据里没有,留给编辑者填
    template = WikiTemplate("悖论模拟").add_all(
        {
            "name": stage_info.name,
            "description": rts.compile(stage_info.description).replace(
                "#FFFFFF", "#000000"
            ),
            "精英化": unlock_phase,
            "等级": unlock_lv,
            "zoneName": "",
            "stageName": "",
            "picId": "",
        }
    )
    reward_items = stage_info.reward_item or []
    for idx, r in enumerate(reward_items, start=1):
        template.add(f"报酬内容{idx}", item_name(item_table, r.id).rstrip())
        template.add(f"报酬数量{idx}", r.count)
    if len(reward_items) > 1:
        logger.info(f"Too many handbook_stage rewardItem for {char.name}.")
    return f"\n==悖论模拟==\n{template}"


def trans_id(id):
    return {
        1: "一",
        2: "二",
        3: "三",
    }.get(id, "X")


def trans_profession(profession):
    return {
        "TANK": "重装",
        "PIONEER": "先锋",
        "SUPPORT": "辅助",
        "SNIPER": "狙击",
        "MEDIC": "医疗",
        "WARRIOR": "近卫",
        "CASTER": "术师",
        "SPECIAL": "特种",
    }.get(profession, profession)


def trans_team(team_id: str | None, team_table: TeamTable) -> str:
    if team_id is None:
        return ""
    team = team_table.get(team_id)
    if team is None:
        return "?"
    return team.power_name or ""


def trans_skill_type(skill_type):
    """技能触发方式,即客户端技能标签里的 TAG_SKILL_TRIGGER_*。"""

    return {
        0: "被动",
        1: "手动触发",
        2: "自动触发",
        "PASSIVE": "被动",
        "MANUAL": "手动触发",
        "AUTO": "自动触发",
    }.get(skill_type, "")


def trans_sp_type(sp_type):
    """技力回复方式,即客户端技能标签里的 TAG_SKILL_SP_*。

    客户端(DataConvertUtil.LoadSkillTags)只认 1/2/4 三个位,其余取值不显示
    回复标签。数据里常见的 8 是 SpTypeIndex.NEVER_USE(技力不回复),不在 SpType
    枚举里,JSON 直接存数字,模型转成字符串 "8";它和"被动"无关,被动看的是
    skillType。
    """

    return {
        1: "自动回复",
        2: "攻击回复",
        4: "受击回复",
        "INCREASE_WITH_TIME": "自动回复",
        "INCREASE_WHEN_ATTACK": "攻击回复",
        "INCREASE_WHEN_TAKEN_DAMAGE": "受击回复",
    }.get(sp_type, "")


def trans_position(position):
    return {"MELEE": "近战位", "RANGED": "远程位", "ALL": "近战/远程位"}[position]


def trans_phase(phase):
    return {"PHASE_0": 0, "PHASE_1": 1, "PHASE_2": 2, "PHASE_3": 3}.get(phase, phase)


def trans_rarity(rarity):
    return {
        "TIER_1": 0,
        "TIER_2": 1,
        "TIER_3": 2,
        "TIER_4": 3,
        "TIER_5": 4,
        "TIER_6": 5,
    }.get(rarity, rarity)


def replace_basic_doc(text, cond):
    p1 = rf"【{cond}】(\s*)([^\n]*)"
    pattern1 = re.compile(p1)
    result = re.search(pattern1, text)
    if result:
        return result.group(2).rstrip()
    return ""


def replace_doc_exp(text):
    p1 = r"【([^【]*)经验】(\s*)([^\n]*)"
    pattern1 = re.compile(p1)
    result = re.search(pattern1, text)
    if result:
        return result.group(1) + "经验", result.group(3).rstrip()
    return "", ""


def handle_ifrit(text):
    text = text.replace("|", "<nowiki>|</nowiki>")
    text = text.replace("=", "<nowiki>=</nowiki>")
    return text


def get_tal_condition(potential_rank, phase, level):
    condition = ""
    if phase == 0:
        condition += "精英0"
    elif phase == 1:
        condition += "精英1"
    elif phase == 2:
        condition += "精英2"
    if level != 1:
        condition += " " + str(level) + "级"
    if potential_rank != 0:
        condition += " 潜能" + str(potential_rank + 1)
    return condition


# {{{{ads/operator}}}}
content = """{{{{干员页面名|{name}|{name}|{name}}}}}{{{{pathnav2|干员一览}}}}
{{{{ads/normal}}}}{{{{ads/mobile}}}}
==干员信息==
{basic_info}
==获得方式==
{char_approach}
==属性==
{phases_data}
==攻击范围==
{range_data}
==天赋==
{talents}
==潜能提升==
{potential}
==技能=={skill}
==后勤技能==
{building}{token_info}
==精英化材料==
{phase}
==技能升级材料==
{skill_levelup}{equip}
==相关道具==
{related_item}
==干员档案==
{stories}
==语音记录==
{{{{参阅三|{{{{FULLPAGENAME}}}}|yy}}}}
{{{{:{{{{FULLPAGENAME}}}}/语音记录}}}}{handbook_avg}{handbook_stage}
==干员模型==
{{{{spineId}}}}
==注释与链接==
<references/>
{{{{干员导航}}}}"""


def iter_operators(character_table: dict[str, CharacterData]):
    """可获得的干员(去掉召唤物、装置和不可获得角色),名字去掉首尾空白。"""

    for char_key, char in character_table.items():
        char.name = (char.name or "").strip()
        if char.profession in ("TRAP", "TOKEN"):
            continue
        if char.is_not_obtainable:
            continue
        yield char_key, char


@job
async def run(
    wiki: Wiki,
    character_table: params.CharacterTable,
    uniequip_table: params.UniEquipTable,
    battle_equip_table: params.BattleEquipTable,
    skill_table: params.SkillTable,
    building_data: params.BuildingData,
    item_table: params.ItemTable,
    team_table: params.HandbookTeamTable,
    stories_table: params.HandbookInfoTable,
    skin_table: params.SkinTable,
    gamedata_const: params.GamedataConst,
    charword_table: params.CharwordTable,
    medal_table: params.MedalTable,
    id_table: params.CharIdTable,
    rts: params.RichText,
    char_list: Annotated[list[str], params.category("分类:干员")],
) -> bool:
    flag_new_char = False
    update_token_page = False

    for char_key, char in iter_operators(character_table):
        if char.name in char_list:
            continue
        if char.name not in id_table:
            logger.info(f"Unknown Character: {char_key} {char.name}.")

        basic_info = get_basic_info(
            char,
            char_key,
            id_table,
            rts,
            uniequip_table,
            team_table,
            skin_table,
            charword_table,
        )
        char_approach = get_char_approach(char, id_table)
        phases_data = get_phases_data(
            char, char_key, uniequip_table, battle_equip_table, team_table
        )
        range_data = get_range_data(char)
        talent_list = get_talent_list(char, rts)
        potential_list = get_potential_list(char)
        skill_list = get_skill_list(char, skill_table, rts)
        token_info = await get_token_info(
            wiki,
            char,
            update_token_page,
            character_table,
            skill_table,
            rts,
        )
        building_skill = get_building_skill(building_data, char_key, rts)
        phase_list = get_phase_list(char, gamedata_const, item_table)
        skill_levelup_list = get_skill_levelup_list(char, item_table)
        battle_equip = "".join(
            get_battle_equip(
                char,
                char_key,
                battle_equip_table,
                uniequip_table,
                item_table,
                rts,
            )
        )
        related_item = get_related_item(char, item_table)
        stories_list_set, stories_list = get_stories_list(char, stories_table, char_key)
        stories_list = stories_list_set + stories_list
        handbook_avg = get_handbook_avg(char, stories_table, char_key, medal_table)
        handbook_stage = get_handbook_stage(
            char, char_key, stories_table, item_table, rts
        )

        char_info = content.format(
            name=char.name,
            char_approach=char_approach,
            basic_info=basic_info,
            phases_data=phases_data,
            range_data=range_data,
            talents=talent_list,
            potential=potential_list,
            skill=skill_list,
            building=building_skill,
            token_info=token_info,
            phase=phase_list,
            skill_levelup=skill_levelup_list,
            equip=battle_equip,
            related_item=related_item,
            stories=stories_list,
            handbook_avg=handbook_avg,
            handbook_stage=handbook_stage,
        )

        flag_new_char = True
        await wiki.edit(
            title=char.name,
            text=char_info,
            summary="init",
            bot=None,
            minor=True,
            createonly="1",
        )
        await wiki.protect(
            title=char.name,
            protections="edit=autoconfirmed|move=sysop|delete=sysop",
            reason="protect",
        )
        if char.name != char.appellation:
            redirect_text = f"#redirect [[{char.name}]]"
            await wiki.edit(
                title=char.appellation,
                text=redirect_text,
                summary="init",
                createonly=True,
            )
        logger.info(f"Created: {char.name}.")

    return flag_new_char


SKIP_UPDATE_KEYS = [
    "char_512_aprot",
    "char_508_aguard",
    "char_509_acast",
    "char_511_asnipe",
    "char_510_amedic",
    "char_513_apionr",
]


@job
async def update(
    wiki: Wiki,
    character_table: params.CharacterTable,
    uniequip_table: params.UniEquipTable,
    battle_equip_table: params.BattleEquipTable,
    building_data: params.BuildingData,
    item_table: params.ItemTable,
    team_table: params.HandbookTeamTable,
    skin_table: params.SkinTable,
    charword_table: params.CharwordTable,
    rts: params.RichText,
) -> None:
    operators = [
        (char_key, char)
        for char_key, char in iter_operators(character_table)
        if char_key not in SKIP_UPDATE_KEYS
    ]
    # 一次性批量读取全部干员页面,再逐个比对、按需编辑
    pages = await wiki.read_many(char.name or "" for _, char in operators)
    for char_key, char in operators:
        if char.name not in pages:
            raise KeyError(char.name)
        origin_text = pages[char.name]
        new_text = origin_text

        # 更新后勤技能
        building_skill = get_building_skill(building_data, char_key, rts)
        num1 = new_text.find("==后勤技能==")
        num2 = new_text.find("==召唤物信息==")
        if num2 == -1:
            num2 = new_text.find("==精英化材料==")
        new_text = (
            new_text[:num1] + "==后勤技能==\n" + building_skill + "\n" + new_text[num2:]
        )

        # 更新属性
        phases_data = get_phases_data(
            char, char_key, uniequip_table, battle_equip_table, team_table
        )
        num1 = new_text.find("==属性==")
        num2 = new_text.find("==攻击范围==")
        new_text = new_text[:num1] + "==属性==\n" + phases_data + "\n" + new_text[num2:]

        # 更新模组
        equip_list = get_battle_equip(
            char,
            char_key,
            battle_equip_table,
            uniequip_table,
            item_table,
            rts,
        )
        num1 = new_text.find("==模组==")
        num2 = new_text.find("\n==相关道具==")
        if num1 == -1:
            num1 = num2
            new_text = new_text[:num1].rstrip() + "".join(equip_list) + new_text[num2:]
        else:
            equip_text = new_text[num1:num2]
            for equip in equip_list:
                result = re.search("===(.+?)===", equip)
                if not result:
                    continue
                if f"==={result.group(1)}===" not in equip_text:
                    equip_text += equip
            new_text = new_text[:num1] + equip_text + new_text[num2:]

        # 更新画师与干员cv:只替换 CharinfoV2 里 |画师= 到 |精英0介绍= 之间的参数
        num1 = new_text.find("\n|画师=")
        num2 = new_text.find("\n|精英0介绍=")
        drawer, drawer_params, complete = phase_drawers(skin_table, char_key)
        # 这里与建页不同:画师信息不完整时整段留空
        params = [("画师", drawer), *drawer_params] if complete else [("画师", "")]
        params += cv_params(charword_table, char_key)
        segment = "".join(f"\n|{key}={value}" for key, value in params)
        new_text = new_text[:num1] + segment + new_text[num2:]

        if new_text != origin_text:
            await wiki.edit(title=char.name, text=new_text, summary="update")
            logger.info(f"Updated: {char.name}.")
        else:
            logger.info(f"Same: {char.name}.")


@job
async def update_handbook(
    wiki: Wiki,
    character_table: params.CharacterTable,
    item_table: params.ItemTable,
    stories_table: params.HandbookInfoTable,
    medal_table: params.MedalTable,
    rts: params.RichText,
) -> None:
    pending: list[tuple[CharacterData, str, str]] = []
    for char_key, char in iter_operators(character_table):
        handbook_avg = get_handbook_avg(char, stories_table, char_key, medal_table)
        handbook_stage = get_handbook_stage(
            char, char_key, stories_table, item_table, rts
        )
        if handbook_avg != "" or handbook_stage != "":
            pending.append((char, handbook_avg, handbook_stage))

    # 一次性批量读取需要更新的干员页面
    pages = await wiki.read_many(char.name or "" for char, _, _ in pending)
    for char, handbook_avg, handbook_stage in pending:
        if char.name not in pages:
            raise KeyError(char.name)
        origin_text = pages[char.name]

        num1 = origin_text.find("/语音记录}}")
        num2 = origin_text.find("\n==干员模型==")
        num3 = origin_text.find("\n==干员异格任务==")
        if num3 > 0:
            num2 = min(num2, num3)
        new_text = (
            origin_text[:num1]
            + "/语音记录}}"
            + handbook_avg
            + handbook_stage
            + origin_text[num2:]
        )

        if new_text != origin_text:
            await wiki.edit(
                title=char.name,
                text=new_text,
                summary="更新干员密录&悖论模拟",
            )
            logger.info(f"Updated: {char.name}.")
        else:
            logger.info(f"Same: {char.name}.")
