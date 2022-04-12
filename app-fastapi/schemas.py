from pydantic import BaseModel


class GetImage(BaseModel):
    user: str
    title: str
    description: str
