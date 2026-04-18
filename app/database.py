import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_HOST_PORT = os.getenv("POSTGRES_HOST_PORT")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_HOST_PORT}/{POSTGRES_DB}"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = _declarative.declarative_base()

