from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField(
        'Email',
        validators=[Email(message='Not a valid email address.'),
                    DataRequired()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField(
        'Repeat Password',
        validators=[EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')
