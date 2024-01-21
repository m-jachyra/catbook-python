from sqlalchemy.orm import Session
from ..models.cat import Cat


def get_cat(db: Session, cat_id: int):
    return db.query(Cat).filter(Cat.id == cat_id).first()


def get_cats(db: Session, skip: int = 0, limit: int = 100):
    print("Lubie placki")
    return db.query(Cat).offset(skip).limit(limit).all()

