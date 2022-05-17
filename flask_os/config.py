import os

from dotenv import load_dotenv


load_dotenv()

DATABASE_DB = os.getenv('POSTGRES_DB')
DATABASE_USER = os.getenv('POSTGRES_USER')
DATABASE_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE_HOST = os.getenv('POSTGRES_HOST')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'''
        postgresql://
        {DATABASE_USER}:
        {DATABASE_PASSWORD}@
        {DATABASE_HOST}/
        {DATABASE_DB}'''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
