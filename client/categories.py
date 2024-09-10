from enum import Enum


class Categories(Enum):
    TOPS = "tops"
    BOTTOMS = "bottoms"
    OUTERWEAR = "outerwear"
    FOOTWEAR = "footwear"
    TAILORING = "tailoring"
    ACCESSORIES = "accessories"


class Tops(Enum):
    BUTTON_UPS = "button_ups"
    JERSEYS = "jerseys"
    LONG_SLEEVE_SHIRTS = "long_sleeve_shirts"
    POLOS = "polos"
    SHORT_SLEEVE_SHIRTS = "short_sleeve_shirts"
    SLEEVELESS = "sleeveless"
    SWEATERS_KNITWEAR = "sweaters_knitwear"
    SWEATSHIRTS = "sweatshirts_hoodies"


class Bottoms(Enum):
    CASUAL_PANTS = "casual_pants"
    CROPPED_PANTS = "cropped_pants"
    DENIM = "denim"
    JUMPSUITS = "jumpsuits"
    LEGGINGS = "leggings"
    SHORTS = "shorts"
    SWEATPANTS_JOGGERS = "sweatpants_joggers"
    SWIMWEAR = "swimwear"


class Outerwear(Enum):
    BOMBERS = "bombers"
    CLOAKS_CAPES = "cloaks_capes"
    DENIM_JACKETS = "denim_jackets"
    HEAVY_COATS = "heavy_coats"
    LEATHER_JACKETS = "leather_jackets"
    LIGHT_JACKETS = "light_jackets"
    PARKAS = "parkas"
    RAINCOATS = "raincoats"
    VESTS = "vests"


class Footwear(Enum):
    BOOTS = "boots"
    FORMAL_SHOES = "formal_shoes"
    HITOP_SNEAKERS = "hitop_sneakers"
    LEATHER = "leather"
    LOWTOP_SNEAKERS = "lowtop_sneakers"
    SANDALS = "sandals"
    SLIP_ONS = "slip_ons"


class Tailoring(Enum):
    BLAZERS = "blazers"
    FORMAL_SHIRTING = "formal_shirting"
    FORMAL_TROUSERS = "formal_trousers"
    SUITS = "suits"
    TUXEDOS = "tuxedos"
    VESTS = "vests"


class Accessories(Enum):
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


class Departments(Enum):
    MENSWEAR = "menswear"
    WOMENSWEAR = "womenswear"


class Conditions(Enum):
    IS_NEW = "is_new"
    IS_GENTLY_USED = "is_gently_used"
    IS_USED = "is_used"
    IS_WORN = "is_worn"
    IS_NOT_SPECIFIED = "is_not_specified"


class Markets(Enum):
    BASIC = "basic"
    GRAILED = "grailed"
    HYPE = "hype"
    SARTORIAL = "sartorial"


class Locations(Enum):
    AUSTRALIA_NZ = "Australia/NZ"
    UK = "United Kingdom"
    US = "United States"
    ASIA = "Asia"
    EUROPE = "Europe"
    CANADA = "Canada"
    OTHER = "Other"
