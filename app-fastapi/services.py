from uuid import uuid4

import aiofiles
from fastapi import UploadFile, HTTPException


CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/heic']


async def save_image(file: UploadFile):
    filename = f'media/{uuid4()}.jpeg'
    if file.content_type in CONTENT_TYPES:
        await write_image(filename, file)
    else:
        raise HTTPException(status_code=412, detail='Incorrect image type')


async def write_image(filename: str, file: UploadFile):
    async with aiofiles.open(filename, 'wb') as buffer:
        data = await file.read()
        await buffer.write(data)
