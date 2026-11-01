"""shop_client_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/shop_client_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class RecommendItemTagTips(IntEnum):
    """enum__Torappu_RecommendItemTagTips"""

    ONSALE = 0
    DEADLINE = 1
    NONE = 2


class ShopRouteTarget(IntEnum):
    """enum__Torappu_ShopRouteTarget"""

    RECOMMENDSHOP = 0
    CASHSHOP = 1
    GIFTPACKAGE = 2
    SKINSHOP = 3
    HQCSHOP = 4
    LQCSHOP = 5
    EXQCSHOP = 6
    SOCAILSHOP = 7
    FURNSHOP = 8
    REPSHOP = 9
    LMGTSSHOP = 10
    EPGSSHOP = 11
    CLASSICSHOP = 12
    NONE = 13


class ShopRecommendTemplateType(IntEnum):
    """enum__Torappu_ShopRecommendTemplateType"""

    DEFAULT = 0
    NORSKIN = 1
    RETURNSKIN = 2
    NORFURN = 3
    NORGIFT = 4


class ShopUnlockType(IntEnum):
    """enum__Torappu_ShopUnlockType"""

    ALWAYS_UNLOCK = 0
    SKIN_UNLOCK = 1
    FURN_UNLOCK = 2
    BOTH_SKIN_FURN = 3


class ShopCondTrigPackageType(IntEnum):
    """enum__Torappu_ShopCondTrigPackageType"""

    NONE = 0
    RETURN_PROGRESS = 1
    RETURN_ONCE = 2
    NEW_PROGRESS = 3
    CHOOSE_REGISTER_TIME = 4
    CHOOSE_NEWBIE = 5


class ShopGPTabType(IntEnum):
    """enum__Torappu_ShopGPTabType"""

    DEFAULT_ALL = 0
    MONTH_CARD = 1
    PERM = 2
    NEWBIE = 3
    RETURN = 4
    RECOMMOND = 5
    TIMELY = 6


class ShopRecommendData(GameDataModel):
    """clz_Torappu_ShopRecommendData"""

    img_id: str | None = None
    slot_index: int = 0
    cmd: str = "RECOMMENDSHOP"
    param_1: str | None = None
    param_2: str | None = None
    skin_id: str | None = None


class ShopRecommendGroup(GameDataModel):
    """clz_Torappu_ShopRecommendGroup"""

    recommend_group: list[int] | None = None
    data_list: list[ShopRecommendData] | None = None


class ShopKeeperWord(GameDataModel):
    """clz_Torappu_ShopKeeperWord"""

    id: str | None = None
    text: str | None = None


class ShopRecommendTemplateNormalGiftParam(GameDataModel):
    """clz_Torappu_ShopRecommendTemplateNormalGiftParam"""

    show_start_ts: int = 0
    show_end_ts: int = 0
    good_id: str | None = None
    gift_package_name: str | None = None
    price: int = 0
    logo_id: str | None = None
    color: str | None = None
    have_mark: bool = False
    avail_count: int = 0


class ShopRecommendTemplateNormalSkinParam(GameDataModel):
    """clz_Torappu_ShopRecommendTemplateNormalSkinParam"""

    show_start_ts: int = 0
    show_end_ts: int = 0
    skin_ids: list[str] | None = None
    skin_group_name: str | None = None
    brand_icon_id: str | None = None
    color_back: str | None = None
    color_text: str | None = None
    text: str | None = None


class ShopRecommendTemplateNormalFurnParam(GameDataModel):
    """clz_Torappu_ShopRecommendTemplateNormalFurnParam"""

    show_start_ts: int = 0
    show_end_ts: int = 0
    furn_pack_id: str | None = None
    is_new: bool = False
    is_pack_sell: bool = False
    count: int = 0
    color_back: str | None = None
    color_text: str | None = None
    act_id: str | None = None


class ShopRecommendTemplateReturnSkinParam(GameDataModel):
    """clz_Torappu_ShopRecommendTemplateReturnSkinParam"""

    show_start_ts: int = 0
    show_end_ts: int = 0


class ShopRecommendTemplateParam(GameDataModel):
    """clz_Torappu_ShopRecommendTemplateParam"""

    normal_gift_param: ShopRecommendTemplateNormalGiftParam | None = None
    normal_skin_param: ShopRecommendTemplateNormalSkinParam | None = None
    normal_furn_param: ShopRecommendTemplateNormalFurnParam | None = None
    return_skin_param: ShopRecommendTemplateReturnSkinParam | None = None


class ShopRecommendItem(GameDataModel):
    """clz_Torappu_ShopRecommendItem"""

    tag_id: str | None = None
    display_type: str | None = None
    tag_name: str | None = None
    item_tag: str = "ONSALE"
    order_num: int = 0
    start_datetime: int = 0
    end_datetime: int = 0
    group_list: list[ShopRecommendGroup] | None = None
    tag_word: ShopKeeperWord | None = None
    template_type: str = "DEFAULT"
    template_param: ShopRecommendTemplateParam | None = None


class ShopCreditUnlockItem(GameDataModel):
    """clz_Torappu_ShopCreditUnlockItem"""

    sort_id: int = 0
    unlock_num: int = 0
    char_id: str | None = None


class ShopCreditUnlockGroup(GameDataModel):
    """clz_Torappu_ShopCreditUnlockGroup"""

    id: str | None = None
    index: str | None = None
    start_date_time: int = 0
    char_dict: list[ShopCreditUnlockItem] | None = None


class ShopClientDataShopKeeperData(GameDataModel):
    """clz_Torappu_ShopClientData_ShopKeeperData"""

    welcome_words: list[ShopKeeperWord] | None = None
    click_words: list[ShopKeeperWord] | None = None


class ShopCarouselDataItem(GameDataModel):
    """clz_Torappu_ShopCarouselData_Item"""

    sprite_id: str | None = None
    start_time: int = 0
    end_time: int = 0
    cmd: str = "RECOMMENDSHOP"
    param_1: str | None = None
    skin_id: str | None = None
    furni_id: str | None = None


class ShopCarouselData(GameDataModel):
    """clz_Torappu_ShopCarouselData"""

    items: list[ShopCarouselDataItem] | None = None


class ChooseShopRelation(GameDataModel):
    """clz_Torappu_ChooseShopRelation"""

    good_id: str | None = None
    option_list: list[str] | None = None


class ShopClientGPData(GameDataModel):
    """clz_Torappu_ShopClientGPData"""

    good_id: str | None = None
    gift_package_id: str | None = None
    display_name: str | None = None
    cond_trig_package_type: str = "NONE"


class ShopGPTabDisplayData(GameDataModel):
    """clz_Torappu_ShopGPTabDisplayData"""

    tab_id: str | None = None
    tab_name: str | None = None
    tab_type: str = "DEFAULT_ALL"
    recom_display_num: int = 0
    tab_pic_id: str | None = None
    tab_pic_on_color: str | None = None
    tab_pic_off_color: str | None = None
    sort_id: int = 0
    tab_start_time: int = 0
    tab_end_time: int = 0
    marker_pic_id: str | None = None


class LMTGSShopSchedule(GameDataModel):
    """clz_Torappu_LMTGSShopSchedule"""

    gacha_pool_id: str | None = None
    lmtgs_id: str | None = Field(default=None, alias="LMTGSId")
    icon_color: str | None = None
    icon_back_color: str | None = None
    store_text_color: str | None = None
    start_time: int = 0
    end_time: int = 0


class LMTGSShopOverlaySchedule(GameDataModel):
    """clz_Torappu_LMTGSShopOverlaySchedule"""

    gacha_pool_id_1: str | None = None
    gacha_pool_id_2: str | None = None
    pic_id: str | None = None


class ShopClientData(GameDataModel):
    """clz_Torappu_ShopClientData"""

    recommend_list: list[ShopRecommendItem] | None = None
    credit_unlock_group: dict[str, ShopCreditUnlockGroup] | None = None
    shop_keeper_data: ShopClientDataShopKeeperData | None = None
    carousels: list[ShopCarouselData] | None = None
    choose_shop_relations: list[ChooseShopRelation] | None = None
    choose_option_to_good_dict: dict[str, str] | None = None
    shop_unlock_dict: dict[str, str] | None = None
    extra_qc_shop_rule: list[str] | None = Field(default=None, alias="extraQCShopRule")
    rep_qc_shop_rule: list[str] | None = Field(default=None, alias="repQCShopRule")
    shop_gp_data_dict: dict[str, ShopClientGPData] | None = Field(
        default=None, alias="shopGPDataDict"
    )
    tab_display_data: dict[str, ShopGPTabDisplayData] | None = None
    shop_monthly_sub_good_id: str | None = None
    ls: list[LMTGSShopSchedule] | None = None
    os: list[LMTGSShopOverlaySchedule] | None = None


# root_type clz_Torappu_ShopClientData
ShopClientTable = ShopClientData


ShopRecommendData.model_rebuild()
ShopRecommendGroup.model_rebuild()
ShopKeeperWord.model_rebuild()
ShopRecommendTemplateNormalGiftParam.model_rebuild()
ShopRecommendTemplateNormalSkinParam.model_rebuild()
ShopRecommendTemplateNormalFurnParam.model_rebuild()
ShopRecommendTemplateReturnSkinParam.model_rebuild()
ShopRecommendTemplateParam.model_rebuild()
ShopRecommendItem.model_rebuild()
ShopCreditUnlockItem.model_rebuild()
ShopCreditUnlockGroup.model_rebuild()
ShopClientDataShopKeeperData.model_rebuild()
ShopCarouselDataItem.model_rebuild()
ShopCarouselData.model_rebuild()
ChooseShopRelation.model_rebuild()
ShopClientGPData.model_rebuild()
ShopGPTabDisplayData.model_rebuild()
LMTGSShopSchedule.model_rebuild()
LMTGSShopOverlaySchedule.model_rebuild()
ShopClientData.model_rebuild()
