from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
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

    cats = relationship("Cat", back_populates="owner", cascade="all,delete")


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey("breeds.id", ondelete='CASCADE'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))

    breed = relationship("Breed", back_populates="cats")
    owner = relationship("User", back_populates="cats")
    images = relationship("CatImage",
                          back_populates="cat",
                          viewonly=True,
                          cascade="all",
                          primaryjoin="and_(Cat.id == CatImage.cat_id and CatImage.is_profile == False)"
                          )

    profile_image = relationship("CatImage",
                                 back_populates="cat",
                                 uselist=False,
                                 viewonly=True,
                                 cascade="all",
                                 primaryjoin="and_ (Cat.id == CatImage.cat_id, CatImage.is_profile == True)"
                                 )


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    cats = relationship("Cat", back_populates="breed")


class CatImage(Base):
    __tablename__ = "cat_images"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    cat_id = Column(Integer, ForeignKey("cats.id", ondelete='CASCADE'))
    is_profile = Column(Boolean, default=False)
    storage_file_id = Column(Integer, ForeignKey("storage_files.id", ondelete='CASCADE'))
    storage_file = relationship("StorageFile", back_populates="cat_image", cascade="all, delete")

    cat = relationship("Cat", back_populates="images")


class StorageFile(Base):
    __tablename__ = "storage_files"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)

    cat_image = relationship("CatImage", back_populates="storage_file", cascade="all")


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    expiration_date = Column(Date)
    is_revoked = Column(Boolean, default=False)

    user = relationship("User", back_populates="refresh_tokens")
