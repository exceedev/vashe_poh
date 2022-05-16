from PIL import Image

from celery_settings import app


@app.task
def resize_image(filepath: str):
    image = Image.open(filepath)
    output = image.resize((600, 400))
    output.save(filepath)
    return filepath
