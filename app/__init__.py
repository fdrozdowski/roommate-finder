from flask import Flask
from flask.ext.mail import Mail
import flask.ext.sqlalchemy
from flask_cas import CAS
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = flask.ext.sqlalchemy.SQLAlchemy(app)
CAS(app)
mail = Mail(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models, profile, email
