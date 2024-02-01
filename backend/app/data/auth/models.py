from typing import Union
from pydantic import BaseModel


# JWT token response
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: Union[int, None] = None


class NewPassword(BaseModel):
    token: str
    new_password: str
