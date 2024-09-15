from typing import Optional, TypedDict


class Photo(TypedDict):
    id: int
    url: str
    width: int
    height: int
    rotate: int
    created_at: str


class ExtendedPhoto(Photo):
    listing_id: int
    image: Optional[str]
    updated_at: str
    photoable_id: int
    photoable_type: str
    position: int
    image_url: str
