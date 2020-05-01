from flask_wtf import FlaskForm
#from wtforms import IntegerField
from wtforms import RadioField
from wtforms.validators import InputRequired


class MoveForm(FlaskForm):
	player_id = RadioField('Select Player', choices=[
		(1, 'Player 1'),(2,'Player 2'),(3,'Player 3'),(4,'Player 4'),(5,'Player 5'),(6,'Player 6')],
		validators=[InputRequired()], coerce=int)
	r_Select = RadioField('Select Room', choices=[
		(19, 'Library'),(20,'Biliard Room'),(18,'Study'),(17,'hall'),(16,'Lounge'),(15,'Dining Room'),(13,'Ballroom'),(14,'Conservatory'),(12,'Kitchen')],
		validators=[InputRequired()], default=1, coerce=int)
		#add hallway 
	h_Select=RadioField('Select Hallway', choices=[
		(21, 'Hallway between Study and Hall'),(22,'Hallway between Hall and Lounge'),(23,'Hallway between Study and Library'),
		(24,'Hallway between Library and Billiard Room'),(25,'Hallway between Hall and Billiard Room'),(26,'Hallway between Billiard Room and Dining Room'),
		(27,'Hallway between Lounge and Dining Room'),(28,'Hallway between Library and Conservatory'),(29,'Hallway between Billiard Room and Ballroom'),
		(30,'Hallway between Dining Room and Kitchen'),(31,'Hallway between Conservartory and Ballroom'),(32,'Hallway between Ballroom and Kitchen')],
		validators=[InputRequired()], default=1, coerce=int)
		
"""if form.validate_on_submit():
    player_id = form.player_id.data
    form.player_id.data = ''
	
	return render_template('game_board.html', form=form, player_id=player_id)
"""		
			
		
