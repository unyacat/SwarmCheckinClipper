from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, text, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from database import Base


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")


class Checkin(Base):
    __tablename__ = "checkins"
    userId = Column(Integer, index=True)
    cId = Column(String(128), primary_key=True)
    cCreatedAt = Column(Integer)
    # cPhotos = Column(String())
    cShout = Column(String(512))
    vId = Column(String(256))
    vName = Column(String(256))
    vCategoryName = Column(String(256))
    vCategoryIconURL = Column(String(256))
    vCategoryId = Column(String(256))
    vLat = Column(Float)
    vLng = Column(Float)


class Session(Base):
    __tablename__ = "sessions"
    userId = Column(Integer, index=True, primary_key=True)
    access_token = Column(String(256))
    cookie = Column(String(256))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
