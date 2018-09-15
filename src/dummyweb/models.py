import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ._app import app
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.environ["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username!r}>'