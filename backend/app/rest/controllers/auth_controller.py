from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from data.user.users_service import users_service
from data.user.user import User, UserCreate
from data.breed.breed_service import breeds_service
from data.auth.models import Token
from db_context.context import get_db
from core.config import settings
from core.security import create_access_token, create_refresh_token, revoke_refresh_token
from rest.helpers import get_current_active_user
router = APIRouter()


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> Token:
    user = users_service.authenticate(db=db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not users_service.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    return Token(
        access_token=create_access_token(subject=user.id, expires_delta=access_token_expires),
        refresh_token=create_refresh_token(subject=user.id, expires_delta=refresh_token_expires)
    )


@router.post("/logout")
def logout(db: Session = Depends(get_db)):
    revoke_refresh_token(db=db, token=Depends(get_current_active_user))


@router.post("/register")
def register(*, user_in: UserCreate, db: Session = Depends(get_db)) -> Any:
    """
    Create new user.
    """
    user = users_service.get_by_email(db=db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crud.create_user(session=session, user_create=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user


# @router.put("/change-password")
# def change_password(breed_id: int, breed_update: BreedUpdate, db: Session = Depends(get_db)):
#     try:
#         auth_service.update(db=db, breed_id=breed_id, breed_update=breed_update)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Failed breed update')
#     return status.HTTP_200_OK


@router.get("/me", response_model=User)
def get_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user
