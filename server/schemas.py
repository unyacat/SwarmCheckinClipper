from typing import List, Optional
from pydantic import BaseModel, HttpUrl, PositiveInt


class Checkin(BaseModel):
    userId: int
    cId: str
    cCreatedAt: PositiveInt
    cShout: str = None
    vId: str
    vName: str
    vCategoryName: str
    vCategoryIconURL: HttpUrl
    vCategoryId: str
    vLat: float
    vLng: float


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    foursquare_at: str
    class Config:
        orm_mode = True


# class Req(BaseModel):

# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []
#
#     class Config:
#         orm_mode = True
