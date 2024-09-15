from typing import List, Optional, TypedDict
from .seller_score import SellerScore, ExtendedSellerScore


class User(TypedDict):
    id: int
    username: str
    aggregate_feedback_count: int
    total_bought_and_sold: int
    avatar_url: Optional[str]
    seller_score: SellerScore
    trusted_seller: bool


class BuyerScore(TypedDict):
    purchase_count: int
    would_sell_to_again_count: int


class Seller(User):
    bio: str
    created_at: str
    height: Optional[int]
    weight: Optional[int]
    location: str
    location_abbreviation: str
    buyer_score: BuyerScore
    seller_score: ExtendedSellerScore
    seller_rating: ExtendedSellerScore
    listings_for_sale_count: int
    followed_listings: List[str]
    is_banned: bool
    is_deleted: bool
    is_confirmed: bool
    is_authed_seller: bool
    group: str
    seller_badges_revoked: bool
    power_seller_group: Optional[str]
    follower_count: int
    following_count: int
    is_blocked: bool
    is_followed: bool
    is_admin: bool
    is_verified: bool
    is_curator: bool
    is_quick_responder: bool
    is_speedy_shipper: bool
    is_trusted_seller: bool
    trust_score: str
    needs_to_connect_paypal_merchant_account: bool
    paypal_merchant_id: str
    vacation: Optional[str]
    account_preferences: Optional[str]
    country_code: str
