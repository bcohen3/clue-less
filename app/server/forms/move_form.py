from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired


class MoveForm(FlaskForm):
    x_coordinate = IntegerField(validators=[InputRequired()])
    y_coordinate = IntegerField(validators=[InputRequired()])
