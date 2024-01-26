from pydantic import BaseModel
# from .cat import Cat


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class BreedRead(BreedBase):
    cats: list["Cat"] | None = None
    pass


class Breed(BreedBase):
    id: int

    class Config:
        orm_mode = True
