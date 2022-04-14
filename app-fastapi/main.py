from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import image_router


app = FastAPI()

app.include_router(image_router)

app.mount('/media', StaticFiles(directory='media'), name='media')
