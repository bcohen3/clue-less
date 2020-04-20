from flask import render_template, Blueprint, request

from app.server.domain.deck import Deck
from app.server.domain.game_creator import GameCreator
from app.server.domain.game_runner import GameRunner
from app.server.domain.suggestion import Suggestion
from app.server.forms.move_form import MoveForm
from app.server.forms.test import TestForm

blueprint = Blueprint('pages', __name__, template_folder='../../../client/templates')

game_runner = None


@blueprint.route('/game-board', methods=['GET', 'POST'])
def home():
    move_form = MoveForm(request.form)
    test_form = TestForm(request.form)
    entered_move = None

    if request.method == 'POST':
        if 'move' in request.form:
            entered_move = 'move'
            move_form = MoveForm(request.form)

        if 'test' in request.form:
            entered_move = 'test'
            test_form = TestForm(request.form)

            # form = TestForm(request.form)

        # if form.validate() is not True:
        #     print(form.errors)
        #     return render_template('pages/game_board.html', form=form)
        #
        # entered_move = form.data['move']

    return render_template('pages/game_board.html', move_form=move_form, test_form=test_form, move=entered_move)


@blueprint.route('/new-game', methods=['POST'])
def start_game():
    global game_runner
    number_of_players = request.json['number_of_players']
    created_game = GameCreator(number_of_players)

    game_runner = GameRunner(created_game.deck, created_game.envelope, created_game.players,
                             created_game.weapons, created_game.game_board_status)
    game_board = game_runner.game_board_status

    return render_template('pages/GameUI.html', form=form, game_board=game_board)


@blueprint.route('/move-player', methods=['POST'])
def move_player():
    player_id = request.json['playerId']
    x_coordinate = request.json['xCoordinate']
    y_coordinate = request.json['yCoordinate']

    game_runner.move_player(player_id, x_coordinate, y_coordinate)
    game_runner.update_current_player()
    game_board = game_runner.game_board_status

    return render_template('pages/home.html', game_board=game_board)


@blueprint.route('/move-weapon', methods=['POST'])
def move_weapon():
    weapon_id = request.json['weaponId']
    x_coordinate = request.json['xCoordinate']
    y_coordinate = request.json['yCoordinate']

    game_runner.move_weapon(weapon_id, x_coordinate, y_coordinate)
    game_board = game_runner.game_board_status

    return render_template('pages/home.html', game_board=game_board)


@blueprint.route('/make-suggestion', methods=['POST'])
def make_suggestion():
    character_id = request.json['characterId']
    weapon_id = request.json['weaponId']
    room_id = request.json['roomNameId']

    deck = Deck()
    character_card = deck.get_card_data_by_id(character_id)
    weapon_card = deck.get_card_data_by_id(weapon_id)
    room_card = deck.get_card_data_by_id(room_id)

    suggestion = Suggestion(character_card, weapon_card, room_card)

    card = game_runner.check_suggestion(suggestion)
    game_board = game_runner.game_board_status

    return render_template('pages/home.html', card=card, game_board=game_board)


@blueprint.route('/make-accusation', methods=['POST'])
def make_accusation():
    character_id = request.json['characterId']
    weapon_id = request.json['weaponId']
    room_id = request.json['roomNameId']

    deck = Deck()
    character_card = deck.get_card_data_by_id(character_id)
    weapon_card = deck.get_card_data_by_id(weapon_id)
    room_card = deck.get_card_data_by_id(room_id)

    suggestion = Suggestion(character_card, weapon_card, room_card, True)

    player_won = game_runner.check_accusation(suggestion)
    game_board = game_runner.game_board_status

    return render_template('pages/home.html', palyer_won=player_won, game_board=game_board)
