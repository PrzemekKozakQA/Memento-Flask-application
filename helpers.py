from flask import redirect, session, flash
from functools import wraps
from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memento.db")


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


def get_username_err(username):
    # Ensure username was submitted
    if not username or username.isspace():
        return "Username can not be empty!!!"
    # checking in DB
    username = username.strip()
    users_with_this_name = db.execute("SELECT id FROM users WHERE username=?", username)
    if len(users_with_this_name) > 0:
        return "User with this name already exists, choose a different name!!!"
    # if username is available
    return ""


def is_password_and_confirmation_valid(password, confirmation):
    result = True
    # Checking if password or confirmation is empty
    if not password or not confirmation:
        flash("Password and its confirmation can not be empty!!!", "danger")
        result = False
    # Checking whether the password and its confirmation have at least 5 different characters
    if len(set(password)) < 5:
        flash("The password must contain at least 5 different characters!!!", "danger")
        result = False
    # Checking if password and confirmation are the same
    if password != confirmation:
        flash("The password and its confirmation cannot be different!!!", "danger")
        result = False
    return result


def is_word_or_def_empty(word, definition):
    result = False
    if not word or word.isspace():
        flash("Word/concept can not be empty", "danger")
        result = True
    if not definition or definition.isspace():
        flash("Definition/meaning can not be empty", "danger")
        result = True
    return result


def is_word_repeated(word):
    user_words_data = db.execute("SELECT word FROM words WHERE userId=?", session["user_id"])
    user_words = [dict.get("word") for dict in user_words_data]
    if word.strip() in user_words:
         flash(f'"{word}" definition/meaning already exists, edit or delete it in the "search" tab', "danger")
         return True
    else:
        return False
