import shutil

from fastapi import APIRouter, UploadFile, File
from db import image_collection, image_db
from schemas import Image
from db import connect


image_router = APIRouter()


@image_router.post('/img/{file_name}')
async def test_mongo(file_name: str):
    record_dict = {
        'file': file_name
    }
    image_db.image_collection.insert_one(record_dict)


@image_router.get('/')
async def get_images():
    return connect.local.user.find()


@image_router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    record_dict = {
        'file': buffer
    }
    image_db.image_collection.insert_one(record_dict)
