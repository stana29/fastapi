from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from sql_database import session
from sql_models import City, Person
from schemas import CityInfo

router = APIRouter(prefix="/sql2")


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
    person = Person(name="taro", city_id=3)
    print(person)
    session.add(person)
    session.commit()
    return


@router.get("/all/")
def get_all_cities_json():
    response = session.query(City).order_by(City.id).all()
    return response

@router.delete("/all/")
def delete_all():
    session.query(City).delete()
    session.commit()
    return {"message": "all users deleted"}


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

env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('sql2_html_template.j2')

@router.get("/city_list/", response_class=HTMLResponse)
def get_all_cities_html():
    return tmpl.render(items = get_all_cities_json())


@router.get("/{id}/")
def get_city(id: int):
    return session.query(City).get(id)

