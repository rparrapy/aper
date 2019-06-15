from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)

login_manager = LoginManager()
login_manager.init_app(app)

import aper.auth
import aper.views
