from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(f"Trying to log in with username: {username}")  # Debugging statement
        
        user = User.query.filter_by(username=username).first()

        if user:
            print(f"User found: {user.username}")  # Debugging statement
        else:
            print("User not found")  # Debugging statement

        if user and user.check_password(password):
            print("Password matches")  # Debugging statement
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        else:
            print("Login failed")  # Debugging statement
            flash('Login failed. Check your credentials and try again.')

    return render_template('login.html')
