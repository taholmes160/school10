# main/routes.py

from flask import render_template, redirect, url_for
from flask_login import current_user
from . import main  # Import the main blueprint or app instance

@main.route('/')
@main.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')