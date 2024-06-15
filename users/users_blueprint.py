from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from models import User, Role

# Create a Blueprint for user-related routes
users_blueprint = Blueprint('users', __name__, template_folder='templates')

# Define a route to list all users by role
@users_blueprint.route('/users-by-role')
@login_required
def users_by_role():
    # Only users with the 'admin' role and above can access this view
    allowed_roles = ['admin', 'principal', 'vice principal']
    if current_user.role.name not in allowed_roles:
        abort(403)  # Return a 403 Forbidden error if the user does not have an allowed role

    # Query all roles and their associated users
    roles = Role.query.all()
    users_by_role = {}
    for role in roles:
        users = User.query.filter_by(role_id=role.id).all()
        users_by_role[role.name] = users

    # Render the users-by-role view
    return render_template('users-by-role.html', users_by_role=users_by_role)
