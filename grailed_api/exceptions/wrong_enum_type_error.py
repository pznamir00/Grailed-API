from typing import Any, Type


class WrongCategoryTypeError(Exception):
    def __init__(self, type: Type):
        super().__init__(
            f"""All categories must be fields of enums, not {type}. \
Make sure you provided valid enum fields (e.g. Tops.BUTTON_UPS, not just Tops)"""
        )


class WrongSizeTypeError(Exception):
    def __init__(self, type: Type):
        super().__init__(
            f"""All sizes must be fields of enums, not {type}. \
Make sure you provided valid enum fields (e.g. Tops.sizes.L, not just Tops.sizes)"""
        )
