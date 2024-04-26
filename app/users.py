from db import db
from flask import session, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT user_id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            sql = text("SELECT * FROM user_roles WHERE user_id=:user_id")
            result = db.session.execute(sql, {"user_id":user.user_id})
            role = result.fetchone()

            if not role:
                create_role(user)
                try:
                    result = db.session.execute(sql, {"user_id":user.user_id})
                    role = result.fetchone()
                    session['user_type'] = role.user_type
                except:
                    print("Plaa")
                    return False
            else:
                session['user_type'] = role.user_type
                
            session["user_id"] = user.user_id
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password, created_at) VALUES (:username, :password, NOW())")
    db.session.execute(sql, {"username":username, "password":hash_value})
    try:
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def is_logged():
    return session.get("username", 0)

def is_admin():
    return session.get("admin")

def is_moderator():
    return session.get("moderator")

def create_role(user):
    sql = text("INSERT INTO user_roles (user_id, user_type) VALUES(:user_id,:user_type)")
    db.session.execute(sql, {"user_id":user.user_id, "user_type":100})
    try:
        db.session.commit()
    except:
        return False
    
def get_users():
    sql = text("SELECT U.username, R.user_type, U.created_at FROM users U, user_roles R WHERE U.user_id=R.user_id AND R.user_type=300")
    if session.user.user_type == 300:
        result = db.session.execute()
        return result.fetchall()
    else:
        return False
    