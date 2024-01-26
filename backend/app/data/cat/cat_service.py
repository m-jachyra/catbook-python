from typing import Type

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from fastapi.encoders import jsonable_encoder
from db_context.models import Cat
from data.base_service import BaseService
from data.cat.cat import CatCreate, CatUpdate, CatRead


class CatsService(BaseService[Cat, CatCreate, CatUpdate]):
    def create(self, db: Session, *, obj_in: CatCreate) -> Cat:
        obj_in_data = jsonable_encoder(obj_in)
        db_bj = self.model(**obj_in_data)
        db.add(db_bj)
        db.commit()
        db.refresh(db_bj)
        return db_bj

    def get(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Type[Cat]]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, db: Session, cat_id: int, obj_in: CatUpdate):
        obj_in_data = jsonable_encoder(obj_in)
        cat = db.query(self.model).filter(self.model.id == cat_id).first()
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")

        for key, value in obj_in_data.items():
            setattr(cat, key, value)

        db.commit()
        db.refresh(cat)
        pass

    def delete(self, db: Session, cat_id: int):
        cat = db.query(self.model).filter(self.model.id == cat_id).first()

        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")

        db.delete(cat)
        db.commit()
        pass

    def show(self, db: Session, *, cat_id: int) -> CatRead:
        return (
            db.query(self.model)
            .options(joinedload(Cat.breed))
            .get(cat_id)
        )


cats_service = CatsService(Cat)
