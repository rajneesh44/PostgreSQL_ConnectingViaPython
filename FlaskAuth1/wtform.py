from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import *


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
