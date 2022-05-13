from uuid import uuid4

from PIL import Image
from fastapi import UploadFile

from celery_settings import app


@app.task
def crop_image(file_bytes: bytes, filename: str):
    # filename = f'{uuid4()}.jpeg'
    filepath = f'media/{filename}'
    # file_bytes = file.file.read()
    image = Image.open(file_bytes)
    croped_image = image.resize((600, 400))
    croped_image.save(filepath)
    return filename
