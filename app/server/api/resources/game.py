from flask import render_template, Blueprint, request, redirect, url_for

from app.server.domain.game_creator import GameCreator
from app.server.domain.game_runner import GameRunner
from app.server.domain.suggestion import Suggestion
from app.server.forms.move_form import MoveForm
from app.server.forms.suggestion import SuggestionForm

blueprint = Blueprint('pages', __name__, template_folder='../../../client/templates')

game_runner = None


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('pages/home.html')


@blueprint.route('/start-game', methods=['GET'])
def start_game():
    global game_runner
    number_of_players = 6
    created_game = GameCreator(number_of_players)

    game_runner = GameRunner(created_game.deck, created_game.envelope, created_game.players,
                             created_game.weapons, created_game.game_board_status)

    return redirect('/game')


@blueprint.route('/game', methods=['GET', 'POST'])
def game_board():
    move_form = MoveForm()
    suggestion_form = SuggestionForm()
    suggestion_message = None
    accusation_message = None
    card_value = None

    if request.method == 'POST':
        form = MoveForm(request.form)
        if form.validate() is True:
            x_coordinate = form.data['x_coordinate']
            y_coordinate = form.data['y_coordinate']

            game_runner.move_player(game_runner.current_player.id, x_coordinate, y_coordinate)
            game_runner.update_current_player()

        form = SuggestionForm(request.form)
        if form.validate() is True:
            character_id = form.data['character_id']
            weapon_id = form.data['weapon_id']
            room_id = form.data['room_id']
            is_accusation = form.data['is_accusation']

            character_card = game_runner.deck.get_card_data_by_id(character_id)
            weapon_card = game_runner.deck.get_card_data_by_id(weapon_id)
            room_card = game_runner.deck.get_card_data_by_id(room_id)
            suggestion = Suggestion(character_card, weapon_card, room_card)

            if is_accusation:
                player_won = game_runner.check_accusation(suggestion)
                if player_won:
                    accusation_message = "Congratulations! Your accusation was correct. You won!"
                else:
                    accusation_message = "Sorry, your accusation was incorrect. You lost."
                    game_runner.update_current_player()
            else:
                card_that_disproves_suggestion = game_runner.check_suggestion(suggestion)
                if card_that_disproves_suggestion is None:
                    suggestion_message = "No card disproves suggestion"
                else:
                    card_type = card_that_disproves_suggestion.type
                    card_value = card_that_disproves_suggestion.value
                    suggestion_message = "A %s card, \"%s\", disproves your suggestion." % (card_type, card_value)

    game_board = game_runner.game_board_status.board
    current_player = game_runner.current_player.id

    return render_template('pages/game_board.html', move_form=move_form, suggestion_form=suggestion_form,
                           game_board=game_board, current_player=current_player, suggestion_message=suggestion_message,
                           accusation_message=accusation_message, card_value=card_value)
