"""charword_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/charword_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class CharWordVoiceType(IntEnum):
    """enum__Torappu_CharWordVoiceType"""

    ONLY_TEXT = 0
    HAVE_CV = 1
    ENUM = 2


class DataUnlockType(IntEnum):
    """enum__Torappu_DataUnlockType"""

    DIRECT = 0
    AWAKE = 1
    FAVOR = 2
    STAGE = 3
    ITEM = 4
    NEVER = 5
    PATCH = 6
    NONE = 7


class CharWordShowType(IntEnum):
    """enum__Torappu_CharWordShowType"""

    HOME_SHOW = 0
    HOME_PLACE = 1
    HOME_WAIT = 2
    GACHA = 3
    EVOLVE_ONE = 4
    EVOLVE_TWO = 5
    FOUR_STAR = 6
    THREE_STAR = 7
    TWO_STAR = 8
    LOSE = 9
    LEVEL_UP = 10
    SQUAD = 11
    SQUAD_FIRST = 12
    BATTLE_START = 13
    BATTLE_FACE_ENEMY = 14
    BATTLE_SELECT = 15
    BATTLE_PLACE = 16
    BATTLE_SKILL_1 = 17
    BATTLE_SKILL_2 = 18
    BATTLE_SKILL_3 = 19
    BATTLE_SKILL_4 = 20
    BUILDING_PLACE = 21
    BUILDING_DRAGGING = 22
    BUILDING_FAVOR_BUBBLE = 23
    BUILDING_TOUCHING = 24
    LOADING_PANEL = 25
    BIRTHDAY = 26
    NEW_YEAR = 27
    VALENT_DAY = 28
    DRAGON_BOAT_FESTIVAL = 29
    HALLOWEEN_DAY = 30
    CHRISMATS_DAY = 31
    GREETING = 32
    ANNIVERSARY = 33
    UNUSED = 34
    AUTOCHESS_GAME_START = 35
    AUTOCHESS_REST_NO_HP_LOSS = 36
    AUTOCHESS_REST_HP_LOSS = 37
    AUTOCHESS_REST_BOSS = 38
    AUTOCHESS_REST_HIDDEN_BOSS = 39
    AUTOCHESS_SAME_OPERATOR = 40
    AUTOCHESS_BUY_OPERATOR_LOW = 41
    AUTOCHESS_BUY_OPERATOR_HIGH = 42
    AUTOCHESS_SHOP_UPGRADE = 43
    AUTOCHESS_COUNTDOWN = 44
    AUTOCHESS_MERGE_TRIPLE = 45
    AUTOCHESS_ALLIANCE_LEVEL = 46
    AUTOCHESS_FREEZE = 47
    E_ALL = 48


class VoiceLangType(IntEnum):
    """enum__Torappu_VoiceLangType"""

    NONE = 0
    JP = 1
    CN_MANDARIN = 2
    EN = 3
    KR = 4
    CN_TOPOLECT = 5
    LINKAGE = 6
    ITA = 7
    GER = 8
    RUS = 9
    FRE = 10
    SPA = 11


class VoiceLangGroupType(IntEnum):
    """enum__Torappu_VoiceLangGroupType"""

    NONE = 0
    CN_MANDARIN = 1
    JP = 2
    EN = 3
    KR = 4
    CUSTOM = 5
    LINKAGE = 6


class FestivalVoiceTimeType(IntEnum):
    """enum__Torappu_FestivalVoiceTimeType"""

    NONE = 0
    FESTIVAL = 1
    BIRTHDAY = 2


class CharWordUnlockParam(GameDataModel):
    """clz_Torappu_CharWordUnlockParam"""

    value_str: str | None = None
    value_int: int = 0


class CharWordData(GameDataModel):
    """clz_Torappu_CharWordData"""

    char_word_id: str | None = None
    word_key: str | None = None
    char_id: str | None = None
    voice_id: str | None = None
    voice_text: str | None = None
    voice_title: str | None = None
    voice_index: int = 0
    voice_type: str = "ONLY_TEXT"
    unlock_type: str = "DIRECT"
    unlock_param: list[CharWordUnlockParam] | None = None
    lock_description: str | None = None
    place_type: str = "HOME_SHOW"
    voice_asset: str | None = None


class CharExtraWordData(GameDataModel):
    """clz_Torappu_CharExtraWordData"""

    word_key: str | None = None
    char_id: str | None = None
    voice_id: str | None = None
    voice_text: str | None = None


class VoiceLangInfoData(GameDataModel):
    """clz_Torappu_VoiceLangInfoData"""

    wordkey: str | None = None
    voice_lang_type: str = "NONE"
    cv_name: list[str] | None = None
    voice_path: str | None = None


class VoiceLangData(GameDataModel):
    """clz_Torappu_VoiceLangData"""

    wordkeys: list[str] | None = None
    char_id: str | None = None
    dict_: dict[str, VoiceLangInfoData] | None = Field(default=None, alias="dict")


class VoiceLangTypeData(GameDataModel):
    """clz_Torappu_VoiceLangTypeData"""

    name: str | None = None
    group_type: str = "NONE"


class VoiceLangGroupData(GameDataModel):
    """clz_Torappu_VoiceLangGroupData"""

    name: str | None = None
    members: list[str] | None = None


class NewVoiceTimeData(GameDataModel):
    """clz_Torappu_NewVoiceTimeData"""

    timestamp: int = 0
    char_set: list[str] | None = None


class FestivalTimeInterval(GameDataModel):
    """clz_Torappu_FestivalTimeInterval"""

    start_ts: int = 0
    end_ts: int = 0


class FestivalTimeData(GameDataModel):
    """clz_Torappu_FestivalTimeData"""

    time_type: str = "NONE"
    interval: FestivalTimeInterval | None = None


class FestivalVoiceData(GameDataModel):
    """clz_Torappu_FestivalVoiceData"""

    show_type: str = "HOME_SHOW"
    time_data: list[FestivalTimeData] | None = None


class FestivalVoiceWeightData(GameDataModel):
    """clz_Torappu_FestivalVoiceWeightData"""

    show_type: str = "HOME_SHOW"
    weight: float = 0.0
    priority: int = 0


class ExtraVoiceConfigData(GameDataModel):
    """clz_Torappu_ExtraVoiceConfigData"""

    voice_id: str | None = None
    valid_voice_lang: list[str] | None = None


class CharWordTable(GameDataModel):
    """clz_Torappu_CharWordTable"""

    char_words: dict[str, CharWordData] | None = None
    char_extra_words: dict[str, CharExtraWordData] | None = None
    voice_lang_dict: dict[str, VoiceLangData] | None = None
    default_lang_type: str = "NONE"
    new_tag_list: list[str] | None = None
    voice_lang_type_dict: dict[str, VoiceLangTypeData] | None = None
    voice_lang_group_type_dict: dict[str, VoiceLangGroupData] | None = None
    char_default_type_dict: dict[str, str] | None = None
    start_time_with_type_dict: dict[str, list[NewVoiceTimeData]] | None = None
    display_group_type_list: list[str] | None = None
    display_type_list: list[str] | None = None
    play_voice_range: str = "HOME_SHOW"
    fes_voice_data: dict[str, FestivalVoiceData] | None = None
    fes_voice_weight: dict[str, FestivalVoiceWeightData] | None = None
    extra_voice_config_data: dict[str, ExtraVoiceConfigData] | None = None


# root_type clz_Torappu_CharWordTable
CharwordTable = CharWordTable


CharWordUnlockParam.model_rebuild()
CharWordData.model_rebuild()
CharExtraWordData.model_rebuild()
VoiceLangInfoData.model_rebuild()
VoiceLangData.model_rebuild()
VoiceLangTypeData.model_rebuild()
VoiceLangGroupData.model_rebuild()
NewVoiceTimeData.model_rebuild()
FestivalTimeInterval.model_rebuild()
FestivalTimeData.model_rebuild()
FestivalVoiceData.model_rebuild()
FestivalVoiceWeightData.model_rebuild()
ExtraVoiceConfigData.model_rebuild()
CharWordTable.model_rebuild()
