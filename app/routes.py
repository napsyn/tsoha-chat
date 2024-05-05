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
    categories = posts.get_categories()
    return render_template("dashboard.html", items=items, categories=categories)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form.get('username')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')

        if password1 != password2:
            return flash("Mismatching passwords")
        
        if users.register(username, password1):
            flash('Account succesfully created')
            return redirect("/login")
        else:
            return flash("Registration failed")

@app.route("/newpost", methods=["POST"])
def new_post():
    if not request.form['csrf_token']:
        return flash("Post creation failed")
    
    content = request.form["content"]
    title = request.form["title"]
    post_category = request.form["post_category"]

    if posts.create_post(title, content, post_category):
        return redirect("/dashboard")
    else:
        return render_template("error.html", message="An error occurred in creating a new post")
    
@app.route("/post/<post_id>", methods=["GET","POST"])
def get_post(post_id):
    if request.method == "DELETE":
        posts.delete_post(post_id)
        return redirect("dashboard")
    
    result = posts.get_post(post_id)

    if not result:
        return flash("Oops, something went wrong")
    else:
        return render_template("post.html", title=result[0], content=result[1], date=result[2])
    
@app.route("/userposts")
def user_posts():
    items = posts.user_posts()
    return render_template("user_posts.html", items=items)

@app.route("/manageusers")
def manage_users():
    all_users = users.get_users()
    if not all_users:
        return redirect("/dashboard")
    else:
        return render_template("admin_view.html", users=all_users)

@app.route("/delete/<post_id>")
def delete_post(post_id):
    if not posts.delete_post(post_id):
        return flash("An error occurred")
    else:
        flash("Post deleted")
        return redirect("/userposts")
    
@app.route("/settings/<user_id>")
def user_settings(user_id):
    user_data = users.get_user(user_id)
    option1, option2 = users.role_options(user_data[2])
    if not user_data:
        return flash("User fetch failed")
    else:
        return render_template("user_data.html", user=user_data, option1=option1, option2=option2)
    
@app.route("/user/modify", methods=['GET', 'POST'])
def modify_role():
    if request.method == "POST":
        role = request.form['role']
        id = request.form['user_id']
        print(role)
        print(id)
        if not users.modify_role(role, id):
            return flash("Error modifying role")
        else:
            flash("Role modified")
            return redirect("/manageusers")
    else:
        return redirect("/manegeusers")

@app.route("/user/delete/<user_id>")
def delete_user(user_id):
    if not user_id:
        return flash("Error deleting user")
    if not users.delete_user(user_id):
        return flash("Error deleting user")
    else:
        return redirect("/manageusers")

@app.route("/filter", methods=['POST'])
def filter_by_category():
    category = request.form.get('category')
    items_filtered = posts.filter_by_category(category)
    categories = posts.get_categories()
    return render_template("dashboard.html", items=items_filtered, categories=categories)
