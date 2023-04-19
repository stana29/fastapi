from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship

from sql_database import Base


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)

    persons: Mapped[list["Person"]] = relationship(back_populates="city")

    def __repr__(self):
        return self.name


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city: Mapped["City"] = relationship(back_populates="persons")
