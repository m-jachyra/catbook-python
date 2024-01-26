from typing import Optional
from pydantic import BaseModel, Field

from .cat_image import CatImage
from .breed import Breed
from .user import User


class CatBase(BaseModel):
    name: str = Field(description="The name of the cat", max_length=200, example="World destroyer")
    description: str | None = Field(default=None, description="The description of the cat", max_length=5000,
                                    example="My fluffy friend")


class CatCreate(CatBase):
    breed_id: int | None
    pass


class CatUpdate(CatBase):
    breed_id: int | None
    pass


class CatRead(CatBase):
    id: int
    images: set[CatImage] = set()
    breed: Optional["Breed"] | None = None
    owner: Optional["User"] | None = None
    pass


class Cat(CatBase):
    id: int
    owner_id: int
    breed_id: int | None

    class Config:
        orm_mode = True
