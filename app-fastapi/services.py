import aiofiles
import os

from uuid import uuid4
from fastapi import UploadFile, HTTPException


CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/heic']


async def save_image(file: UploadFile):
    if not os.path.exists('media/'):
        os.makedirs('media')
    filename = f'{uuid4()}.jpeg'
    filepath = f'media/{filename}'
    if file.content_type in CONTENT_TYPES:
        await write_image(filepath, file)
    else:
        raise HTTPException(status_code=412, detail='Incorrect image type')
    return filename


async def write_image(filename: str, file: UploadFile):
    async with aiofiles.open(filename, 'wb') as buffer:
        data = await file.read()
        await buffer.write(data)
