from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask import current_app as app
from flask_login import LoginManager, login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm
from ..models import User, db


auth_bp = Blueprint('auth', __name__,
                    template_folder='templates', static_folder='static')


# view to redirect to for anonymous users
login_manager = LoginManager()
login_manager.login_view = '.login'


@login_manager.user_loader
def load_user(id):
    """
    Get connected user from session on each page request.
    """
    return User.query.get(id)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # get user details from form
        email = form.email.data
        password = form.password.data

        # login if user in database
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)

            # redirect to targeted page in url
            next_page = request.args.get('next')
            return redirect(next_page or url_for('.success'))

        flash('Invalid email/password combination')
        return redirect(url_for('.login'))

    return render_template('auth/login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # get user details from form
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # create a new user if not already in database
        user_existing = User.query.filter_by(email=email).first()

        if user_existing is None:
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('.success'))

        flash('A user already exists with the same email address')
        return redirect(url_for('.register'))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/success')
def success():
    return render_template('auth/success.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')
