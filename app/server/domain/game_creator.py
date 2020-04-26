from collections import namedtuple

from app.server.domain.deck import Deck
from app.server.domain.envelope import Envelope
from app.server.domain.game_board import GameBoard
from app.server.domain.game_piece import GamePiece
from app.server.domain.player import Player


class GameCreator:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.deck = Deck()
        self.envelope = Envelope()
        self.game_board_status = GameBoard()
        Point = namedtuple('Point', 'x_coordinate y_coordinate')
        #self.player_starting_indices = [Point(7, 1), Point(7, 9), Point(1, 7), Point(9, 3), Point(1, 3), Point(3, 9)]

        #Mrs White; Mr. Green; Mrs. Peacock; Professor Plum; Miss Scarlet; Colonel Mustard
        self.player_starting_indices = [Point(8, 12), Point(4, 12), Point(0, 8),
                                        Point(0, 4), Point(8, 0), Point(12, 4)]

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
        weapon_list = [None] * 6
        end_index = self.number_of_players + 6

        weapon_list_index = 0
        for i in range(self.number_of_players, end_index):
            weapon_list[weapon_list_index] = GamePiece(i, 0, 0)
            weapon_list_index += 1

        return weapon_list

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
