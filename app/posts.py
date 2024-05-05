from db import db
from sqlalchemy.sql import text
import users

def get_posts():
    sql = text("SELECT P.post_id, P.title, P.content, U.username, P.created_at FROM posts P JOIN users U ON P.user_id=U.user_id ORDER BY P.created_at")
    result = db.session.execute(sql)
    return result.fetchall()

def create_post(title, content, category):
    user_id = users.user_id()
    if not user_id:
        return False
    sql = text("INSERT INTO posts (title, content, user_id, created_at) VALUES (:title, :content, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    sql = text("SELECT post_id FROM posts where user_id=:user_id ORDER BY created_at DESC")
    result = db.session.execute(sql, {'user_id': user_id})
    post_id = result.fetchone()
    post_id = post_id[0]
    sql = text("INSERT INTO post_categories (post_id, category_id) VALUES(:post_id, :category_id)")
    db.session.execute(sql, {'post_id': post_id, 'category_id': category})
    try:
        db.session.commit()
    except:
        return False
    return True

def get_categories():
    sql = text("SELECT * FROM categories")
    result = db.session.execute(sql)
    categories = result.fetchall()
    return categories

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

def user_posts():
    sql = text("SELECT post_id, title, content, created_at FROM posts WHERE posts.user_id=:user_id ORDER BY created_at")
    id = users.user_id()

    if not id:
        return False
    else:
        result = db.session.execute(sql, {'user_id': id})
        return result.fetchall()

def delete_post(post_id):
    sql = text("DELETE from posts WHERE posts.post_id=:post_id")
    db.session.execute(sql, {'post_id': post_id})
    try:
        db.session.commit()
    except:
        return False
    return True

def filter_by_category(category):
    sql = text("SELECT P.post_id, P.title, P.content, U.username, P.created_at FROM posts P JOIN users U ON P.user_id=U.user_id JOIN post_categories C ON p.post_id=C.post_id WHERE C.category_id=:category ORDER BY P.created_at")
    result = db.session.execute(sql, {'category': category})
    return result.fetchall()
