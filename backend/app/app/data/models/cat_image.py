from pydantic import BaseModel


class CatImageBase(BaseModel):
    description: str


class CatImageCreate(CatImageBase):
    pass


class CatImage(CatImageBase):
    id: int
    cat_id: int
    storage_file_id: int

    class Config:
        orm_mode = True
