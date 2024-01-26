from typing import List, Annotated

from fastapi import APIRouter, Depends, status, Response, HTTPException, Path
from sqlalchemy.orm import Session

from db_context.context import get_db
from data.services.cats_service import cats_service

from data.models.cat import CatCreate, CatUpdate, Cat, CatRead

router = APIRouter()


@router.get("/", response_model=List[Cat])
def get_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cats = cats_service.get(db, skip=skip, limit=limit)
    return cats


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
