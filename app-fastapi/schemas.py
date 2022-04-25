from pydantic import BaseModel


class UploadImage(BaseModel):
    filename: str
