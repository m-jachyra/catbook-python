from pydantic import BaseModel
from .cat_image import CatImage

class CatBase(BaseModel):
    name: str
    description: str


class CatCreate(CatBase):
    pass


class CatUpdate(CatBase):
    pass


class Cat(CatBase):
    id: int
    owner_id: int
    breed_id: int
    images: list[CatImage] = []

    class Config:
        orm_mode = True
