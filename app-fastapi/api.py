from fastapi import APIRouter, UploadFile, File

from db import collection
from services import save_image
from schemas import UploadImage


image_router = APIRouter(
    prefix='/images'
)


@image_router.post('/upload/', response_model=UploadImage, status_code=201)
async def upload_file(file: UploadFile = File(...)):
    await save_image(file)
    document = {'filename': file.filename}
    await collection.insert_one(document)
    return document
