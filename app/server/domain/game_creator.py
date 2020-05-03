from collections import namedtuple

from app.server.domain.deck import Deck
from app.server.domain.envelope import Envelope
from app.server.domain.game_board import GameBoard
from app.server.domain.game_piece import GamePiece
from app.server.domain.player import Player
from app.server.domain.weapon import Weapon


class GameCreator:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.deck = Deck()
        self.envelope = Envelope()
        self.game_board_status = GameBoard()
        Point = namedtuple('Point', 'x_coordinate y_coordinate')

        #Miss Scarlet; Colonel Mustard; Mrs White; Mr. Green; Mrs. Peacock; Professor Plum
        self.player_starting_indices = [Point(8, 0), Point(12, 4), Point(8, 12),
                                        Point(4, 12), Point(0, 8), Point(0, 4)]

        #wrench; candlestick; lead pipe; rope; revolver; knife
        self.weapon_starting_indices = [Point(0, 14), Point(1, 14), Point(2, 14),
                                        Point(3, 14), Point(4, 14), Point(5, 14)]

        self.deck.shuffle()
        self.select_cards_for_envelope()
        self.players = self.create_players(number_of_players)
        self.weapons = self.create_weapons()

    def create_players(self, number_of_players):
        player_list = [None] * number_of_players
        chunked_cards = self.deck.chunk_cards(number_of_players)
        for i in range(number_of_players):
            point = self.player_starting_indices[i]
            player_list[i] = Player(i, point.x_coordinate, point.y_coordinate, chunked_cards[i])

        self.add_players_to_board(player_list)
        return player_list

    def add_players_to_board(self, players):
        for player in players:
            self.game_board_status.board[player.y_coordinate][player.x_coordinate] = player.id

    def create_weapons(self):
        chunked_cards = self.deck.chunk_cards(self.number_of_players)
        weapon_list = [None] * 6
        end_index = self.number_of_players + 6

        weapon_list_index = 0
        for i in range(self.number_of_players, end_index):
            point = self.weapon_starting_indices[weapon_list_index]
            weapon_list[weapon_list_index] = Weapon(i, point.x_coordinate, point.y_coordinate, chunked_cards[weapon_list_index])
            weapon_list_index += 1

        self.add_weapons_to_board(weapon_list)
        return weapon_list

    def add_weapons_to_board(self, weapons):
        counter = 0

        for weapon in weapons:
            self.game_board_status.board[14][counter] = weapon.id
            counter += 1

    def select_cards_for_envelope(self):
        for card in self.deck.cards:
            if card.type == 'suspect' and self.envelope.suspect_card is None:
                self.envelope.suspect_card = card
                list.remove(self.deck.cards, card)
            elif card.type == 'weapon' and self.envelope.weapon_card is None:
                self.envelope.weapon_card = card
                list.remove(self.deck.cards, card)
            elif card.type == 'room' and self.envelope.room_card is None:
                self.envelope.room_card = card
                list.remove(self.deck.cards, card)
