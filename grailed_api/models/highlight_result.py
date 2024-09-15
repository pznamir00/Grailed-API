from typing import Any, List, TypedDict


class HighlightResultField(TypedDict):
    value: str
    matchLevel: str
    matchedWords: List[Any]


class HighlightResultDesigner(TypedDict):
    name: HighlightResultField


class HighlightResultSellerScore(TypedDict):
    rating_average: HighlightResultField
    rating_count: HighlightResultField


class HighlightResultUser(TypedDict):
    id: HighlightResultField
    username: HighlightResultField
    aggregate_feedback_count: HighlightResultField
    total_bought_and_sold: HighlightResultField
    avatar_url: HighlightResultField
    seller_score: HighlightResultSellerScore


class HighlightResult(TypedDict):
    category: HighlightResultField
    color: HighlightResultField
    designers: List[HighlightResultDesigner]
    hashtags: List[HighlightResultField]
    location: HighlightResultField
    size: HighlightResultField
    title: HighlightResultField
    user: HighlightResultUser
