from flask import redirect, session
from functools import wraps
from cs50 import SQL


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def get_user_data(name):
    # Configure CS50 Library to use SQLite database
    db = SQL("sqlite:///memento.db")
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)
    return rows
