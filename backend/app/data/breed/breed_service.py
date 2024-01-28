from typing import Type

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from starlette import status

from data.base_service import BaseService
from data.breed.breed import BreedCreate, BreedUpdate
from db_context.models import Breed


class BreedsService(BaseService[Breed, BreedCreate, BreedUpdate]):

    def create(self, db: Session, breed: BreedCreate) -> Breed:
        breed_data = jsonable_encoder(breed)
        breed_db = self.model(**breed_data)
        db.add(breed_db)
        db.commit()
        db.refresh(breed_db)
        return breed_db

    def get(self, db: Session, **kwargs) -> list[Type[Breed]]:
        return (
            db.query(self.model)
            .all()
        )

    def update(self, db: Session, breed_id: int, breed_update: BreedUpdate):
        try:
            try:
                breed_db = db.query(self.model).filter(self.model.id == breed_id).first()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Breed not found")

            for var, value in vars(breed_update).items():
                if value is not None:
                    setattr(breed_db, var, value)
            db.commit()
            db.refresh(breed_db)
            return breed_db
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Failed breed update')

    def delete(self, db: Session, breed_id: int):
        try:
            breed_db = db.query(self.model).filter(self.model.id == breed_id).first()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Breed not found")

        db.delete(breed_db)
        db.commit()


breeds_service = BreedsService(Breed)
