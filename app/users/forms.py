from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User
# from flask_login import current_user

class CartForm(FlaskForm):
	quantity = IntegerField('1', validators=[DataRequired()])
	submit = SubmitField('Submit')


class ShippingForm(FlaskForm):
    address1 = StringField('Primary Address',validators=[DataRequired()]) 
    address2 = StringField('Secondary Address', validators=[DataRequired()])
    postcode = IntegerField('Postal code', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RequestResetForm(FlaskForm):
	email = StringField('Email Address', validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError("There is no account associated with this email")


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
	confirm = PasswordField('Password Again', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset')
