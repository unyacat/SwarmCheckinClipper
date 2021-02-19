from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

DATABASE = 'mysql+pymysql'
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
host = os.environ.get("DOMAIN")
port = 3306
db_name = "test_db"
option = "?charset=utf8"

SQLALCHEMY_DATABASE_URL = '{}://{}:{}@{}:{}/{}{}'.format(DATABASE, db_user, db_pass, host, port, db_name, option)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


