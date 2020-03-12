from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# database & migrations
migrate = Migrate()
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)