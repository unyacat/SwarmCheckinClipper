from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

import models, schemas


def post_checkins(db: Session, item: schemas.Checkin):
    db_item = models.Checkin(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def create_user_item(db: Session, item: schemas.User):
    db_item = models.User(**item.dict())
    db.merge(db_item)
    db.commit()
    return db_item


def load_user_item(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user_checkin_item(db: Session, item: schemas.Checkin):
    db_item = models.Checkin(**item.dict())
    db.merge(db_item)
    db.commit()
    return db_item


def get_user_checkin_freq(db: Session, user_id: str):
    sql = '''SELECT DATE_FORMAT(FROM_UNIXTIME(TRUNCATE(checkins.cCreatedAt / 86400, 0) * 86400), '%Y-%m-%d') AS date,
                COUNT(*) AS count
                FROM checkins
                WHERE userId = {user_id} AND cCreatedAt BETWEEN UNIX_TIMESTAMP(DATE_SUB(curdate(), interval 365 DAY)) AND UNIX_TIMESTAMP(DATE_ADD(curdate(), interval 0 DAY))
                GROUP BY DATE'''.format(user_id=user_id)
    return db.execute(sql).fetchall()


def get_user_checkin_venue_rank(db: Session, user_id: str):
    sql = '''
            SELECT COUNT(*) AS count, vName FROM checkins WHERE userId = {user_id} GROUP BY vId ORDER BY count DESC LIMIT 3
          '''.format(user_id=user_id)
    return db.execute(sql).fetchall()


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()