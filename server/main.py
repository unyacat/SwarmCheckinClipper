from typing import List
import os

from fastapi import Depends, FastAPI, HTTPException, Cookie, status
from fastapi.responses import RedirectResponse
import uvicorn
import foursquare
from dotenv import load_dotenv
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
models.Base.metadata.create_all(bind=engine)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
cid = os.environ.get("CID")
cs = os.environ.get("CS")


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/auth")
def auth():
    redirect_uri = 'http://' + os.environ.get("DOMAIN") + '/callback'
    client = foursquare.Foursquare(client_id=cid, client_secret=cs, redirect_uri=redirect_uri)
    return RedirectResponse(client.oauth.auth_url())


@app.get("/callback")
async def callback(code: str = None):
    if not code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    redirect_uri = 'http://' + os.environ.get("DOMAIN") + '/callback'
    client = foursquare.Foursquare(client_id=cid, client_secret=cs, redirect_uri=redirect_uri)
    # access_token = client.oauth.get_token(request.args.get('code'))


@app.get("/api/load_checkins", response_model=schemas.LoadCheckin)
def load_checkins():
    crud.post_checkins()
    return crud.post_checkins()


from auth import create_tokens
@app.get("/token", response_model=schemas.Token)
async def login(code: str = None, db: Session = Depends(get_db)):
    """トークン発行"""
    # user = authenticate(form.username, form.password)
    return create_tokens(db=db, user_id=code)

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
    uvicorn.run(app, host="localhost", port=8000)