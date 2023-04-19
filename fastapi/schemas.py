from pydantic import BaseModel


class CityInfo(BaseModel):
    name: str
    population: int
