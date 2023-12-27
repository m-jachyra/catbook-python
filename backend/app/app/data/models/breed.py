from pydantic import BaseModel
from .cat import Cat


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class Breed(BreedBase):
    id: int
    cats: list[Cat] = []

    class Config:
        orm_mode = True
