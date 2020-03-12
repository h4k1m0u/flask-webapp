from flask import Blueprint, render_template, url_for, redirect
from .forms import MyForm


login_bp = Blueprint('login', __name__,
                     template_folder='templates', static_folder='static')


@login_bp.route('/', methods=['GET', 'POST'])
def submit():
    form = MyForm()

    if form.validate_on_submit():
        return redirect(url_for('.success'))

    return render_template('login/login.html', form=form)


@login_bp.route('/success')
def success():
    return render_template('login/success.html')
