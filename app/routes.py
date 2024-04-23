from flask import redirect, render_template, request, flash
import users, posts
from app import app

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
    items = posts.get_posts()
    return render_template("dashboard.html", items=items)

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

@app.route("/newpost", methods=["POST"])
def new_post():
    content = request.form["content"]
    title = request.form["title"]
    if posts.create_post(title, content):
        return redirect("/dashboard")
    else:
        return render_template("error.html", message="An error occurred in creating a new post")
    
@app.route("/post/<post_id>", methods=["GET","POST","DELETE"])
def get_post(post_id):
    if request.method == "DELETE":
        posts.delete_post(post_id)
        return redirect("dashboard")
    
    result = posts.get_post(post_id)

    if not result:
        return flash("Oops, something went wrong")
    else:
        return render_template("post.html", title=result[0], content=result[1], date=result[2])
    
@app.route("/settings")
def settings():
    return render_template("settings.html")