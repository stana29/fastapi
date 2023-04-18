from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
with open('password.txt', mode="r") as f:
    password = f.readline()

DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/mydb2"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class Base(DeclarativeBase):
    pass
