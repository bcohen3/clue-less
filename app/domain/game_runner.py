from app.domain.deck import Deck
from app.domain.game_board import GameBoard
from app.domain.player import Player


class GameRunner:
    playerList = []
    currentPlayerTurn = Player()
    gameBoardStatus = GameBoard()
    deck = Deck()

    @staticmethod
    def test_method():
        return True
