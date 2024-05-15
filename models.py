from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Initialize the SQLAlchemy ORM
db = SQLAlchemy()

# Define the Role model
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))

    # Relationship to the User model
    users = db.relationship('User', back_populates='role')

    def __repr__(self):
        return '<Role %r>' % self.name

# Define a User model with additional fields
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # Foreign key to the roles table
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Additional profile information
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    profile_picture = db.Column(db.String(255))
    bio = db.Column(db.Text)

    # Contact information
    phone_number = db.Column(db.String(15), unique=True, nullable=True)

    # Security and privacy
    last_login_at = db.Column(db.DateTime, nullable=True)
    login_attempts = db.Column(db.Integer, default=0)
    password_reset_token = db.Column(db.String(100), nullable=True)
    password_reset_expiration = db.Column(db.DateTime, nullable=True)

    # Preferences
    language = db.Column(db.String(10), nullable=True)
    timezone = db.Column(db.String(50), nullable=True)

    # Status and flags
    is_admin = db.Column(db.Boolean, default=False)
    deactivated_at = db.Column(db.DateTime, nullable=True)

    # Relationship to the Role model
    role = db.relationship('Role', back_populates='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

# You can define other models here following the same pattern
