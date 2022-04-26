import os


BASE_DIR = os.path.dirname(os.path.abspath(__name__))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
    SQL_TRACK_MODIFICATION = False
