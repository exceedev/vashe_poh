from email.policy import default
from click import password_option
from datetime import datetime


from app import db


def slugify(s):
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(86))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
