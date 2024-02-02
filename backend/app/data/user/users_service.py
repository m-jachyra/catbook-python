from typing import Any, Dict, Optional, Union

from db_context.context import Session
from core.security import get_password_hash, verify_password
from data.base_service import BaseService
from db_context.models import User
from data.user.user import UserCreate, UserUpdate


class UsersService(BaseService[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            password_hash=get_password_hash(obj_in.password),
            username=obj_in.username
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if update_data["password"]:
            password_hash = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = password_hash
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None

        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_admin(self, user: User) -> bool:
        return user.roles == 'admin'

    def is_moderator(self, user: User) -> bool:
        return user.roles == 'moderator'


users_service = UsersService(User)
