from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None


class Message(BaseModel):
    message: str


class NewPassword(BaseModel):
    token: str
    new_password: str
