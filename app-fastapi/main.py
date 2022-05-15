from fastapi import FastAPI

from api import image_router

app = FastAPI()

app.include_router(image_router)
