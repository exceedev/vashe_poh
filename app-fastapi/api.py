from fastapi import APIRouter, UploadFile, File

image_router = APIRouter()


@image_router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    return {'filename': file.filename}
