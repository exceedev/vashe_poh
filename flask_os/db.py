from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from .config import Config


engine = create_engine(Config.DB_CONN)

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = session.query_property()

Base.metadata.create_all(bind=engine)
