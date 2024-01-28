from typing import Optional

from pydantic import BaseModel
from data.storage_file.storage_file import StorageFile


class CatImageBase(BaseModel):
    description: Optional[str] = None


class CatImageCreate(CatImageBase):
    cat_id: int
    storage_file_id: int
    pass


class CatImageUpdate(CatImageBase):
    pass


class CatImage(CatImageBase):
    id: int
    cat_id: int
    storage_file_id: int
    is_profile: bool
    storage_file: StorageFile

    class Config:
        orm_mode = True
