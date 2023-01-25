from flask import Blueprint, render_template
from flask_login import current_user, login_required
# 
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
# 
engine = create_engine('sqlite:///db.sqlite')

Session = sessionmaker(bind=engine)
session = Session()
# 
from . import db



main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/groups')
@login_required
def groups():
    return render_template('groups.html', name=current_user.name)