from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from sql_database import session
from sql_models import City, Person
from schemas import CityInfo
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

router = APIRouter(prefix="/sql2/city", tags=["city"])


@router.get("/test/")
def test():
    city = City(name="hoge", population=10000)
    session.add(city)
    session.commit()
    return


@router.get("/test2/")
def test2():
    filtered = session.query(City).filter(City.id == 5)
    if filtered:
        filtered.first().name = "fuga"
        session.commit()
    return get_all_cities_json()


@router.get("/test3/")
def test3():
    person = Person(name="taro")
    print(person.city)
    city = City(name="a", population=155)
    print(city.persons)
    city.persons.append(person)
    session.add(person)
    session.commit()
    print(city.id, city.population, city.name)
    print(person.id, person.city_id, person.city.name, person.name)
    person.name = "aiueo"
    print(person in session.dirty)
    session.flush()
    print(person in session.dirty)
    pid = person.id
    person2 = session.execute(select(Person.name).where(Person.id == pid)).scalar_one()
    print(person2)
    return


@router.get("/test4")
def test4():
    stmt = select(Person.id).join_from(City, Person).where(City.id < 20)
    print(stmt)
    print(session.execute(stmt).fetchall())
    return


@router.get("/all/")
def get_all_cities_json():
    response = session.query(City).order_by(City.id).all()
    return response


@router.delete("/all/")
def delete_all():
    session.query(City).delete()
    session.commit()
    return {"message": "all persons deleted"}


@router.delete("/{id}/")
def delete_city(id: int):
    user_a = session.query(City).get(id)
    if user_a:
        session.delete(user_a)
        session.commit()
    return


@router.post("/add/")
def add_city(cityinfo: CityInfo):
    session.add(City(name=cityinfo.name, population=cityinfo.population))
    session.commit()
    return


env = Environment(loader=FileSystemLoader("./", encoding="utf8"))
tmpl = env.get_template("city_list.html")


@router.get("/list/", response_class=HTMLResponse)
def get_all_cities_html():
    return tmpl.render(items=get_all_cities_json())


@router.get("/{id}/")
def get_city(id: int):
    return session.query(City).get(id)
