from models import User, db
from werkzeug.security import generate_password_hash

def set_default_password():
    users = User.query.all()
    default_password = 'school@1234'
    for user in users:
        user.set_password(default_password)
    db.session.commit()
