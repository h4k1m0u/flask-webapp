from flask import Flask
from .auth import routes as auth_routes
from .auth.routes import login_manager
from .file import routes as file_routes
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
    app.register_blueprint(auth_routes.auth_bp, url_prefix='/auth')
    app.register_blueprint(file_routes.file_bp, url_prefix='/file')

    # intialize extensions (database, migration, auth)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app, db)

    return app
