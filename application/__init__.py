from flask import Flask
from .login import routes as login_routes


def create_app():
    """
    Application factory.
    """
    app = Flask(__name__, instance_relative_config=True)

    # configuration file inside instance folder
    app.config.from_pyfile('config.py')

    # register blueprints
    app.register_blueprint(login_routes.login_bp)
    print('Path:', app.instance_path)

    return app
