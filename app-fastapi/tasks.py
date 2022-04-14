from celery_settings import app


@app.task
def test():
    return 'Good job MAAAAAN'
