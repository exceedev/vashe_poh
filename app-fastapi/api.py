from bson import ObjectId
from fastapi import APIRouter, UploadFile, File
from starlette import status
from starlette.responses import Response

from db import collection
from services import save_image
from schemas import GetImage


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


@image_router.put('/{image_id}/', response_model=GetImage)
async def put_image(image_id: str, file: UploadFile = File(...)):
    find_image = await collection.find_one({'_id': ObjectId(image_id)})
    file_save = await save_image(file)
    update_value = {'$set': {'filename': file_save}}
    await collection.update_one(find_image, update_value)
    document = {'filename': file_save, 'id': ObjectId(image_id)}
    return document


@image_router.delete('/{image_id}/', status_code=204)
async def delete_image(image_id: str):
    await collection.delete_one({'_id': ObjectId(image_id)})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
