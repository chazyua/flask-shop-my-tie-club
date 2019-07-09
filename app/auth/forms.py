
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User


class RegistrationForm(FlaskForm):
	firstname = StringField('First Name',validators=[DataRequired(), Length(max=20)])
	lastname = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	phonenumber = StringField('Phone Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError("This Email already in use")

	def validate_phone(self, phonenumber):
		user = User.query.filter_by(phonenumber=phonenumber.data).first()
		if user is not None:
			raise ValidationError("This phone # is already in use")

#general login form
class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')
