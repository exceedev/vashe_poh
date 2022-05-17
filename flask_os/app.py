from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
from flask_jwt_extended import JWTManager

try:
    from config import Config
except ImportError:
    from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

users_blueprint = Blueprint('users', __name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run()
