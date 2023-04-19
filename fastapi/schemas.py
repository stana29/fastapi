from pydantic import BaseModel


class CityInfo(BaseModel):
    name: str
    population: int


class PersonInfo(BaseModel):
    name: str
    city_id: int
