from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException, Path
from sqlalchemy.orm import Session

from db_context.context import get_db
from data.cat.cat_service import cats_service

from data.cat.cat import CatCreate, CatUpdate, CatRead, CatList

from fastapi_pagination import paginate
from fastapi_pagination.links import Page
router = APIRouter()


@router.get("/", response_model=Page[CatList])
def get_list(db: Session = Depends(get_db)):
    cats = cats_service.get(db)

    return paginate(cats)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_cat(cat: CatCreate, db: Session = Depends(get_db)):
    try:
        cat = cats_service.create(db, obj_in=cat)
        return cat
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    pass


@router.put("/{cat_id}")
def update_cat(cat_id: int, cat: CatUpdate, db: Session = Depends(get_db)):
    try:
        cat = cats_service.update(db, cat_id, obj_in=cat)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    pass


@router.delete("/{cat_id}")
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    try:
        cats_service.delete(db, cat_id)
        return status.HTTP_200_OK
        pass
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    pass


@router.get("/{cat_id}", response_model=CatRead)
def show(cat_id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    cat = cats_service.show(db, cat_id=cat_id)

    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cat not found")
        pass
    return cat
