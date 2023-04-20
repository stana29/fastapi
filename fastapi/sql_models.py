from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sql_database import Base


class City(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    population: Mapped[int]

    persons: Mapped[list["Person"]] = relationship(back_populates="city")

    # def __repr__(self):
    #    return self.name


class Person(Base):
    __tablename__ = "persons"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    city_id = mapped_column(ForeignKey("cities.id"))

    city: Mapped["City"] = relationship(back_populates="persons")
