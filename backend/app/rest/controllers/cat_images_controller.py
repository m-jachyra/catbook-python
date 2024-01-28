from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import FileResponse

from core.config import settings
from data.cat_image.cat_image_service import cat_images_service
from db_context.context import get_db

router = APIRouter()



@router.get('/{image_name}')
def get_cat_image(image_name: str):
    return FileResponse(settings.IMAGES_DIR + image_name)
    pass


@router.post('/')
def add_cat_profile_image(cat_id: int, db: Session = Depends(get_db), file: UploadFile = File()):
    try:
        cat_images_service.create_profile_image(db, file, cat_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {'success': True}


@router.get('/profile_image/{cat_id}')
def get_cat_profile_image(cat_id: int, db: Session = Depends(get_db)):
    profile_image = cat_images_service.get_cat_profile_image(db, cat_id)
    try:
        return FileResponse(settings.IMAGES_DIR + profile_image.storage_file.url)
    except Exception as e:
        raise HTTPException(status_code=404)
    pass

