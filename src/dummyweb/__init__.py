"""Dummy Meuporg web frontend"""

from flask import Flask, flash, redirect, render_template, request, url_for

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
from .models import db, User


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
    return render_template("index/template.html")

@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    if request.method == "POST":

        if request.form["password"] != request.form["password_confirm"]:
            flash("Passwords do not match.", "error")
            return redirect(url_for("subscribe"))
        
        if request.form["email"] != request.form["email_confirm"]:
            flash("Emails do not match", "error")
            return redirect(url_for("subscribe"))

        # XXX: Subscribe the user.
        account = User()
        account.generate_tagname(request.form["login"])
        account.set_password(request.form["password"])
        account.email = request.form["email"]

        db.session.add(account)
        db.session.commit()
        flash(f"Account {account.username} registered!", "info")
        return redirect(url_for("subscribe"))
    else:
        return render_template("subscribe/template.html")