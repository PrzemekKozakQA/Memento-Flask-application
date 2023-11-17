from flask import redirect, session
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


def get_username_status(username):
    # Ensure username was submitted
    if not username or username.isspace():
        return "Username can not be empty!!!"
    # checking in DB
    username = username.strip()
    users_with_this_name = db.execute("SELECT id FROM users WHERE username=?", username)
    if len(users_with_this_name) > 0:
        return "User with this name already exists, choose a different name!!!"
    # if username is available
    return "available"


def get_password_and_confirmation_status(password, confirmation):
    # Checking if password or confirmation is empty
    if not password or not confirmation:
        return "Password and its confirmation can not be empty!!!"
    # Checking whether the password and its confirmation have at least 5 different characters
    if len(set(password)) < 5:
        return "The password must contain at least 5 different characters!!!"
    # Checking if password and confirmation are the same
    if password != confirmation:
        return "The password and its confirmation cannot be different!!!"
    return "ok"


def check_word_data(word, definition):
    # Checking if word or definition is empty
    if not word or word.isspace():
        return "Word/concept can not be empty"
    if not definition or definition.isspace():
        return "Definition/meaning can not be empty"
    # Checking word and  definition length
    if len(word.strip()) > 50:
        return "Maximum word/concept length is 50 characters"
    if len(definition.strip()) > 10**5:
        return "Definition/meaning is too long"
    # Checking if word has already been added by the user
    user_words_data = db.execute("SELECT word FROM words WHERE userId=?", session["user_id"])
    user_words = [dict.get("word") for dict in user_words_data]
    if word in user_words:
        return f'"{word}" definition/meaning already exists, edit or delete it in the "search" tab'
    # If everything is fine return ok
    return "ok"
