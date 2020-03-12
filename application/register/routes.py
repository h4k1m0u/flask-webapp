from flask import Blueprint, render_template, url_for, redirect
from .forms import MyForm


register_bp = Blueprint('register', __name__,
                        template_folder='templates', static_folder='static')


@register_bp.route('/', methods=['GET', 'POST'])
def submit():
    form = MyForm()

    if form.validate_on_submit():
        return redirect(url_for('login.success'))

    return render_template('register/register.html', form=form)


@register_bp.route('/success')
def success():
    return render_template('register/success.html')
