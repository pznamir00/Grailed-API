from aenum import Enum, nonmember
from .sizes import (
    AccessorySizes,
    BottomSizes,
    FootwearSizes,
    OuterwearSizes,
    TailoringSizes,
    TopSizes,
)
from .labels import CategoryLabels
from .base_category import BaseCategory


class Tops(BaseCategory, Enum):  # type: ignore
    BUTTON_UPS = "button_ups"
    JERSEYS = "jerseys"
    LONG_SLEEVE_SHIRTS = "long_sleeve_shirts"
    POLOS = "polos"
    SHORT_SLEEVE_SHIRTS = "short_sleeve_shirts"
    SLEEVELESS = "sleeveless"
    SWEATERS_KNITWEAR = "sweaters_knitwear"
    SWEATSHIRTS = "sweatshirts_hoodies"

    category_label = nonmember(CategoryLabels.TOPS)
    sizes = nonmember(TopSizes)


class Bottoms(BaseCategory, Enum):  # type: ignore
    CASUAL_PANTS = "casual_pants"
    CROPPED_PANTS = "cropped_pants"
    DENIM = "denim"
    JUMPSUITS = "jumpsuits"
    LEGGINGS = "leggings"
    SHORTS = "shorts"
    SWEATPANTS_JOGGERS = "sweatpants_joggers"
    SWIMWEAR = "swimwear"

    category_label = nonmember(CategoryLabels.BOTTOMS)
    sizes = nonmember(BottomSizes)


class Outerwear(BaseCategory, Enum):  # type: ignore
    BOMBERS = "bombers"
    CLOAKS_CAPES = "cloaks_capes"
    DENIM_JACKETS = "denim_jackets"
    HEAVY_COATS = "heavy_coats"
    LEATHER_JACKETS = "leather_jackets"
    LIGHT_JACKETS = "light_jackets"
    PARKAS = "parkas"
    RAINCOATS = "raincoats"
    VESTS = "vests"

    category_label = nonmember(CategoryLabels.OUTERWEAR)
    sizes = nonmember(OuterwearSizes)


class Footwear(BaseCategory, Enum):  # type: ignore
    BOOTS = "boots"
    FORMAL_SHOES = "formal_shoes"
    HITOP_SNEAKERS = "hitop_sneakers"
    LEATHER = "leather"
    LOWTOP_SNEAKERS = "lowtop_sneakers"
    SANDALS = "sandals"
    SLIP_ONS = "slip_ons"

    category_label = nonmember(CategoryLabels.FOOTWEAR)
    sizes = nonmember(FootwearSizes)


class Tailoring(BaseCategory, Enum):  # type: ignore
    BLAZERS = "blazers"
    FORMAL_SHIRTING = "formal_shirting"
    FORMAL_TROUSERS = "formal_trousers"
    SUITS = "suits"
    TUXEDOS = "tuxedos"
    VESTS = "vests"

    category_label = nonmember(CategoryLabels.TAILORING)
    sizes = nonmember(TailoringSizes)


class Accessories(BaseCategory, Enum):  # type: ignore
    BAGS_LUGGAGE = "bags_luggage"
    BELTS = "belts"
    GLASSES = "glasses"
    GLOVES_SCARVES = "gloves_scarves"
    HATS = "hats"
    JEWELRY_WATCHES = "jewelry_watches"
    MISC = "misc"
    PERIODICALS = "periodicals"
    SOCKS_UNDERWEAR = "socks_underwear"
    SUNGLASSES = "sunglasses"
    SUPREME = "supreme"
    TIES_POCKETSQUARES = "ties_pocketsquares"
    WALLETS = "wallets"

    category_label = nonmember(CategoryLabels.ACCESSORIES)
    sizes = nonmember(AccessorySizes)
