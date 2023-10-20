from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
import json

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memento.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
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
    """Register user"""
    # Forget any user_id
    session.pop("user_id", None)

    # User reached route via POST
    if request.method == "POST":
        username = request.form.get("username")

        # AJAX request handling
        if request.form.get("check") == "username":
            # Ensure username was submitted
            if not username or username.isspace():
                return jsonify(dict(message="Username can not be empty!"))
            else:
                username = username.strip()

            # Checking if the username is already registered
            users_with_this_name = db.execute(
                "SELECT * FROM users WHERE username=?", username
            )
            if len(users_with_this_name) > 0:
                return jsonify(
                    dict(
                        message="User with this name already exists, choose a different name!"
                    )
                )

            # Send message that user can register with this username
            return jsonify(dict(username_status="ok"))

        # Form request handling
        else:
            # Ensure username was submitted
            if not username or username.isspace():
                flash("Username can not be empty", "danger ")
                return redirect(request.url)
            else:
                username = username.strip()

            # Checking if the username is already registered
            users_with_this_name = db.execute(
                "SELECT * FROM users WHERE username=?", username
            )
            if len(users_with_this_name) > 0:
                flash(
                    "User with this name already exists, choose a different name!",
                    "danger ",
                )
                return redirect(request.url)

            # Get password and confirmation from form
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")

            # Checking if password or confirmation is empty
            if not password or not confirmation:
                flash("Password or it confirmation can not be empty!", "danger ")
                return redirect(request.url)

            # Checking whether the password and its confirmation have at least 5 characters
            if len(set(password)) < 5:
                flash(
                    "The password must contain at least 5 different characters!",
                    "danger ",
                )
                return redirect(request.url)

            # Checking if password and confirmation are the same
            if password != confirmation:
                flash(
                    "The password and its confirmation cannot be different!", "danger"
                )
                return redirect(request.url)

        # Generate hash from password
        hash = generate_password_hash(password)

        # Saving the new user's data to the database
        new_user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
        )

        # Remember which user has register
        session["user_id"] = new_user_id

        # Redirect user to home page with message
        flash(
            "The new user registration was successful. You are logged in to the account you created.",
            "success ",
        )
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.pop("user_id", None)

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")

        # Ensure username was submitted
        if not username or username.isspace():
            flash("Username can not be empty", "danger ")
            return redirect(request.url)
        else:
            username = username.strip()

        # Ensure password was submitted
        password = request.form.get("password")
        if not password:
            flash("Password can not be empty", "danger ")
            return redirect(request.url)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1:
            flash("Invalid username and/or password!", "danger")
            return redirect(request.url)

        # Ensure password is correct
        check_password_hash(rows[0]["hash"], password)
        if not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password!", "danger")
            return redirect(request.url)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect to main page and show message
        flash("You were successfully logged in!", "success ")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form and show flash message
    flash("You were successfully logged out!", "warning")
    return redirect("/")


@app.route("/add")
@login_required
def add():
    return render_template("add.html")


@app.route("/search")
@login_required
def search():
    return render_template("search.html")


@app.route("/words", methods=["GET", "POST"])
@login_required
def words():
    if request.method == "POST":
        word_input = request.form.get("word_input")
        def_input = request.form.get("def_input")
        if not word_input or word_input.isspace():
            flash("Concept/word can not be empty", "danger ")
            return redirect("/add")
        if not def_input or def_input.isspace():
            flash("Definition/meaning can not be empty", "danger ")
            return redirect("/add")

        word = word_input.strip()
        definition = def_input.strip()
        if len(word) > 50:
            flash("Maximum concept/word length is 50 characters", "danger ")
            return redirect("/add")
        if len(definition) > 10**5:
            flash("Definition/meaning is too long", "danger ")
            return redirect("/add")

        rows = db.execute("SELECT word FROM words WHERE userId=?", session["user_id"])
        user_words = [dict["word"] for dict in rows]

        if word in user_words:
            flash(
                '"'
                + word
                + "\" definition/meaning already exists, edit or delete it in the 'search' tab",
                "warning",
            )
            return redirect("/add")

        db.execute(
            "INSERT INTO words(word, definition, userId) VALUES (?, ?, ?)",
            word,
            definition,
            session["user_id"],
        )
        flash("Added successfully!", "success")
        return redirect("/add")

    if request.method == "GET":
        q = request.args.get("q")
        if not q or q.isspace():
            rows = []
        else:
            rows = db.execute(
                "SELECT word, definition, id FROM words WHERE word LIKE ? AND userId=? LIMIT 100",
                q.strip() + "%",
                session["user_id"],
            )
        return json.dumps(rows)


@app.route("/words/<id>", methods=["DELETE", "POST", "GET"])
@login_required
def word(id):
    word_data = db.execute("Select * FROM words WHERE id=? AND userId=?", id, session["user_id"])

    if request.method == "GET":
        if not word_data:
            return page_not_found(404)
        return render_template("word.html",id=id, word=word_data[0]['word'], definition=word_data[0]['definition'])

    if request.method == "DELETE":
        deleted_words_number = db.execute(
            "DELETE FROM words WHERE id=? AND userId=?", id, session["user_id"]
        )
        if deleted_words_number == 1:
            return "OK", 200
        else:
            return "ERROR", 400

    if request.method == "POST":
        if not word_data:
            flash("Concept/word with this id was not found", "danger ")
            return redirect(request.url)

        word_input = request.form.get("word_input")
        def_input = request.form.get("def_input")

        if not word_input or word_input.isspace():
            flash("Concept/word can not be empty", "danger ")
            return redirect(request.url)
        if not def_input or def_input.isspace():
            flash("Definition/meaning can not be empty", "danger ")
            return redirect(request.url)

        word = word_input.strip()
        definition = def_input.strip()
        if len(word) > 50:
            flash("Maximum concept/word length is 50 characters", "danger ")
            return redirect(request.url)
        if len(definition) > 10**5:
            flash("Definition/meaning is too long", "danger ")
            return redirect(request.url)

        db.execute("UPDATE words SET word=?, definition=? WHERE id=? AND userId=?", word, definition, id, session["user_id"])
        flash("Update successfully", "success")
        return redirect(request.url)




@app.route("/memorize")
@login_required
def memorize():
    # TODO
    return render_template("memorize.html")


@app.route("/quiz")
@login_required
def quiz():
    # TODO
    return render_template("quiz.html")


@app.route("/account")
@login_required
def account():
    """Show user account"""
    rows = db.execute("SELECT username FROM users WHERE id=?", session["user_id"])
    user = rows[0]["username"]
    return render_template("account.html", user=user)


@app.route("/rename_user", methods=["POST"])
@login_required
def rename_user():
    new_user = request.form.get("new_username")

    # Ensure username was submitted
    if not new_user or new_user.isspace():
        flash("New username can not be empty", "danger ")
        return redirect("/account")
    else:
        new_user = new_user.strip()

    # Checking if the username is already registered
    users_with_this_name = db.execute("SELECT * FROM users WHERE username=?", new_user)
    if len(users_with_this_name) > 0:
        flash("User with this name already exists, choose a different name!", "danger ")
        return redirect("/account")

    # Insert new username into db
    db.execute("UPDATE users SET username=? WHERE id=?", new_user, session["user_id"])

    flash("The username change was successful!", "success ")
    return redirect("/account")


@app.route("/change_pass", methods=["POST"])
@login_required
def change_password():
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    confirmation = request.form.get("new_password_conf")
    # Ensure password was submitted
    if not old_password or not new_password or not confirmation:
        flash("Password, new pasword and it confirmation can not be empty", "danger ")
        return redirect("/account")

    # Ensure username old password is correct
    rows = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
    old_hash = rows[0].get("hash")
    if not check_password_hash(old_hash, old_password):
        flash("Invalid old password!", "danger")
        return redirect("/account")

    # Checking whether the new password and its confirmation have at least 5 characters
    if len(set(new_password)) < 5:
        flash("The password must contain at least 5 different characters!", "danger ")
        return redirect("/account")

    # Checking if new password and confirmation are the same
    if new_password != confirmation:
        flash("The password and its confirmation cannot be different!", "danger ")
        return redirect("/account")

    # Generate hash from new password
    hash = generate_password_hash(new_password)

    # Saving the new user's data to the database
    db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])

    return redirect("/logout")
