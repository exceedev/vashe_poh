from flask import Blueprint, render_template

registration = Blueprint('registration', __name__, template_folder='templates')


@registration.route('/')
def auth_list():
    return render_template('index.html', title='registration')
