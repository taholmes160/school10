from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import main  # Import the main blueprint or app instance

@main.route('/')
@main.route('/home')
def home():
    if current_user.is_authenticated:
        print(f"User authenticated: {current_user.is_authenticated}")  # Debugging statement
        return redirect(url_for('main.dashboard'))
    return render_template('home.html')

@main.route('/dashboard')
@login_required
def dashboard():
    print("User authenticated:", current_user.is_authenticated)  # Debugging statement
    return render_template('dashboard.html')
