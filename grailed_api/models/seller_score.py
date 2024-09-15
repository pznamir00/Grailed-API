from typing import List, Optional, TypedDict


class SellerScore(TypedDict):
    rating_average: Optional[float]
    rating_count: Optional[int]


class ExtendedSellerScore(SellerScore):
    sold_count: int
    tag_list: List[str]
