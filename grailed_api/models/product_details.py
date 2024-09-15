from typing import TypedDict, List, Optional
from .user import Seller
from .designer import ExtendedDesigner
from .photo import Photo
from .shipping import Shipping


class Measurement(TypedDict):
    inches: float
    measurement_type_id: int
    department_mapping_id: int


class ProductDetails(TypedDict):
    id: int
    title: str
    true_created_at: str
    created_at: str
    price_updated_at: str
    sold: bool
    sold_at: Optional[str]
    sold_price: int
    sold_shipping_price: Optional[int]
    sold_price_includes_shipping: Optional[bool]
    sold_with_label: Optional[bool]
    buyer_id: Optional[int]
    price: int
    description: str
    size: str
    exact_size: Optional[str]
    pretty_size: str
    category: str
    subcategory: str
    category_path: str
    price_drops: List[int]
    dropped: bool
    pretty_path: str
    followed: Optional[bool]
    follower_count: int
    photos: List[Photo]
    designer: ExtendedDesigner
    designer_names: str
    designers: List[ExtendedDesigner]
    seller: Seller
    strata: str
    buy_now: bool
    make_offer: bool
    deleted: bool
    deleted_via_refund: bool
    currency: str
    repost_id: Optional[int]
    hidden_from_algolia: bool
    hidden: bool
    published: bool
    condition: str
    traits: List[dict]
    payment_status: Optional[str]
    purchased_via: Optional[str]
    payment_destination: Optional[str]
    seller_rating: Optional[str]
    shipping: Shipping
    badges: List[str]
    needs_tracking: bool
    needs_feedback: bool
    withheld_at: Optional[str]
    product_id: Optional[int]
    sku_id: Optional[str]
    minimum_price: Optional[int]
    was_digitally_authenticated: bool
    reposts: Optional[int]
    hashtags: List[str]
    measurements: List[Measurement]
    last_relist_path: Optional[str]
    shipping_label: Optional[str]
    department: str
    external_seller_reference: Optional[str]
    return_address_country_code: str
    in_saved_list: bool
