from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from data.breed.breed import BreedCreate, BreedRead, BreedUpdate
from data.breed.breed_service import breeds_service
from db_context.context import get_db

router = APIRouter()


@router.get("/", response_model=List[BreedRead])
def get_list(db: Session = Depends(get_db)):
    breeds = breeds_service.get(db)

    return breeds
    pass


@router.post("/")
def create_breeds(breed: BreedCreate, db: Session = Depends(get_db)):
    try:
        breeds_service.create(db=db, breed=breed)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Breeds could not be created')
    return status.HTTP_201_CREATED
    pass


@router.put("/")
def update_breeds(breed_id: int, breed_update: BreedUpdate, db: Session = Depends(get_db)):
    try:
        breeds_service.update(db=db, breed_update=breed_update, breed_id=breed_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Failed breed update')
    return status.HTTP_200_OK
    pass


@router.delete("/")
def delete_breeds(breed_id: int, db: Session = Depends(get_db)):
    try:
        breeds_service.delete(db=db, breed_id=breed_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail='Breed can not be deleted')
    return status.HTTP_200_OK
    pass