from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY='ubhwfgoinhwepf'
)

db = SQLAlchemy(app)

from . import routes
