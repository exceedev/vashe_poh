from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models import *


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/test', methods=['GET', 'POST'])
@jwt_required()
def test():
    return jsonify({'count': 'count'})


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
    token = user.get_token()
    return {'access_token': token}
