from pydantic import BaseModel
from .cat import Cat


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    is_active: bool
    cats: list[Cat] = []
    roles: str

    class Config:
        orm_mode = True
