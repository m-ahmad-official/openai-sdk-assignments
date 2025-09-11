from pydantic import BaseModel


class PoliticsOutput(BaseModel):
    contains_politics: bool
    reason: str
