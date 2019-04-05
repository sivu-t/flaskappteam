# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt


application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
application.config['DEBUG']= True
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login = LoginManager(application)
login.login_view = "users.login"


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app

def initialize_extensions(application):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(application)
    bcrypt.init_app(application)
    login.init_app(application)

    # Flask-Login configuration





def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app



from src.flaskbasic.wsgi import *


try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
