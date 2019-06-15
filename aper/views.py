from aper import app
from flask_login import login_required, current_user
from flask import jsonify
from .models import User


@app.route('/')
@login_required
def index():
    return 'Hello {}!'.format(current_user.name)


@app.route('/users', methods=['GET'])
@login_required
def users():
    users = [u.serialize() for u in User.query.all()]
    return jsonify(users)