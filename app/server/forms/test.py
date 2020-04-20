from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, AnyOf


class TestForm(FlaskForm):
    test = TextField(
        validators=[DataRequired(), AnyOf(['left', 'right', 'up', 'down'])]
    )
