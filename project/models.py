from flask_login import UserMixin

from . import db

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class BillGroups (db.Model):
    __tablename__='bill_groups'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    group_name = db.Column(db.String(255), unique=True)

class BillGroupIntermediary (db.Model):
    __tablename__ = 'group_user_intermediary'
    user_id = db.Column (db.Integer), db.ForeignKey('user.id')
    group_id = db.Column (db.Integer), db.ForeignKey('bill_groups.id')

class IndividualBill (db.Model):
    __tablename__ = 'individual_bill'
    bill_id = db.Column (db.Integer), db.ForeignKey('bill_groups.id')
    bill_item = db.Column(db.String(255))


# class Group_names(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     group_name = db.Column(db.String(100), unique=True)

# class Group_intermediary(UserMixin, db.Model):
#     user_id = db.Column(db.Integer, models.ForeignKey("models.User", verbose_name=_(""), on_delete=models.CASCADE)=True) # primary keys are required by SQLAlchemy
#     group_id = db.Column(db.String(100), unique=True)
