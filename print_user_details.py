from models import User, db
from app import create_app

# Create the Flask app and push an application context
app = create_app()
app.app_context().push()

# Query the database for the user with the username 'stu2024001'
user = User.query.filter_by(username='stu2024001').first()

# Print out the user details
print(f"Username: {user.username}")
print(f"Email: {user.email}")
print(f"Password hash: {user.password_hash}")
# Print out other user details as needed
