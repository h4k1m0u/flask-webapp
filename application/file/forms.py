from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileRequired(), FileAllowed(['jpg', 'png'], 'Jpg or png images only')])
    submit = SubmitField('Upload')
