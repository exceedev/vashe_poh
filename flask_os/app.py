from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from registration.blueprint import registration

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(registration, url_prefix='/auth')

db = SQLAlchemy(app)
