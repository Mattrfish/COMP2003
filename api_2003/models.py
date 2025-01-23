# models.py

from datetime import datetime
import pytz
from config import db, ma

class User(db.Model):
    __tablename__= "User"
    __table_args__ = {'schema': 'STAMPEDE'}

    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Level_ID = db.Column(db.Integer, nullable=False)
    Role_ID = db.Column(db.Integer, nullable=False)
    Username = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(128), nullable=False)
    xpTotal = db.Column(db.Integer, nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)
    
