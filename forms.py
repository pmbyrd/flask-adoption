from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, Length

class PetForm(FlaskForm):
    """Creates an instance of a form for our pets in the database"""
    name = StringField("Pet Name", validators=[InputRequired(message="Please provide a name for the Pet")])
    species = StringField("Species", validators=[InputRequired(message="Please provide a species")])
    photo_url= StringField("Photo URL Link", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), Length(min=0, max=30, message="Age must be between 0-30")])
    notes = TextAreaField("Any notes or stories you wish to share", validators=[Optional()])
    is_available = BooleanField("Availble")