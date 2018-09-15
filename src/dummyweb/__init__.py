"""Dummy Meuporg web frontend"""

from flask import Flask

from .__about__ import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __summary__,
    __title__,
    __uri__,
    __version__,
)
from ._app import app
from .models import db


__all__ = [
    "__author__",
    "__copyright__",
    "__email__",
    "__license__",
    "__summary__",
    "__title__",
    "__uri__",
    "__version__",
    "app",
    "db"
]

@app.route('/')
def index():
    return 'It works!'