from aper import app
from flask_login import login_required, current_user


@app.route('/')
@login_required
def index():
    return 'Hello {}!'.format(current_user.id)