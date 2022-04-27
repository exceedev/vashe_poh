from bson import ObjectId
from fastapi import APIRouter, UploadFile, File

from db import collection
from services import save_image
from schemas import GetImage, PydanticObjectId


image_router = APIRouter(
    prefix='/images'
)


@image_router.post('/upload/', response_model=GetImage, status_code=201)
async def upload_file(file: UploadFile = File(...)):
    file_save = await save_image(file)
    document = {'filename': file_save}
    object_ = await collection.insert_one(document)
    document |= {'id': object_.inserted_id}
    return document


@image_router.get('/{image_id}/', response_model=GetImage)
async def get_image(image_id: str):
    result = await collection.find_one({'_id': ObjectId(image_id)})
    return result
