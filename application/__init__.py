from flask import Flask
from .login import routes as login_routes
from .register import routes as register_routes
from .models import db, migrate, User


def create_app():
    """
    Application factory.

    Returns:
        app(flask.app.Flask)
    """
    app = Flask(__name__, instance_relative_config=True)

    # configuration files (2nd: private & inside instance folder)
    app.config.from_object('application.config')
    app.config.from_pyfile('config.py')

    # register blueprints
    app.register_blueprint(login_routes.login_bp, url_prefix='/login')
    app.register_blueprint(register_routes.register_bp, url_prefix='/register')

    # intialize database & migration
    db.init_app(app)
    migrate.init_app(app, db)

    return app
