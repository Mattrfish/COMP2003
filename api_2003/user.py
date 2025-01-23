# user.py

from flask import make_response, abort

from config import db
from models import User, user_schema, users_schema

def read_all():
    user = User.query.all()
    return user_schema.dump(user)

def create(user):
    User_ID = user.get("User_ID")
    existing_user = User.query.filter(User.User_ID == User_ID).one_or_none()
    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"User with id {User_ID} already exists")
    
