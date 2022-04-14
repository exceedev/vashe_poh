from fastapi import FastAPI
from api import image_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(image_router)

app.mount('/media', StaticFiles(directory='media'), name='media')
