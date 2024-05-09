from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy ORM
db = SQLAlchemy()

# Define a simple User model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

# You can define other models here following the same pattern
