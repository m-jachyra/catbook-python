import uuid
from fastapi import HTTPException, File
from sqlalchemy.orm import Session
from starlette import status
from core.config import settings
from data.base_service import BaseService
from data.cat_image.cat_image import CatImageCreate, CatImageUpdate
from data.storage_file.storage_file_service import storage_files_service
from db_context.models import CatImage


class CatImagesService(BaseService[CatImage, CatImageCreate, CatImageUpdate]):
    IMAGE_DIR = settings.IMAGES_DIR

    def create_profile_image(self, db: Session, image: File, cat_id: int):
        image.filename = f"{uuid.uuid4()}.jpg"
        self.save_image_file(image)

        storage_file = storage_files_service.save_storage_file(db, image)

        self.replace_and_create_image(db, storage_file, cat_id)

    def get_image(self, image_id: str) -> CatImage:
        pass

    def delete_image(self, image_id: str) -> None:
        pass

    def get_cat_profile_image(self, db: Session, cat_id: int) -> CatImage:
        try:
            return (db.query(self.model).filter(self.model.cat_id == cat_id)
                    .filter(self.model.is_profile == True)
                    .first())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        pass

    def save_image_file(self, image: File):
        try:
            with open(f"{self.IMAGE_DIR}{image.filename}", 'wb') as f:
                f.write(image.file.read())
                f.close()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed uploading image")

    def replace_and_create_image(self, db: Session, storage_file, cat_id):

        existing_profile_image = (
            db.query(self.model)
            .filter(self.model.cat_id == cat_id)
            .filter(self.model.is_profile == True).first())

        if existing_profile_image:
            try:
                db.delete(existing_profile_image)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed uploading image")

        cat_db = CatImage(cat_id=cat_id, storage_file_id=storage_file.id, is_profile=True)
        db.add(cat_db)
        db.commit()
        db.refresh(cat_db)



cat_images_service = CatImagesService(CatImage)
