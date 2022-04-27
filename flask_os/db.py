from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


engine = create_engine('sqlite:///db.sqlite')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = session.query_property()

Base.metadata.create_all(bind=engine)
