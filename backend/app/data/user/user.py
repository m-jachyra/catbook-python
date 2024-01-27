from pydantic import BaseModel
# from .cat import Cat


class UserBase(BaseModel):
    email: str


class UserOut(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    cats: list["Cat"] = []
    pass


class User(UserBase):
    id: int
    username: str
    is_active: bool
    roles: str

    class Config:
        orm_mode = True
