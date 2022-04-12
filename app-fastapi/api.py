from fastapi import APIRouter


image_router = APIRouter()


@image_router.get('/')
async def get_all_images():
    pass