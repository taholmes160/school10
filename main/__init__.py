from flask import Blueprint

main = Blueprint('main', __name__)

from . import routes  # Import routes to register them with the blueprint
