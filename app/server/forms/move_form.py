from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, AnyOf


class MoveForm(FlaskForm):
    move = TextField(
        validators=[DataRequired(), AnyOf(['left', 'right', 'up', 'down'])]
    )
