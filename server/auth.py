import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
import foursquare
from sqlalchemy.orm import Session
from jose import jwt
from dotenv import load_dotenv

import crud
import models, schemas
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
random_key = os.environ.get("RANDOM_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_tokens(db: Session, user_id: int, at: str):
    """パスワード認証を行い、トークンを生成"""
    # ペイロード作成
    access_payload = {
        'token_type': 'access_token',
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'user_id': user_id,
    }
    refresh_payload = {
        'token_type': 'refresh_token',
        'exp': datetime.utcnow() + timedelta(days=90),
        'user_id': user_id,
    }

    # トークン作成（本来は'SECRET_KEY123'はもっと複雑にする）
    access_token = jwt.encode(access_payload, random_key, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, random_key, algorithm='HS256')

    # DBにリフレッシュトークンを保存
    # db.query(User).update({"refresh_token": refresh_token}).filter(User.id == user_id).values()
    # User.update(refresh_token=refresh_token).where(User.id == user_id).execute()
    user = schemas.User(id=user_id, foursquare_at=at)
    crud.create_user_item(db, user)


    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}


def read_foursquare_access_token(db: Session, token: str):
    payload = jwt.decode(token, 'SECRET_KEY123', algorithms=['HS256'])

    if payload['token_type'] != token_type:
        raise HTTPException(status_code=401, detail=f'トークンタイプ不一致')

    user = models.User.get_by_id(payload['user_id'])

    return user["foursquare_at"]

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """アクセストークンからログイン中のユーザーを取得"""
#     return get_current_user_from_token(token, 'access_token')
#
#
# async def get_current_user_with_refresh_token(token: str = Depends(oauth2_scheme)):
#     """リフレッシュトークンからログイン中のユーザーを取得"""
#     return get_current_user_from_token(token, 'refresh_token')