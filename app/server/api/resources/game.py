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
    card = None
    suggestion_message = None

    if request.method == 'POST':
        form = MoveForm(request.form)
        if form.validate() is True:
            player_id = form.data['player_id']
            x_coordinate = form.data['x_coordinate']
            y_coordinate = form.data['y_coordinate']

            game_runner.move_player(player_id, x_coordinate, y_coordinate)
            game_runner.update_current_player()

        form = SuggestionForm(request.form)
        if form.validate() is True:
            character_id = form.data['character_id']
            weapon_id = form.data['weapon_id']
            room_id = form.data['room_id']

            character_card = game_runner.deck.get_card_data_by_id(character_id)
            weapon_card = game_runner.deck.get_card_data_by_id(weapon_id)
            room_card = game_runner.deck.get_card_data_by_id(room_id)
            suggestion = Suggestion(character_card, weapon_card, room_card)

            card_that_disproves_suggestion = game_runner.check_suggestion(suggestion)
            if card_that_disproves_suggestion is None:
                suggestion_message = "No card disproves suggestion"
            else:
                card_type = card_that_disproves_suggestion.type
                card_value = card_that_disproves_suggestion.value
                suggestion_message = "A %s card, \"%s\", disproves your suggestion." % (card_type, card_value)

    game_board = game_runner.game_board_status.board

    return render_template('pages/game_board.html', move_form=move_form, suggestion_form=suggestion_form,
                           game_board=game_board, card=card, suggestion_message=suggestion_message)


@blueprint.route('/make-accusation', methods=['POST'])
def make_accusation():
    character_id = request.json['characterId']
    weapon_id = request.json['weaponId']
    room_id = request.json['roomNameId']

    character_card = game_runner.deck.get_card_data_by_id(character_id)
    weapon_card = game_runner.deck.get_card_data_by_id(weapon_id)
    room_card = game_runner.deck.get_card_data_by_id(room_id)

    suggestion = Suggestion(character_card, weapon_card, room_card, True)

    player_won = game_runner.check_accusation(suggestion)
    game_board = game_runner.game_board_status

    return render_template('pages/home.html', palyer_won=player_won, game_board=game_board)
