from models import *
from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = app.test_client()

engine = create_engine('sqlite:///db.sqlite')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)


Base.metadata.create_all(bind=engine)


@app.route('/test/<int:cound>', methods=['GET'])
@jwt_required
def test(count):
    return jsonify({'count': count})


@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run()
