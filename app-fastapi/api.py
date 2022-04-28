from bson import ObjectId
from fastapi import APIRouter, UploadFile, File, status, HTTPException
from fastapi.responses import Response

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
    find_image = await collection.find_one({'_id': ObjectId(image_id)})
    if not find_image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Image not found'
        )
    return find_image


@image_router.put('/{image_id}/', response_model=GetImage)
async def put_image(image_id: str, file: UploadFile = File(...)):
    find_image = await collection.find_one({'_id': ObjectId(image_id)})
    if not find_image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Image not found'
        )
    file_save = await save_image(file)
    update_value = {'$set': {'filename': file_save}}
    await collection.update_one(find_image, update_value)
    document = {'filename': file_save, 'id': ObjectId(image_id)}
    return document


@image_router.delete('/{image_id}/', status_code=204)
async def delete_image(image_id: str):
    find_image = await collection.find_one({'_id': ObjectId(image_id)})
    if not find_image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Image not found'
        )
    await collection.delete_one(find_image)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
