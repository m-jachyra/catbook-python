from typing import List
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from db_context.models import Cat
from data.base_service import BaseService
from data.models.cat import CatCreate, CatUpdate


class CatsService(BaseService[Cat, CatCreate, CatUpdate]):
    def create(self, db: Session, *, obj_in: CatCreate) -> Cat:
        obj_in_data = jsonable_encoder(obj_in)
        db_bj = self.model(**obj_in_data)
        db.add(db_bj)
        db.commit()
        db.refresh(db_bj)
        return db_bj

    def get(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Cat]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


cats_service = CatsService(Cat)
