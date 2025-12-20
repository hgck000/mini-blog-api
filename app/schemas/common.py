from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: list[T]
    total: int
    skip: int
    limit: int
    q: str | None = None
