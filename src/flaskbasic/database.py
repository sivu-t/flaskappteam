from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import application

db = SQLAlchemy(application)

from src.flaskbasic.wsgi import *