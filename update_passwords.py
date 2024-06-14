from app import create_app
from models import User, db
from werkzeug.security import generate_password_hash

# Create the Flask app and push an application context
app = create_app()
app.app_context().push()

# Define the hash_passwords function to update the password hashes
def hash_passwords():
    users = User.query.all()
    for user in users:
        hashed_password = generate_password_hash('school@1234', method='scrypt', salt_length=16)
        user.password_hash = hashed_password
        db.session.add(user)
    db.session.commit()

# Call the hash_passwords function to update the password hashes
hash_passwords()
