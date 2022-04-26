from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class JWT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship('User',
                           backref=db.backref('jwt', lazy=True))
    token = db.Column(db.String(400), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username.username


db.create_all()


@app.route('/register', methods=['POST', ])
def users():
    if request.method == 'POST':
        try:
            password = request.json['password']
            hash = generate_password_hash(password)

            user = User(
                username=request.json['username'],
                email=request.json['email'],
                password=hash
            )

            db.session.add(user)
            db.session.flush()

            jwt = JWT(
                token='awdawdawdawd123123123',
                user_id=user.id
            )

            db.session.add(jwt)
            db.session.commit()

            return jsonify({'status': 200, 'hash': hash, 'password': password})
        except:
            db.session.rollback()
            return jsonify({'status': 300})


@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'GET':
        return jsonify({'response': 'GET', 'user_id': user_id})
    elif request.method == 'POST':
        return jsonify({'response': 'POST', 'user_id': user_id})


app.run()
