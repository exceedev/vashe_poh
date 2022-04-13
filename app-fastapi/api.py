import shutil

from fastapi import APIRouter, UploadFile, File
from db import image_collection, image_db
from schemas import Image
from db import connect
import gridfs

image_router = APIRouter()

record_image = gridfs.GridFS(image_db)


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
    record_image.put(file.file, filename=file.filename)


@image_router.get('/download')
async def download_file(name: str):
    download_location = f'./{name}'
    with open(download_location, 'wb') as output:
        data = record_image.find_one({'filename': name})
        shutil.copyfileobj(data, output)

