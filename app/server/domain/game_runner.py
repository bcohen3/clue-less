from app.server.domain.deck import Deck
from app.server.domain.envelope import Envelope
from app.server.domain.game_board import GameBoard
from app.server.domain.player import Player


class GameRunner:
    def __init__(self, deck, envelope, player_list, weapon_list, game_board):
        self.deck = deck
        self.envelope = envelope
        self.player_list = player_list
        self.weapon_list = weapon_list
        self.current_player = player_list[0]
        self.game_board_status = game_board

    def check_suggestion(self, suggestion):
        suggestion_cards = suggestion.get_card_ids()

        for player in self.player_list:
            player_card_ids = player.get_card_ids()
            card_ids = [i for i in suggestion_cards if i in player_card_ids]

            if len(card_ids) > 0:
                return self.deck.get_card_data_by_id(card_ids[0])

    def check_accusation(self, accusation):
        if set(accusation.get_card_ids()) == set(self.envelope.get_card_ids()):
            self.current_player.is_winner = True
        else:
            self.current_player.is_loser = True

        return self.current_player.is_winner

    # TODO add move player validation
    def validatePlayerMove(self):
        return True

    def move_player(self, palyer_id, x_coordinate, y_coordinate):
        if self.validatePlayerMove() is True:
            # TODO make current position blank with currentPlayerTurn.x_coordinate and currentPlayerTurn.y_coordinate
            self.current_player.x_coordinate = x_coordinate
            self.current_player.y_coordinate = y_coordinate
            # TODO update current position with currentPlayerTurn.x_coordinate and currentPlayerTurn.y_coordinate
            self.update_current_player()

    # TODO add move weapon validation
    def validate_weapon_move(self):
        return True

    def get_weapon_by_id(self, weapon_id):
        for weapon in self.weapon_list:
            if weapon.id == weapon_id:
                return weapon

    def move_weapon(self, weapon_id, x_coordinate, y_coordinate):
        if self.validate_weapon_move() is True:
            weapon = self.get_weapon_by_id(weapon_id)
            # TODO make current position blank with weapon.x_coordinate and weapon.y_coordinate
            weapon.x_coordinate = x_coordinate
            weapon.y_coordinate = y_coordinate
            # TODO update current position with weapon.x_coordinate and weapon.y_coordinate

    def update_current_player(self):
        current_player_id = self.current_player.id
        next_player_id = current_player_id + 1

        while self.player_list[next_player_id].is_loser is True:
            next_player_id += 1

        self.current_player = self.player_list[next_player_id]
