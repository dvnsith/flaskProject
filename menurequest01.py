#!/usr/bin/env python3
import requests
from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from datetime import date


app = Flask(__name__)
app.secret_key = "asdsa456564dasdsd"


@app.route("/")
def index():
    # if the key "username" has a value in session
    if "username" in session:
        username = session["username"]
        URL = "http://127.0.0.1:3000/"
        menu = requests.get(URL).json()
        return render_template("menu.html", name=username, menu=menu, date=date.today())

    return render_template("splash.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # if you sent us a POST because you clicked the login button
    if request.method == "POST":

        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    # return this HTML data if you send us a GET
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
