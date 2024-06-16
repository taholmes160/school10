from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
