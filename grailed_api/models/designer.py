from typing import List, Optional, TypedDict


class Designer(TypedDict):
    id: int
    name: str


class ExtendedDesigner(Designer):
    departments: List[str]
    slug: str
    logo_url: Optional[str]
