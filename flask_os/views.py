from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token

from .models import *


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/test/<int:count>', methods=['GET', 'POST'])
@jwt_required()
def test(count):
    return jsonify({'count': count})


@users_blueprint.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@users_blueprint.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    refresh = create_refresh_token(identity=user.id)
    token = user.get_token()
    return {'access_token': token, 'refresh_token': refresh}


@users_blueprint.route('/token/refresh')
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({'refresh_token': access})