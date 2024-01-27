from typing import Optional
from pydantic import BaseModel, Field

from data.cat_image.cat_image import CatImage
from data.breed.breed import Breed
from data.user.user import User


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
    images: list[CatImage]
    breed: Optional["Breed"] | None = None
    owner: Optional["User"] | None = None
    profile_image: Optional["CatImage"] | None
    pass


class CatList(CatBase):
    id: int
    breed: Optional["Breed"] | None = None
    owner: Optional["User"] | None = None
    profile_image: Optional["CatImage"]


class Cat(CatBase):
    id: int
    owner_id: int
    breed_id: int | None

    class Config:
        orm_mode = True
