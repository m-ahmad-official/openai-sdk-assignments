from pydantic import BaseModel


class UsaCitiesOutPut(BaseModel):
    is_usa_cities: bool
    reason: str
