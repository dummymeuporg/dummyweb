import importlib

from flask import Flask

from .conf import settings

app = Flask(__name__)
app.secret_key = "changeme".encode()