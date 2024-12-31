from pydantic import BaseModel
from typing import List, Optional


class BookPost(BaseModel):
    name: str
    author: List[str]
    country: str
    language: List[str]
    genre: List[str]
    year_published: int
    publisher: str
    price: float


class BookPut(BaseModel):
    name: Optional[str] = None
    author: Optional[List[str]] = None
    country: Optional[str] = None
    language: Optional[List[str]] = None
    genre: Optional[List[str]] = None
    year_published: Optional[int] = None
    publisher: Optional[str] = None
    price: Optional[float] = None
