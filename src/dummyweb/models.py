import hashlib
import os
import random
from pathlib import Path

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from ._app import app
from .conf import settings

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

    def set_password(self, password):
        hasher = hashlib.sha512()
        hasher.update(self.username.encode())
        hasher.update(password.encode())
        self.password = hasher.hexdigest()

    def generate_tagname(self, username):
        is_unique = False
        while not is_unique:
            number = random.randint(0, 9999)
            tagname = f"{username}.{number:04d}"
            user = self.query.filter(func.upper(tagname)).first()
            if user is None:
                self.username = tagname.upper()
                is_unique = True

    def create_directory(self):
        target_path = Path(settings.DUMMY_ACCOUNT_DIR) / self.username.upper()
        target_path.mkdir(exist_ok=True)
        with open(str((target_path) / "password"), "wb") as stream:
            stream.write(bytes.fromhex(self.password))
