from bson.objectid import ObjectId as BsonObjectId
from pydantic import BaseModel


class PydanticObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class GetImage(BaseModel):
    def __init__(self, **data):
        if '_id' in data.keys():
            data['id'] = data.pop('_id')
        super().__init__(**data)

    filename: str
    id: PydanticObjectId
