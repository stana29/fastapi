from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.schema import Column
from sqlalchemy import Integer, String

router = APIRouter(prefix="/sql2")

with open('password.txt', mode="r") as f:
    password = f.readline()

DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/mydb2"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class Base(DeclarativeBase):
    pass

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)
    def __repr__(self):
        return self.name
    
class CityInfo(BaseModel):
    name: str
    population: int


Base.metadata.create_all(engine)

@router.get("/test/")
def test():
    city = City(name="hoge", population=10000)
    session.add(city)
    session.commit()
    return


@router.get("/test2/")
def test2():
    city_a = session.query(City).get(1)
    city_a.name = "fuga"
    session.commit()
    return get_all_users()


@router.get("/all/")
def get_all_users():
    response = session.query(City).all()
    return response

@router.delete("/all/")
def delete_all():
    session.query(City).delete()
    session.commit()
    return {"message": "all users deleted"}


@router.delete("/{id}/")
def delete_user(id: int):
    user_a = session.query(City).get(id)
    session.delete(user_a)
    session.commit()
    return get_all_users()


@router.post("/add/")
def add_user(cityinfo: CityInfo):
    session.add(City(name=cityinfo.name, population=cityinfo.population))
    session.commit()
    return


@router.get("/{id}")
def get_user(id: int):
    return session.query(City).get(id)