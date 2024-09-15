from typing import TypedDict


class ShippingField(TypedDict):
    amount: int
    enabled: bool


class Shipping(TypedDict):
    us: ShippingField
    ca: ShippingField
    uk: ShippingField
    eu: ShippingField
    asia: ShippingField
    au: ShippingField
    other: ShippingField
