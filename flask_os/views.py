from app import app
from flask import render_template, request, jsonify


@app.route('/')
def index():
    response = {
        'status': 200,
        'title': 'INDEX'
    }
    return jsonify(response)


@app.route('/auths', methods=['GET', 'POST'])
def auth():
    response = {
        'status': 200,
        'title': 'AUTH TEST',
        'method': request.method,
        'your json': request.json
    }
    return jsonify(response)


@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def auth():
    response = {
        'status': 200,
        'title': 'AUTH TEST',
        'method': request.method,
        'your json': request.json
    }
    return jsonify(response)
