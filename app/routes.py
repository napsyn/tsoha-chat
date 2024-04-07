from app import app
from flask import redirect, render_template, request, flash, session
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        if users.login(request.form["username"], request.form["password"]):
            return redirect("/dashboard")
        else:
            flash("Incorrect username or password")
            return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    users.logout()
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    testitems = ["moi", "testi", "jee"]
    return render_template("dashboard.html", items=testitems)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            error = "Mismatching passwords"
            return render_template("error.html", error=error)
        if users.register(username, password1):
            flash('Account succesfully created')
            return redirect("/login")
        else:
            error = "Registration failed"
            return render_template("error.html", error=error)