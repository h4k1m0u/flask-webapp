**Project structure:** [Tutorial series](https://hackersandslackers.com/flask-application-factory/)

# Usage & defined routes
----------------
```bash
python main.py
```

- **Login:** `/auth/login`
- **Logout:** `/auth/logout`
- **Profile:** `/auth/profile`
- **Register:** `/auth/register`
- **Upload:** `/file/upload`

# Prerequisites
---------------
- **Flask-WTF:** `pip install flask-wtf`
- **Flask-SQLAlchemy:** `pip install flask-sqlalchemy`
- **Flask-Migrate:** `pip install flask-migrate`
- **Flask-Login:** `pip install flask-login`

# Database migrations
----------------------
0. **Define environment variable:** `export FLASK_APP=main.py`
1. `flask db init`
2. `flask db migrate -m "message"`
3. `flask db upgrade`

# Deployment
------------
An `instance` folder needs to be created at the root of the project to contain database access credentials. For that, `instance/config.py` will have to contain:

```python
import os


# needed by csrf field in wtforms & user passwords)
SECRET_KEY = os.urandom(32)

# database access
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@<host>/<database>"
```

The files uploaded through this web application should also be placed inside the `instance` folder (e.g. inside a photos subdirectory).
