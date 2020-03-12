**Project structure:** [Tutorial series](https://hackersandslackers.com/flask-application-factory/)

## Prerequisites
- **Flask-WTF:** `pip install flask-wtf`
- **Flask-SQLAlchemy:** `pip install flask-sqlalchemy`
- **Flask-Migrate:** `pip install flask-migrate`

## Database migrations
0. **Define environment variable:** `export FLASK_APP=main.py`
1. `flask db init`
2. `flask db migrate -m "message"`
3. `flask db upgrade`
