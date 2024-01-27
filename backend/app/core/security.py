from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from passlib.context import CryptContext

from config import settings

context = CryptContext(schemes=["argon2"], deprecated='auto')

ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None ) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_password(password: str, hashed_password: str) -> bool:
    return context.verify(password, hashed_password)


def get_password_has(password: str) -> str:
    return context.hash(password)
