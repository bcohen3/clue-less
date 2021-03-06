from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField
from wtforms.validators import InputRequired


class SuggestionForm(FlaskForm):
    character_id = IntegerField(validators=[InputRequired()])
    weapon_id = IntegerField(validators=[InputRequired()])
    room_id = IntegerField(validators=[InputRequired()])
    is_accusation = BooleanField()