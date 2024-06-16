from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from auth.routes import auth as auth_blueprint
from users.users_blueprint import users_blueprint
from main.routes import main as main_blueprint
from werkzeug.security import generate_password_hash
from models import db, User

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(users_blueprint, url_prefix='/users')
    app.register_blueprint(main_blueprint, url_prefix='/')

    @app.route('/')
    def home():
        return render_template('home.html')

    def hash_passwords():
        users = User.query.all()
        for user in users:
            user.set_password(user.password)
            db.session.add(user)
        db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        hash_passwords()
    app.run(debug=True)
