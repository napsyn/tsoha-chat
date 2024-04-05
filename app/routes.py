from app import app
from flask import redirect, render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    sql = "SELECT id, content, created_at FROM polls ORDER BY id DESC"
    result = db.session.execute(sql)
    posts = result.fetchall()
    return render_template("dashboard.html", items=posts)