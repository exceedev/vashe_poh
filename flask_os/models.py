from email.policy import default
from click import password_option
from datetime import datetime


from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)
    email = db.Column(db.String(86), unique=True)

    def __repr__(self) -> str:
        return f'<User: id:{self.id}, username:{self.username}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'),
                     nullable=False)
    name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer)
    city = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f'<Profile: id:{self.name}>'
