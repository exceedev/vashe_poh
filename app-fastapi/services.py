import os
from uuid import uuid4

import aiofiles
from fastapi import HTTPException, UploadFile

from tasks import resize_image

CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/heic']


async def save_image(file: UploadFile):
    if not os.path.exists('media/'):
        os.makedirs('media')
    filename = f'{uuid4()}.jpeg'
    filepath = f'media/{filename}'
    if file.content_type in CONTENT_TYPES:
        await write_image(filepath, file)
        resize_image.delay(filepath, filename)
    else:
        raise HTTPException(status_code=412, detail='Incorrect image type')
    return filename


async def write_image(filepath: str, file: UploadFile):
    async with aiofiles.open(filepath, 'wb') as buffer:
        data = await file.read()
        await buffer.write(data)
