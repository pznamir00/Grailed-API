from aenum import nonmember


class BaseEntity:
    category_label = nonmember(None)

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = f"{cls.category_label.value}.{value}"  # type: ignore
        return obj
