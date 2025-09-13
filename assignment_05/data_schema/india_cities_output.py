from pydantic import BaseModel


class IndiaCitiesOutPut(BaseModel):
    is_india_cities: bool
    reason: str
