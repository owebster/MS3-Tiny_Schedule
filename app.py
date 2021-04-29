import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("home.html")


@app.route("/management")
def management():
    return render_template("management.html")


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        #check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register_user"))

        register = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        flash("registration successful")
    return render_template("register.html")


@app.route("/login_page", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("management"))

            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login_page"))

        else:
            #username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login_page"))

    return render_template("login.html")


@app.route("/user") #usersection
def user():
    users = list(mongo.db.users.find().sort("fname"))

    return render_template("user.html", users=users)


@app.route("/profile") #profile section
def profile():
    return render_template("profile.html")


@app.route("/message_board") #message section
def message_board():
    messages = mongo.db.messages.find()
    return render_template("messages.html", messages=messages)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login_page"))


@app.route("/contact_page") #contact section
def contact_page():
    return render_template("contact.html")


@app.route("/new_message") #add new message section
def new_message():
    return render_template("new_message.html")


@app.route("/add_message", methods=["GET", "POST"]) #create new message in mongodb
def add_message():
    if request.method == "POST":
        message = {
            "message_title": request.form.get("message_title"),
            "message_content": request.form.get("message_content"),
            "created_by": session["user"]
        }
        mongo.db.messages.insert_one(message)
        flash("Message posted")
        return redirect(url_for("message_board"))

    messages = mongo.db.messages.find().sort("messages", 1)
    return render_template("new_message.html", messages=messages)


@app.route("/delete_message/<messages_id>") #delete message
def delete_message(messages_id):
    mongo.db.messages.remove({"_id": ObjectId(messages_id)})
    flash("Message Deleted")
    return redirect(url_for("message_board"))


@app.route("/edit_message/<messages_id>", methods=["GET", "POST"]) #edit single message in mongodb
def edit_message(messages_id):
    if request.method == "POST":
        submit = {
            "message_title": request.form.get("message_title"),
            "message_content": request.form.get("message_content")
        }
        mongo.db.messages.update_one({ 
            '_id': ObjectId(messages_id) 
            }, { 
            '$set': { 
                'message_title': request.form.get("message_title"),
                'message_content': request.form.get("message_content") 
            } 
        })
        flash("Message Updated")

    messages = mongo.db.messages.find_one({"_id": ObjectId(messages_id)})
    return render_template("edit_message.html", messages=messages)


@app.route("/delete_user/<users_id>") #option to delete users by admin user
def delete_users(users_id):
    mongo.db.users.remove({"_id": ObjectId(users_id)})
    flash("User Removed")
    return redirect(url_for("user"))


if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False)
