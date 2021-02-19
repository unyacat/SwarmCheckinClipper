from sqlalchemy import Column, Integer, String, Float, DateTime, func
from database import Base


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


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, index=True, primary_key=True)
    refresh_token = Column(String(512))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

