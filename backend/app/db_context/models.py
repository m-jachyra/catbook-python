from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_context.context import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    roles = Column(String)

    cats = relationship("Cat", back_populates="owner")


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey("breeds.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    breed = relationship("Breed", back_populates="cats")
    owner = relationship("User", back_populates="cats")


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    cats = relationship("Cat", back_populates="breed")


class CatImage(Base):
    __tablename__ = "cat_images"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    cat_id = Column(Integer, ForeignKey("cats.id"))
    storage_file_id = Column(Integer, ForeignKey("storage_files.id"))


class StorageFile(Base):
    __tablename__ = "storage_files"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
