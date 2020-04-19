from app.server.domain.deck import Deck
from app.server.domain.envelope import Envelope
from app.server.domain.game_board import GameBoard
from app.server.domain.player import Player


class GameCreator:
    # todo call this method in route
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.deck = Deck()
        self.envelope = Envelope()

        self.deck.shuffle()
        self.select_cards_for_envelope()
        self.players = self.create_players(number_of_players)

        # TODO this probably needs number of players
        self.game_board_status = GameBoard()

    def create_players(self, number_of_players):
        player_list = [None] * number_of_players
        chunked_cards = self.deck.chunk_cards(number_of_players)
        for i in range(number_of_players):  # TODO check to make sure number_of_players < 7
            player_list[i] = Player(i, 0, 0, chunked_cards[i]) # TODO figure out stating position for players
        return player_list

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
