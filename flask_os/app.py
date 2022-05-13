from datetime import datetime, timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from passlib.hash import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_refresh_token, unset_jwt_cookies, create_access_token
)

from .config import Config


users_blueprint = Blueprint('users', __name__)

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user


@users_blueprint.route('/test/<int:count>', methods=['GET', 'POST'])
@jwt_required()
def test(count):
    return jsonify({'count': count})


@users_blueprint.route('/register', methods=['POST'])
def register():
    try:
        params = request.json
        user = User(**params)
        db.session.add(user)
        db.session.commit()
        token = user.get_token()
        return {'access_token': token}
    except:
        db.session.rollback()
        print('Error of create user')


@users_blueprint.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    refresh = create_refresh_token(identity=user.id)
    token = user.get_token()
    return {'access_token': token, 'refresh_token': refresh}


@users_blueprint.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@users_blueprint.route('/refresh')
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({'refresh_token': access})


app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run()
