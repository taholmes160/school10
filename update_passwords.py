from app import create_app
from models import User, db

# Create the Flask app and push an application context
app = create_app()
app.app_context().push()

# Define the hash_passwords function to update the password hashes
def hash_passwords():
    users = User.query.all()
    for user in users:
        user.set_password(user.password)
        db.session.add(user)
    db.session.commit()

# Call the hash_passwords function to update the password hashes
hash_passwords()
