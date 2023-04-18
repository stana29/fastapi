from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Template, Environment, FileSystemLoader
from pydantic import BaseModel
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Integer, String

from sql_database import Base

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)
    def __repr__(self):
        return self.name
    

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))
