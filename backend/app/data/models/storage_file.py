from pydantic import BaseModel


class StorageFileBase(BaseModel):
    url: str


class StorageFileCreate(StorageFileBase):
    pass


class StorageFile(StorageFileBase):
    id: int

    class Config:
        orm_mode = True
