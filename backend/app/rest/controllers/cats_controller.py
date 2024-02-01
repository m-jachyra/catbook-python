from typing import Annotated, List
from fastapi import APIRouter, Depends, status, HTTPException, Path, UploadFile, Form, File
from sqlalchemy.orm import Session
from data.cat_image.cat_image_service import cat_images_service

from db_context.context import get_db
from data.cat.cat_service import cats_service
from data.cat.cat import CatCreate, CatUpdate, CatRead, CatList, Cat

from fastapi_pagination import paginate
from fastapi_pagination.links import Page


router = APIRouter()


@router.get("/", response_model=Page[CatList])
def get_list(db: Session = Depends(get_db)):
    cats = cats_service.get(db)

    return paginate(cats)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_cat(name: Annotated[str, Form()],
               description: Annotated[str, Form()],
               breed_id: Annotated[int, Form()],
               images: List[UploadFile] = File([]),
               db: Session = Depends(get_db)):
    try:
        cat_create = CatCreate(name=name, description=description, breed_id=breed_id, owner_id='1') #TODO Dodać owner id
        cat = cats_service.create(db, obj_in=cat_create)

        if images:
            for img in images:
                cat_images_service.create_cat_image(db, image=img, cat_id=cat.id)
        return cat
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{cat_id}", response_model=Cat)
def update_cat(cat_id: int,
               name: Annotated[str, Form()],
               description: Annotated[str, Form()],
               breed_id: Annotated[int, Form()],
               images: List[UploadFile] = File([]),
               db: Session = Depends(get_db)):
    try:
        cat_update = CatUpdate(name=name, description=description, breed_id=breed_id)
        cat = cats_service.update(db, cat_id, obj_in=cat_update)

        if images:
            for img in images:
                cat_images_service.create_cat_image(db, image=img, cat_id=cat.id)

        return cat
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{cat_id}")
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    try:
        cats_service.delete(db, cat_id)
        return status.HTTP_200_OK
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{cat_id}", response_model=CatRead)
def show(cat_id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    cat = cats_service.show(db, cat_id=cat_id)

    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cat not found")
        pass
    return cat
