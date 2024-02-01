from pydantic import BaseModel
# from .cat import Cat


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class UserRead(UserBase):
    pass


class UserList(UserBase):
    pass


class User(UserBase):
    id: int
    username: str
    is_active: bool
    roles: str

    class Config:
        orm_mode = True
