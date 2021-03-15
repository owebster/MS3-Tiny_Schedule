import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route("/login_page")
def login_page():
    return render_template("login.html")


@app.route("/message_board")
def get_messages():
    messages = mongo.db.messages.find()
    return render_template("messages.html", messages=messages)


if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
