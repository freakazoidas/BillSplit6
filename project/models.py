from flask_login import UserMixin

from . import db

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class BillGroups (db.Model):
    __tablename__='bill_groups'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    group_name = db.Column(db.String(255), unique=True)
    # bill_intermediaries = relationship("BillGroupIntermediary", back_populates="group")

class BillGroupIntermediary (db.Model):
    __tablename__ = 'group_user_intermediary'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))
    group_id = db.Column (db.Integer, db.ForeignKey('bill_groups.id'))
    # user = relationship("User", back_populates="bill_groups")
    # group = relationship("BillGroup", back_populates="bill_intermediaries")


class IndividualBill (db.Model):
    __tablename__ = 'individual_bill'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    bill_id = db.Column (db.Integer, db.ForeignKey('bill_groups.id'))
    bill_item = db.Column(db.String(255))

db.create_all()
