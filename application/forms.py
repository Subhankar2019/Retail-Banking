from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError



class LoginForm(FlaskForm):
    user_id= StringField("user_id", validators=[DataRequired(), Length(min=8)])
    password=PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Login")