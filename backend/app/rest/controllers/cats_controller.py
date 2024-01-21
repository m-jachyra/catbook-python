from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db_context.context import get_db
from data.services import cats_service

router = APIRouter()


@router.get('/')
def get_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cats = cats_service.get_cats(db, skip, limit)
    return cats
