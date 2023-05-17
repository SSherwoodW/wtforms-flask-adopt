from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf, Length


class PetForm(FlaskForm):
    """Form for adding a new pet."""
    name = StringField(
        "Pet Name", 
        validators=[InputRequired(message="Pet name must be provided.")]
        )
    species = StringField(
        "Pet Species", 
        validators=[InputRequired(message="Pet species must be provided."), 
                    AnyOf(['dog', 'cat', 'porcupine'], message='Accepted species: dog, cat, porcupine.')]
                    )
    photo_url = StringField(
        "Photo URL", 
        validators=[Optional(), 
                    URL(require_tld=True, message="Please provide a valid URL address.")]
                    )
    age = IntegerField(
        "Pet Age", 
        validators=[Optional(), 
                    NumberRange(min=0, max=30, message="Age must be a number between 0 and 30.")]
                    )
    notes = StringField(
        "Other Information", 
        validators=[Optional()]
        )
    

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )

    available = BooleanField("Available?")