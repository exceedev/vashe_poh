import io
import os
import shutil
import gridfs
from fastapi import APIRouter, UploadFile, File
from starlette.responses import StreamingResponse

from db import image_db
from tasks import test
from dotenv import load_dotenv

load_dotenv('.env')

image_router = APIRouter(
    prefix='/images'
)

database = gridfs.GridFS(image_db)
DOWNLOAD_LOCATION = os.getenv('DOWNLOAD_LOCATION')


@image_router.get('/')
async def get_images():
    response = database.find_one({})
    binary_data = response.read()
    test.delay()
    return StreamingResponse(io.BytesIO(binary_data))


@image_router.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    download_location = f'media/{file.filename}'
    with open(download_location, 'wb') as output:
        data = database.find_one({'filename': file.filename})
        shutil.copyfileobj(data, output)
    database.put(file.file, filename=file.filename)
