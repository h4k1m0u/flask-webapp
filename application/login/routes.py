from flask import Blueprint


login_bp = Blueprint('blueprint', __name__,
                     template_folder='templates', static_folder='static')


@login_bp.route('/')
def index():
    return 'This is an example app'
