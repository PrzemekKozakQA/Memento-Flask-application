from flask import redirect, session, flash
from functools import wraps
from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memento.db")


def login_required(f):
    # Decorate routes to require login.
    # https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def get_username_err(username):
    if not username or username.isspace():
        return "Username can not be empty!!!"
    username = username.strip()
    users_with_this_name = db.execute(
        "SELECT id FROM users WHERE username=?", username)
    if len(users_with_this_name) > 0:
        return "User with this name already exists, choose a different name!!!"
    # if username is available
    return ""


def is_password_and_confirmation_valid(password, confirmation):
    # checks the password and its confirmation, displays error information in the flask message
    if not password or not confirmation:
        flash("Password and its confirmation can not be empty!!!", "danger")
        return False
    if len(set(password)) < 5:
        flash("The password must contain at least 5 different characters!!!", "danger")
        return False
    if password != confirmation:
        flash("The password and its confirmation cannot be different!!!", "danger")
        return False
    return True


def is_word_or_def_empty(word, definition):
    # checks the word and its definition, displays error information in the flask message
    result = False
    if not word or word.isspace():
        flash("Word/concept can not be empty", "danger")
        result = True
    if not definition or definition.isspace():
        flash("Definition/meaning can not be empty", "danger")
        result = True
    return result


def is_word_repeated(word):
    # checks whether the word is already saved by the user and displays error information in the flask message
    user_words_data = db.execute(
        "SELECT word FROM words WHERE userId=?", session["user_id"])
    user_words = [dict.get("word") for dict in user_words_data]
    if word.strip() in user_words:
        flash(
            f'"{word}" definition/meaning already exists, edit or delete it in the "search" tab', "danger")
        return True
    else:
        return False
