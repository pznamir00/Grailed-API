from aenum import nonmember
from .base_entity import BaseEntity


class BaseCategory(BaseEntity):
    sizes = nonmember(None)
