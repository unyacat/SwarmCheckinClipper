from typing import List
import os

from fastapi import Depends, FastAPI, HTTPException, Cookie, status, Response
from fastapi.responses import RedirectResponse
from jose.jwt import decode
from sqlalchemy.sql.base import SchemaEventTarget
from starlette.responses import JSONResponse

import uvicorn
import foursquare
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from auth import create_tokens, decode_jwt, read_foursquare_access_token
import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
cid = os.environ.get("CID")
cs = os.environ.get("CS")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="access_token")


@app.get("/api/auth")
def auth():
    redirect_uri = 'http://' + os.environ.get("DOMAIN") + '/callback'
    client = foursquare.Foursquare(
        client_id=cid, client_secret=cs, redirect_uri=redirect_uri)
    return RedirectResponse(client.oauth.auth_url())


@app.get("/api/token")
async def callback(code: str = None, db: Session = Depends(get_db)):
    if not code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    redirect_uri = 'http://' + os.environ.get("DOMAIN") + '/callback'
    client = foursquare.Foursquare(
        client_id=cid, client_secret=cs, redirect_uri=redirect_uri)
    access_token = client.oauth.get_token(code)
    client = foursquare.Foursquare(access_token=access_token)
    user = client.users()
    user_id = user["user"]["id"]
    token = create_tokens(db=db, user_id=user_id, at=access_token)
    return token


@app.get("/api/load_checkins")
async def load_checkins(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_id, f_at = read_foursquare_access_token(db=db, token=token)
    client = foursquare.Foursquare(access_token=f_at, lang='ja')
    offset = 0

    while True:
        checkins = client.users.checkins(
            USER_ID='self', params={"limit": 250, "offset": offset}
        )
        for checkin in checkins["checkins"]["items"]:
            # コメントなしチェックイン
            if not checkin.get("shout"):
                checkin["shout"] = None
            # 無カテゴリーチェックインは無視する
            if not len(checkin["venue"]["categories"]):
                continue
            item = schemas.Checkin(
                userId=user_id,
                cId=checkin["id"],
                cCreatedAt=checkin["createdAt"],
                cShout=checkin["shout"],
                vId=checkin["venue"]["id"],
                vName=checkin["venue"]["name"],
                vCategoryName=checkin["venue"]["categories"][0]["name"],
                vCategoryIconURL=checkin['venue']['categories'][0]['icon']['prefix'] +
                "bg_64" + checkin['venue']['categories'][0]['icon']['suffix'],
                vCategoryId=checkin["venue"]['categories'][0]["id"],
                vLat=checkin['venue']['location']['lat'],
                vLng=checkin['venue']['location']['lng']
            )
            crud.create_user_checkin_item(db=db, item=item)

        offset += len(checkins["checkins"]["items"])
        if (offset >= checkins["checkins"]["count"]) or (len(checkins["checkins"]["items"]) == 0):
            break

    return {"status": "done"}


@app.get("/api/checkin-freq")
async def get_user_checkin_freq(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_id = decode_jwt(token)
    items = crud.get_user_checkin_freq(db=db, user_id=user_id)
    return items



@app.get("/api/rank/venue")
async def get_user_checkin_venue_rank(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_id = decode_jwt(token)
    items = crud.get_user_checkin_venue_rank(db, user_id)
    return items
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
#


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
