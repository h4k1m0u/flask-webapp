from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from .forms import UploadForm
from werkzeug.utils import secure_filename
import os


file_bp = Blueprint('file', __name__,
                    template_folder='templates', static_folder='static')


@file_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        # get file from form
        f = form.photo.data
        filename = secure_filename(f.filename)

        # save file inside instance folder
        f.save(os.path.join(app.instance_path, 'photos', filename))

        return redirect(url_for('.success'))

    return render_template('file/upload.html', form=form)


@file_bp.route('/success')
def success():
    return render_template('file/success.html')
