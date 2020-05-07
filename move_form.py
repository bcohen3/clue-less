from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms.validators import InputRequired

class MoveForm(FlaskForm):
    player_id = StringField(validators=[InputRequired()])
    room = StringField(validators=[InputRequired()])
    hall = StringField(validators=[InputRequired()])