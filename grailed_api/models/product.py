from typing import List, Optional, TypedDict
from .user import User
from .designer import Designer
from .photo import ExtendedPhoto
from .shipping import Shipping
from .highlight_result import HighlightResult


class Trait(TypedDict):
    name: str
    value: str


class RankingInfo(TypedDict):
    nbTypos: int
    firstMatchedWord: int
    proximityDistance: int
    userScore: int
    geoDistance: int
    geoPrecision: int
    nbExactWords: int
    words: int
    filters: int


class Product(TypedDict):
    badges: List[str]
    bumped_at: str
    buynow: bool
    category_path_size: str
    category_path: str
    category_size: str
    category: str
    color: str
    condition: str
    cover_photo: ExtendedPhoto
    created_at_i: int
    created_at: str
    deleted: bool
    department: str
    description: str
    designer_count: int
    designer_names: str
    designers: List[Designer]
    dropped: bool
    followerno: int
    hashtags: List[str]
    heat_f: float
    id: int
    location: str
    makeoffer: bool
    marketplace: str
    price_drops: List[int]
    price_i: int
    price_updated_at_i: int
    price_updated_at: str
    price: int
    product_id: Optional[int]
    repost_id: Optional[int]
    size: str
    sku_id: Optional[int]
    sold_at: Optional[str]
    sold: bool
    strata: str
    title: str
    traits: List[Trait]
    user: User
    sold_price: int
    sold_price_includes_shipping: Optional[bool]
    sold_shipping_price: Optional[int]
    sold_at_i: int
    shipping: Shipping
    heat_recency: float
    objectID: str
    _highlightResult: HighlightResult
    _rankingInfo: RankingInfo
