from flask_wtf import FlaskForm
#from wtforms import IntegerField
from wtforms import RadioField
from wtforms.validators import InputRequired


class MoveForm(FlaskForm):
	player_id = RadioField('PlayerId', choices=[
		(1, 'Player 1'),(2,'Player 2'),(3,'Player 3'),(4,'Player 4'),(5,'Player 5'),(6,'Player 6')],
		validators=[InputRequired()], coerce=int)
	r_Select = RadioField('RSelect', choices=[
		(19, 'Library'),(20,'Biliard Room'),(18,'Study'),(17,'hall'),(16,'Lounge'),(15,'Dining Room'),(13,'Ballroom'),(14,'Conservatory'),(12,'Kitchen')],
		validators=[InputRequired()], default=1, coerce=int)
"""
	y_coordinate = RadioField('Room Y', choices=[
		(1, 'Library'),(2,'Office')],
		validators=[InputRequired()], default=1, coerce=int)
"""