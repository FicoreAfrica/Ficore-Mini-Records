from flask import Blueprint

transactions_bp = Blueprint('transactions', __name__, template_folder='templates')

from .routes import *
