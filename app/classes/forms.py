# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher", "Teacher"), ("Student", "Student")])
    status = SelectField('Status', choices=[("Unavailable", "Unavailable"), ("Available", "Available")])

class jobiForm(FlaskForm):
    jobi = StringField("", validators=[DataRequired()])
    hours = IntegerField()
    dateneeded = StringField("", validators=[DataRequired()])
    location = StringField("", validators=[DataRequired()])
    level = StringField("", validators=[DataRequired()])
    description = StringField("", validators=[DataRequired()])
    post = SubmitField('Post')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')
    rate = SelectField('Rate', choices=[("1","1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
