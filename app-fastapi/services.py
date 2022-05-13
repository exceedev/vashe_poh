import aiofiles
import os

from uuid import uuid4
from fastapi import UploadFile, HTTPException
from tasks import crop_image


CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/heic']


async def save_image(file: UploadFile):
    if not os.path.exists('media/'):
        os.makedirs('media')
    filename = f'{uuid4()}.jpeg'
    # filepath = f'media/{filename}'
    file_bytes = file.file.read()
    if file.content_type in CONTENT_TYPES:
        crop_image.apply_async(
            queue='high_priority', args=(str(file_bytes), filename)
        )

    else:
        raise HTTPException(status_code=412, detail='Incorrect image type')
    return filename


async def write_image(filename: str, file: UploadFile):
    async with aiofiles.open(filename, 'wb') as buffer:
        data = await file.read()
        await buffer.write(data)
