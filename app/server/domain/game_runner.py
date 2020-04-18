from app.server.domain.deck import Deck
from app.server.domain.game_board import GameBoard
from app.server.domain.player import Player


class GameRunner:
    playerList = []
    currentPlayerTurn = Player()
    gameBoardStatus = GameBoard()
    deck = Deck()

    @staticmethod
    def test_method():
        return True
