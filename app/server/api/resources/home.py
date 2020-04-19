from flask import render_template, Blueprint, request

from app.server.domain.game_creator import GameCreator
from app.server.domain.game_runner import GameRunner

blueprint = Blueprint('pages', __name__, template_folder='../../../client/templates')


class GlobalGameRunner:
    game_runner = GameRunner()


global_game_runner = GlobalGameRunner()


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('pages/home.html', form=request.json)


@blueprint.route('/new-game', methods=['POST'])
def start_game():
    number_of_players = request.json['number_of_players']
    created_game = GameCreator(number_of_players)

    global_game_runner.game_runner = GameRunner(created_game.deck, created_game.envelope, created_game.players,
                                                created_game.weapons, created_game.game_board_status)
    game_board = global_game_runner.game_runner.game_board_status

    return render_template('pages/home.html', game_board=game_board)


@blueprint.route('/move-player', methods=['POST'])
def move_player():
    player_id = request.json['playerId']
    x_coordinate = request.json['xCoordinate']
    y_coordinate = request.json['yCoordinate']

    is_valid = global_game_runner.game_runner.move_player(player_id, x_coordinate, y_coordinate)

    return render_template('pages/home.html', is_valid=is_valid)


@blueprint.route('/move-weapon', methods=['POST'])
def move_weapon():
    weapon_id = request.json['playerId']
    x_coordinate = request.json['xCoordinate']
    y_coordinate = request.json['yCoordinate']

    is_valid = global_game_runner.game_runner.move_weapon(weapon_id, x_coordinate, y_coordinate)

    return render_template('pages/home.html', is_valid=is_valid)
