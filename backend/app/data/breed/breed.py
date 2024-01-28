from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class BreedUpdate(BreedBase):
    pass


class BreedRead(BreedBase):
    id: int
    pass


class Breed(BreedBase):
    id: int

    class Config:
        orm_mode = True
