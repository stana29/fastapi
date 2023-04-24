from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

db_user = config["DATABASE"]["User"]
db_password = config["DATABASE"]["Password"]
db_host = config["DATABASE"]["Host"]
db_port = config["DATABASE"]["Port"]
db_name = config["DATABASE"]["DBName"]

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


class Base(DeclarativeBase):
    pass
