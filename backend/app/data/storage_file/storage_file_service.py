from fastapi import File, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from data.base_service import BaseService
from data.storage_file.storage_file import StorageFileBase, StorageFileCreate
from db_context.models import StorageFile


class StorageFileService(BaseService[StorageFileBase, StorageFileCreate, StorageFile]):

    def save_storage_file(self, db: Session, file: File) -> StorageFile:
        try:
            storage_file_create = StorageFileCreate(url=file.filename)
            storage_file_db = StorageFile(url=storage_file_create.url)
            db.add(storage_file_db)
            db.commit()
            db.refresh(storage_file_db)
            return storage_file_db

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


storage_files_service = StorageFileService(StorageFile)
