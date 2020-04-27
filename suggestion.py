from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField,RadioField
from wtforms.validators import InputRequired


class SuggestionForm(FlaskForm):
    character_id = RadioField('CharacterId', choices=[
    	(5, 'Mr.Green'),(2,'Mrs.Peacock'),(3,'Colonel Mustard'),(4,'Professor Plum'),(1,'Mrs.White'),(0,'Miss Scarlet')],
    	validators=[InputRequired()],coerce=int)
    weapon_id = RadioField('WeaponId', choices=[
    	(6, 'Wrench'),(7,'Candlestick'),(8,'Lead Pipe'),(9,'Rope'),(10,'Revolver'),(11,'Knife')],
    	validators=[InputRequired()],coerce=int)
    room_id = RadioField('RoomId', choices=[
		(19, 'Library'),(20,'Biliard Room'),(18,'Study'),(17,'hall'),(16,'Lounge'),(15,'Dining Room'),(13,'Ballroom'),(14,'Conservatory'),(12,'Kitchen')],
    	validators=[InputRequired()], coerce=int)
    is_accusation = BooleanField()