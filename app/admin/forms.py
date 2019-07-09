from flask_wtf import FlaskForm
from wtforms import ( StringField, SubmitField,TextAreaField,IntegerField,
FloatField, validators, RadioField
)
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import photos
from app.models import Categories

class CategoriesForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	image = FileField('Category Image', validators=[FileRequired(), FileAllowed(photos, "images only")])
	submit = SubmitField('Submit')


class ProductsForm(FlaskForm):
	categories = QuerySelectField(query_factory=lambda: Categories.query.all(),
	get_label="category_name")
	name = StringField('Name', validators=[DataRequired()])
	price =IntegerField('Price', validators=[DataRequired()])
	image = FileField('Picture', validators=[FileRequired(), FileAllowed(photos, "images only")])
	stock = IntegerField('Stock', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')


class Variations(FlaskForm):
    sizes = RadioField('Sizes',validators=[DataRequired(message="select a product size")],
    choices=[('Small','S'),('Medium','M'),('Large','L'),('Extra Large','XL')])
    submit =SubmitField('Add to Cart')

