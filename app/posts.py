from db import db
from sqlalchemy.sql import text
import users

def get_posts():
    sql = text("SELECT P.content, U.username, P.created_at FROM posts P, users U WHERE P.user_id=U.id ORDER BY P.id")
    result = db.session.execute(sql)
    return result.fetchall()

def create_post(content):
    user_id = users.user_id()
    if not user_id:
        return False
    sql = text("INSERT INTO posts (content, user_id, created_at) VALUES (:content, :user_id, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True