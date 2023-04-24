from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sql_database import Base, engine


class City(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    population: Mapped[int]

    persons: Mapped[list["Person"]] = relationship(back_populates="city")

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, population={self.population})"


class Person(Base):
    __tablename__ = "persons"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    city_id = mapped_column(ForeignKey("cities.id"))

    city: Mapped["City"] = relationship(back_populates="persons")

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, city_id={self.city_id})"


Base.metadata.create_all(engine)
