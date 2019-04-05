from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from src.flaskbasic.models import Student, Users

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        # if user is not None:
        #     raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')



class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    physics = IntegerField('Physics',validators=[DataRequired()])
    maths = IntegerField('Maths', validators=[DataRequired()])
    chemistry = IntegerField('Chemistry', validators=[DataRequired()])
    submit = SubmitField('Submit')


# IntegerField('Telephone', [validators.NumberRange(min=0, max=10)])
