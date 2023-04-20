from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from sql_database import session
from sql_models import Person, City
from schemas import PersonInfo
from sqlalchemy import select

router = APIRouter(prefix="/sql2/person", tags=["person"])

env = Environment(loader=FileSystemLoader("./", encoding="utf8"))
tmpl = env.get_template("person_list.html")


@router.get("/all/")
def get_all_persons_json():
    response = session.query(Person).order_by(Person.id)
    return response.all()


@router.get("/list/", response_class=HTMLResponse)
def get_all_persons_html():
    return tmpl.render(items=get_all_person_with_city())


@router.get("/all_c/")
def get_all_person_with_city():
    stmt = select(Person.id, Person.name, City.name).join_from(City, Person)
    print(stmt)
    response = session.execute(stmt)
    columns = ("id", "name", "city")
    return [dict(zip(columns, row)) for row in response]


@router.post("/add/")
def add_person(personinfo: PersonInfo):
    session.add(Person(name=personinfo.name, city_id=personinfo.city_id))
    session.commit()
    return


@router.get("/{id}/")
def get_person(id: int):
    response = session.query(Person).where(Person.id == id)
    if response:
        print(response.one().city.name)
        return response.one()
    return
