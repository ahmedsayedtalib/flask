from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of the Car:- ')
    submit = SubmitField('Click to Add')

class DelForm(FlaskForm):
    id = IntegerField('ID Number to delete:- ')
    submit = SubmitField('Submit to delete form')