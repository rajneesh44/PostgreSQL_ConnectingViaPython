from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import *
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    """Username and password Checker"""
    username_entered = form.username.data
    password_entered = field.data

    #Checking username is valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("username or password is incorrect")
    #"""This is used for without hash passwords"""
    #elif password_entered != user_object.password:
    #     raise ValidationError("Username is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or password is incorrect")



class RegistrationForm(FlaskForm):
    """Registration form"""

    username = StringField('username_label', validators=[InputRequired(message="Username Required"),
                                                         Length(min=4, max=25, message="Username must be b/w 4 and 25")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password Required"),
                                                           Length(min=4, max=25, message="Password must be b/w 4 and 25")])
    confirm_pwd = PasswordField('confirm_label', validators=[InputRequired(message="Confirm password Required"),
                                                             EqualTo('password', message="passwords mus match")])
    submit_button = SubmitField('create')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already Exists")


class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('username_label', validators=[InputRequired(message="Username Required")])

    password = PasswordField('password_label', validators=[InputRequired(message="Password Required"),
                                                           invalid_credentials])
    submit_button = SubmitField('Login')