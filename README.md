**Project structure:** [Tutorial series](https://hackersandslackers.com/flask-application-factory/)

# Usage & defined routes
```bash
python main.py
```

- **Login:** `/auth/login`
- **Logout:** `/auth/logout`
- **Profile:** `/auth/profile`
- **Register:** `/auth/register`
- **Upload:** `/file/upload`

# Prerequisites
The python packages needed to run the webapp can be installed with:

```bash
pip install -r requirements.txt
```

# Database migrations
[flask-migrate] is an extension based on Alembic, a migrations tool for SQLAlchemy. The following instructions use it to first add a `migrations` folder at the root of the project, then to create a new migration and finally apply it:

0. **Define environment variable:** `export FLASK_APP=main.py`
1. `flask db init`
2. `flask db migrate -m "message"`
3. `flask db upgrade`

[flask-migrate]: https://flask-migrate.readthedocs.io/en/latest/

# Deployment
An `instance` folder needs to be created at the root of the project to contain database access credentials. For that, `instance/config.py` will have to contain:

```python
import os


# needed by csrf field in wtforms & user passwords)
SECRET_KEY = os.urandom(32)

# database access
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@<host>/<database>"
```

If the password of the user used to login to pgadmin4 was forgotten, it can be reset with:

```sql
ALTER USER user_name WITH PASSWORD 'new_password';
```

The files uploaded through this web application should also be placed inside the `instance` folder (e.g. inside a photos subdirectory).

# Docker
The docker image was deployed on the [docker-hub]. The following commands were used to build and tag the image, and deploy it to the hub:

```bash
docker build -t <hub-user>/<repo-name> .
docker login
docker push <hub-user>/<repo-name>
```

To download the image on another machine:

```bash
docker run <hub-user>/<repo-name>
```

[docker-hub]: https://hub.docker.com/r/h4k1m0u/flask
