from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Group_names(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    group_name = db.Column(db.String(100), unique=True)

class Group_intermediary(UserMixin, db.Model):
    user_id = db.Column(db.Integer, models.ForeignKey("models.User", verbose_name=_(""), on_delete=models.CASCADE)=True) # primary keys are required by SQLAlchemy
    group_id = db.Column(db.String(100), unique=True)
