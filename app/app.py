from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, get_username_err, is_word_or_def_empty, is_word_repeated, is_password_and_confirmation_valid
import json
import random

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memento.db")


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # Forget any user_id if logged user has proceeded to register endpoint by changing URL
    session.pop("user_id", None)

    ### POST method ###
    if request.method == "POST":
        username = request.form.get("username")
        username_err = get_username_err(username)

        # Handle AJAX request
        if request.form.get("ajaxCheckUsername") == "true":
            if username_err:
                # Send JSON with error message
                return jsonify(dict(message=username_err)), 400, {"Content-Type": "application/json"}
            else:
                return "OK", 200

        # The following form request processing is necessary if user has disabled JS scripts in his browser
        if username_err:
            flash(username_err, "danger")
            return redirect(request.url)
        else:
            username = username.strip()

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not is_password_and_confirmation_valid(password, confirmation):
            # flash message with error has been added in is_password_and_confirmation_valid() method
            return redirect(request.url)

        new_user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Log in registered user
        session["user_id"] = new_user_id
        session["username"] = username

        flash("The new user registration was successful. You are logged in to the account you created.", "success")
        return redirect("/")

    ### GET method ###
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id if logged user has proceeded to register endpoint
    # Added a second parameter "None" to handle the error if the "user_id" key is not found
    session.pop("user_id", None)

    ### POST method ###
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or username.isspace():
            flash("Username can not be empty", "danger")
            return redirect(request.url)
        else:
            username = username.strip()

        if not password:
            flash("Password can not be empty", "danger")
            return redirect(request.url)

        user_data_rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists
        if len(user_data_rows) != 1:
            flash("Invalid username or/and password!", "danger")
            return redirect(request.url)

        user_data = user_data_rows[0]

        # Ensure password is correct
        hash = user_data.get("hash")
        if not check_password_hash(hash, password):
            flash("Invalid username or/and password!", "danger")
            return redirect(request.url)

        # Remember which user has logged in
        session["user_id"] = user_data.get("id")
        session["username"] = username

        flash(f"Hi {username}! You were successfully logged in!", "success")
        return redirect("/")

    ### GET method ###
    return render_template("login.html")


@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    flash("You were successfully logged out!", "warning")
    return redirect("/")


@app.route("/account")
@login_required
def account():
    return render_template("account.html", user=session["username"])


@app.route("/user/rename", methods=["POST"])
@login_required
def rename_user():
    new_name = request.form.get("newUsername")

    new_name_err = get_username_err(new_name)
    if new_name_err:
        flash(new_name_err, "danger")
        return redirect("/account")
    else:
        new_name = new_name.strip()

    db.execute("UPDATE users SET username=? WHERE id=?",
               new_name, session["user_id"])
    session["username"] = new_name
    flash("The username change was successful!", "success ")
    return redirect("/account")


@app.route("/password/change", methods=["POST"])
@login_required
def change_password():
    old_password = request.form.get("oldPassword")
    new_password = request.form.get("newPassword")
    confirmation = request.form.get("newPasswordConf")

    if not old_password:
        flash(" Old password can not be empty", "danger")
        return redirect("/account")

    # Ensure username old password is correct
    old_password_data = db.execute(
        "SELECT hash FROM users WHERE id = ?", session["user_id"])
    old_hash = old_password_data[0].get("hash")
    if not check_password_hash(old_hash, old_password):
        flash("Invalid old password!", "danger")
        return redirect("/account")

    # Check new password and it confirmation
    if not is_password_and_confirmation_valid(new_password, confirmation):
        return redirect("/account")

    hash = generate_password_hash(new_password)

    db.execute("UPDATE users SET hash = ? WHERE id = ?",
               hash, session["user_id"])

    return redirect("/logout")


@app.route("/user/delete", methods=["POST"])
@login_required
def delete_user():
    user_id = session["user_id"]
    # Deleting users data
    db.execute("DELETE FROM words WHERE userId=?", user_id)
    # Delete user
    db.execute("DELETE FROM users WHERE id=?", user_id)

    session.clear()
    flash("The user account and all its data have been deleted!", "secondary")
    return redirect("/")


@app.route("/add")
@login_required
def add():
    return render_template("add.html")


@app.route("/words", methods=["GET", "POST"])
@login_required
def words():
    ### POST method ###
    if request.method == "POST":
        word = request.form.get("wordInput")
        definition = request.form.get("defInput")

        if is_word_or_def_empty(word, definition):
            # flash message with error information has been added in is_word_or_def_empty() method
            return redirect("/add")
        else:
            word = word.strip()
            definition = definition.strip()

        is_memorized = request.form.get("isMemorizedSwitch") == "on"

        if is_word_repeated(word):
            # flash message with error information has been added in is_word_repeated() method
            return redirect("/add")

        db.execute("INSERT INTO words(word, definition, isMemorized, userId) VALUES (?, ?, ?, ?)",
                   word, definition, int(is_memorized), session["user_id"])

        flash("Added successfully!", "success")
        return redirect("/add")

    ### GET method ###
    if request.method == "GET":
        q = request.args.get("q")
        # if searched word is empty
        if not q or q.isspace():
            words_data = []
        # if user wants to display all his words
        elif q == "%":
            words_data = db.execute(
                "SELECT word, definition, isMemorized, id FROM words WHERE userId=? ORDER BY word", session["user_id"])
        # if user wants to display words start with given text
        else:
            words_data = db.execute(
                "SELECT word, definition, isMemorized, id FROM words WHERE word LIKE ? AND userId=? ORDER BY word", q.strip() + "%", session["user_id"])
        # dumps() parse list of dict to json
        return json.dumps(words_data), 200, {"Content-Type": "application/json"}


@app.route("/words/<id>", methods=["DELETE", "POST", "GET"])
@login_required
def word(id):
    word_data_row = db.execute(
        "Select * FROM words WHERE id=? AND userId=?", id, session["user_id"])

    ### GET method ###
    if request.method == "GET":
        if not word_data_row:
            flash("Word/concept with this id was not found", "danger")
            return page_not_found(404), 404
        word_data = word_data_row[0]
        return render_template("word.html", id=id, word=word_data.get("word"), definition=word_data.get("definition"), isMemorized=word_data.get("isMemorized"))

    ### DELETE method ###
    if request.method == "DELETE":
        deleted_rows_number = db.execute(
            "DELETE FROM words WHERE id=? AND userId=?", id, session["user_id"])
        if deleted_rows_number == 1:
            return "OK", 200
        else:
            return "ERROR", 400

    ### POST method ###
    if request.method == "POST":
        if not word_data_row:
            flash(
                "The updated word/concept was not found, it was probably deleted in the meantime.", "danger")
            return page_not_found(404), 404

        updated_word = request.form.get("wordInput")
        updated_definition = request.form.get("defInput")

        if is_word_or_def_empty(updated_word, updated_definition):
            # a flash message with error information has been added in is_word_or_def_empty() method
            return redirect(request.url)
        else:
            updated_word = updated_word.strip()
            updated_definition = updated_definition.strip()

        # getting the value of the "isMemorize" switch
        is_memorized = request.form.get("isMemorizedSwitch") == "on"

        # if the words/meaning have been changed and it is repeated in the database
        if not updated_word == word_data_row[0].get("word") and is_word_repeated(updated_word):
            return redirect(request.url)

        changed_row_num = db.execute("UPDATE words SET word=?, definition=?, isMemorized=? WHERE id=? AND userId=?",
                                     updated_word, updated_definition, int(is_memorized), id, session["user_id"])
        if changed_row_num < 1:
            flash("Something went wrong and no entries were changed", "danger")
        else:
            flash("Update successfully", "success")
        return redirect(request.url)


@app.route("/search")
@login_required
def search():
    return render_template("search.html")


@app.route("/memorize", methods=["POST", "GET"])
@login_required
def memorize():
    ### POST method ###
    if request.method == "POST":
        # Update information whether the word is remembered
        id = request.form.get("wordId")
        updated_rows_number = db.execute(
            "UPDATE words SET isMemorized=1 WHERE id=? AND userId=?", id, session["user_id"])
        if updated_rows_number != 1:
            return "Error", 400
        else:
            return "OK", 200

    ### GET method ###
    # Get all user's unremembered words
    user_words_data = db.execute(
        "SELECT word, definition, id FROM words WHERE userId=? AND isMemorized=0", session["user_id"])

    # Checking if there are words to remember and choose random word
    if len(user_words_data) > 0:
        word_data = random.choice(user_words_data)
    else:
        word_data = {}
    return render_template("memorize.html", word_data=word_data)


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    ### POST method ###
    if request.method == "POST":
        # Checking quiz answers
        user_answer = request.form.get("word")
        if not user_answer:
            flash("Something get wrong", "danger")
            return redirect("/quiz")
        if user_answer == session["quiz_answer"]:
            return jsonify(dict(status="right")), 200, {"Content-Type": "application/json"}
        else:
            return jsonify(dict(status="wrong")), 200, {"Content-Type": "application/json"}

    ### GET method ###
    rows_user_words = db.execute(
        "SELECT word FROM words WHERE userId=?", session["user_id"])

    user_words = [dict["word"] for dict in rows_user_words]

    # Checking whether the user has added enough words to complete the quiz
    if len(user_words) < 3:
        words = []
        question = ""
    else:
        # Getting random words without repetitions
        words = random.sample(user_words, 4)

        # Select answer word and getting a question for it
        answer = random.choice(words)
        question_data = db.execute(
            "SELECT definition FROM words WHERE word=? AND userId=?", answer, session["user_id"])
        question = question_data[0].get("definition")

        # Saving the correct answer to the user's session file
        session["quiz_answer"] = answer

    return render_template("quiz.html", words=words, question=question)
