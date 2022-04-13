from pydantic import BaseModel


class Image(BaseModel):
    user: str
    title: str
    description: str
