from app import app
from flask import render_template, request, jsonify


@app.route('/')
def index():
    think = 'start'
    return render_template('index.html', title=think)


@app.route('/auth', methods=['GET'])
def auth_get():
    return 'hi'
