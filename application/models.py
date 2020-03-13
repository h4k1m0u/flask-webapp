from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash


# database & migrations
migrate = Migrate()
db = SQLAlchemy()


class User(UserMixin, db.Model):
    """
    User authentication
    source: https://hackersandslackers.com/flask-login-user-authentication/
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """
        Used during registration
        """
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """
        Used on login
        """
        return check_password_hash(self.password, password)
