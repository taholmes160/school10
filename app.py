from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User
from auth import auth as auth_blueprint  # Import the auth Blueprint

<<<<<<< HEAD
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Update the login view to point to the 'login' route within the 'auth' Blueprint

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint, url_prefix='/auth', template_folder='auth/templates')  # Register the auth Blueprint with a URL prefix and the correct template folder

    @app.route('/')
    def home():
        return render_template('home.html')  # Your home template

    # Run the Flask app
    return app

if __name__ == '__main__':
    app = create_app()
=======
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Update the login view to point to the 'login' route within the 'auth' Blueprint

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Register the auth Blueprint with a URL prefix

@app.route('/')
def home():
    return render_template('home.html')  # Your home template

# Run the Flask app
if __name__ == '__main__':
>>>>>>> ea6a09c853f7d6b23819e93dc7875e99e3c35beb
    app.run(debug=True)
