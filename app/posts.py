from db import db
from sqlalchemy.sql import text
import users

def get_posts():
    sql = text("SELECT P.post_id, P.title, P.content, U.username, P.created_at FROM posts P, users U WHERE P.user_id=U.user_id ORDER BY P.post_id")
    result = db.session.execute(sql)
    return result.fetchall()

def create_post(title, content):
    user_id = users.user_id()
    if not user_id:
        return False
    sql = text("INSERT INTO posts (title, content, user_id, created_at) VALUES (:title, :content, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def get_post(post_id):
    sql = text("SELECT P.title, P.content, P.created_at FROM posts P WHERE P.post_id=:post_id ORDER BY P.post_id")
    result = db.session.execute(sql, {"post_id":post_id})
    post = result.fetchone()
    if not post:
        return False
    
    return post

def delete_post(post_id):
    sql = text("DELETE FROM posts WHERE post_id=:post_id")
    result = db.session.execute(sql, {"post_id" : post_id})
    return result