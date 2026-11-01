"""skin_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/skin_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class SkinVoiceType(IntEnum):
    """enum__Torappu_SkinVoiceType"""

    NONE = 0
    ILLUST = 1
    ALL = 2


class CharSkinDataTokenSkinInfo(GameDataModel):
    """clz_Torappu_CharSkinData_TokenSkinInfo"""

    token_id: str | None = None
    token_skin_id: str | None = None


class CharSkinDataBattleSkin(GameDataModel):
    """clz_Torappu_CharSkinData_BattleSkin"""

    overwrite_prefab: bool = False
    skin_or_prefab_id: str | None = None


class CharSkinDataDisplaySkin(GameDataModel):
    """clz_Torappu_CharSkinData_DisplaySkin"""

    skin_name: str | None = None
    color_list: list[str] | None = None
    title_list: list[str] | None = None
    model_name: str | None = None
    drawer_list: list[str] | None = None
    designer_list: list[str] | None = None
    skin_group_id: str | None = None
    skin_group_name: str | None = None
    skin_group_sort_index: int = 0
    content: str | None = None
    dialog: str | None = None
    usage: str | None = None
    description: str | None = None
    obtain_approach: str | None = None
    sort_id: int = 0
    display_tag_id: str | None = None
    get_time: int = 0
    on_year: int = 0
    on_period: int = 0


class CharSkinData(GameDataModel):
    """clz_Torappu_CharSkinData"""

    skin_id: str | None = None
    char_id: str | None = None
    token_skin_map: list[CharSkinDataTokenSkinInfo] | None = None
    illust_id: str | None = None
    sp_illust_id: str | None = None
    dyn_illust_id: str | None = None
    sp_dyn_illust_id: str | None = None
    avatar_id: str | None = None
    sp_avatar_id: str | None = None
    portrait_id: str | None = None
    sp_portrait_id: str | None = None
    dyn_portrait_id: str | None = None
    dyn_entrance_id: str | None = None
    building_id: str | None = None
    battle_skin: CharSkinDataBattleSkin | None = None
    is_buy_skin: bool = False
    tmpl_id: str | None = None
    voice_id: str | None = None
    voice_type: str = "NONE"
    display_skin: CharSkinDataDisplaySkin | None = None


class CharSkinGroupInfo(GameDataModel):
    """clz_Torappu_CharSkinGroupInfo"""

    skin_group_id: str | None = None
    publish_time: int = 0


class CharSkinKvImgInfo(GameDataModel):
    """clz_Torappu_CharSkinKvImgInfo"""

    kv_img_id: str | None = None
    linked_skin_group_id: str | None = None


class CharSkinBrandInfo(GameDataModel):
    """clz_Torappu_CharSkinBrandInfo"""

    brand_id: str | None = None
    group_list: list[CharSkinGroupInfo] | None = None
    kv_img_id_list: list[CharSkinKvImgInfo] | None = None
    brand_name: str | None = None
    brand_capital_name: str | None = None
    description: str | None = None
    publish_time: int = 0
    sort_id: int = 0


class SpecialSkinInfo(GameDataModel):
    """clz_Torappu_SpecialSkinInfo"""

    skin_id: str | None = None
    start_time: int = 0
    end_time: int = 0


class SpDynIllustInfo(GameDataModel):
    """clz_Torappu_SpDynIllustInfo"""

    skin_id: str | None = None
    sp_dyn_illust_id: str | None = None
    sp_dyn_illust_skin_tag: str | None = None
    sp_illust_id: str | None = None
    sp_portrait_id: str | None = None
    sp_avatar_id: str | None = None
    sp_dyn_entrance_id: str | None = None


class SkinTable(GameDataModel):
    """clz_Torappu_SkinTable"""

    char_skins: dict[str, CharSkinData] | None = None
    buildin_evolve_map: dict[str, dict[int, str]] | None = None
    buildin_patch_map: dict[str, dict[str, str]] | None = None
    brand_list: dict[str, CharSkinBrandInfo] | None = None
    special_skin_info_list: list[SpecialSkinInfo] | None = None
    sp_dyn_skins: dict[str, SpDynIllustInfo] | None = None
    sp_dyn_illust_skin_tags_map: dict[str, str] | None = None


# root_type clz_Torappu_SkinTable


CharSkinDataTokenSkinInfo.model_rebuild()
CharSkinDataBattleSkin.model_rebuild()
CharSkinDataDisplaySkin.model_rebuild()
CharSkinData.model_rebuild()
CharSkinGroupInfo.model_rebuild()
CharSkinKvImgInfo.model_rebuild()
CharSkinBrandInfo.model_rebuild()
SpecialSkinInfo.model_rebuild()
SpDynIllustInfo.model_rebuild()
SkinTable.model_rebuild()
