import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost/mydatabase'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
