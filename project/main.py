from flask import Blueprint, render_template
from flask_login import current_user, login_required
# 
from sqlalchemy import (Column, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from project.models import BillGroupIntermediary, BillGroups

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
    user_id = current_user.id
    user_groups = BillGroupIntermediary.query.filter_by(user_id=user_id).all()
    user_group_ids = [group.group_id for group in user_groups]
    groups = BillGroups.query.all()
    return render_template('groups.html', groups=groups, user_group_ids=user_group_ids)