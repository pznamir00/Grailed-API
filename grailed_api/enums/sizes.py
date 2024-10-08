from aenum import Enum, nonmember
from grailed_api.enums import CategoryLabels
from .base_size import BaseSize


class TopSizes(BaseSize, Enum):  # type: ignore
    XXS = "xxs"
    XS = "xs"
    S = "s"
    M = "m"
    L = "l"
    XL = "xl"
    XXL = "xxl"

    category_label = nonmember(CategoryLabels.TOPS)


class OuterwearSizes(BaseSize, Enum):  # type: ignore
    XXS = "xxs"
    XS = "xs"
    S = "s"
    M = "m"
    L = "l"
    XL = "xl"
    XXL = "xxl"

    category_label = nonmember(CategoryLabels.OUTERWEAR)


class BottomSizes(BaseSize, Enum):  # type: ignore
    _26 = "26"
    _27 = "27"
    _28 = "28"
    _29 = "29"
    _30 = "30"
    _31 = "31"
    _32 = "32"
    _33 = "33"
    _34 = "34"
    _35 = "35"
    _36 = "36"
    _37 = "37"
    _38 = "38"
    _39 = "39"
    _40 = "40"
    _41 = "41"
    _42 = "42"
    _43 = "43"
    _44 = "44"

    category_label = nonmember(CategoryLabels.BOTTOMS)


class FootwearSizes(BaseSize, Enum):  # type: ignore
    _5 = "5"
    _5_5 = "5.5"
    _6 = "6"
    _6_5 = "6.5"
    _7 = "7"
    _7_5 = "7.5"
    _8 = "8"
    _8_5 = "8.5"
    _9 = "9"
    _9_5 = "9.5"
    _10 = "10"
    _10_5 = "10.5"
    _11 = "11"
    _11_5 = "11.5"
    _12 = "12"
    _12_5 = "12.5"
    _13 = "13"
    _14 = "14"
    _15 = "15"

    category_label = nonmember(CategoryLabels.FOOTWEAR)


class TailoringSizes(BaseSize, Enum):  # type: ignore
    _34S = "34s"
    _34R = "34r"
    _36S = "36s"
    _36R = "36r"
    _38S = "38s"
    _38R = "38r"
    _38L = "38l"
    _40S = "40s"
    _40R = "40r"
    _40L = "40l"
    _42S = "42s"
    _42R = "42r"
    _42L = "42l"
    _44S = "44s"
    _44R = "44r"
    _44L = "44l"
    _46S = "46s"
    _46R = "46r"
    _46L = "46l"
    _48S = "48s"
    _48R = "48r"
    _48L = "48l"
    _50S = "50s"
    _50R = "50r"
    _50L = "50l"
    _52S = "52s"
    _52R = "52r"
    _52L = "52l"
    _54R = "54r"
    _54L = "54l"

    category_label = nonmember(CategoryLabels.TAILORING)


class AccessorySizes(BaseSize, Enum):  # type: ignore
    OS = "os"
    _26 = "26"
    _28 = "28"
    _30 = "30"
    _32 = "32"
    _34 = "34"
    _36 = "36"
    _38 = "38"
    _40 = "40"
    _42 = "42"
    _44 = "44"
    _46 = "46"

    category_label = nonmember(CategoryLabels.ACCESSORIES)
