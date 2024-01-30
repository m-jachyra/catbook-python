import hashlib
import os
from datetime import datetime

from fastapi import HTTPException, File
from sqlalchemy.orm import Session, joinedload
from starlette import status
from core.config import settings
from data.base_service import BaseService
from data.cat_image.cat_image import CatImageCreate, CatImageUpdate
from data.storage_file.storage_file_service import storage_files_service
from db_context.models import CatImage


class CatImagesService(BaseService[CatImage, CatImageCreate, CatImageUpdate]):

    def create_profile_image(self, db: Session, image: File, cat_id: int):
        hash_image_name(image)
        save_image_file(image)

        storage_file = storage_files_service.save_storage_file(db, image)
        self.replace_and_create_image(db, storage_file, cat_id)

    def create_cat_image(self, db: Session, image: File, cat_id: int):
        hash_image_name(image)
        save_image_file(image)

        storage_file = storage_files_service.save_storage_file(db, image)
        self.create_image(db, storage_file_id=storage_file.id, cat_id=cat_id, is_profile=False)

    def get_image(self, image_id: str) -> CatImage:
        pass

    def delete_image(self, image_id: str) -> None:
        pass

    def create_image(self, db: Session, cat_id: int, storage_file_id: int, is_profile: bool = False):

        cat_db = CatImage(cat_id=cat_id, storage_file_id=storage_file_id, is_profile=is_profile)
        db.add(cat_db)
        db.commit()
        db.refresh(cat_db)

    def get_cat_profile_image(self, db: Session, cat_id: int) -> CatImage:
        try:
            return (db.query(self.model).filter(self.model.cat_id == cat_id)
                    .filter(self.model.is_profile == True)
                    .options(joinedload(CatImage.storage_file))
                    .first())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        pass

    def replace_and_create_image(self, db: Session, storage_file, cat_id):

        existing_profile_image = self.get_cat_profile_image(db, cat_id=cat_id)

        if existing_profile_image:
            try:
                db.delete(existing_profile_image)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed uploading image")

        self.create_image(db, storage_file_id=storage_file.id, cat_id=cat_id, is_profile=True)


def hash_image_name(image):
    filename, file_extension = os.path.splitext(image.filename)

    if file_extension not in {'.jpg', '.jpeg', '.png'}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")

    current_date_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    image.filename = f"{hashlib.sha256(filename.encode() + current_date_time.encode()).hexdigest()}{file_extension}"


def save_image_file(image: File):
    try:
        with open(f"{settings.IMAGES_DIR}{image.filename}", 'wb') as f:
            f.write(image.file.read())
            f.close()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed uploading image")


cat_images_service = CatImagesService(CatImage)
