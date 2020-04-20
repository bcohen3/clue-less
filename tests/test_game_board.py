from unittest import TestCase

from app.server.domain.game_board import GameBoard


class TestGameBoard(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_board = GameBoard()

    def test_finds_free_spot_in_room(self):
        self.game_board.board[0][0] = 'x'
        free_spot = self.game_board.find_free_spot_in_room(18)
        self.assertEqual(1, free_spot.x_coordinate)
        self.assertEqual(0, free_spot.y_coordinate)

    def test_handles_no_free_spot_in_room(self):
        self.game_board.board[0][0] = 'x'
        self.game_board.board[0][1] = 'x'
        self.game_board.board[0][2] = 'x'
        self.game_board.board[1][0] = 'x'
        self.game_board.board[1][1] = 'x'
        self.game_board.board[1][2] = 'x'
        self.game_board.board[2][0] = 'x'
        self.game_board.board[2][1] = 'x'
        self.game_board.board[2][2] = 'x'

        free_spot = self.game_board.find_free_spot_in_room(18)
        self.assertIsNone(free_spot)

    def test_finds_player_in_room(self):
        self.game_board.board[0][0] = 1
        player_spot = self.game_board.find_player_in_room(1, 18)
        self.assertEqual(0, player_spot.x_coordinate)
        self.assertEqual(0, player_spot.y_coordinate)

    def test_handles_no_player_in_room(self):
        player_spot = self.game_board.find_player_in_room(1, 18)
        self.assertIsNone(player_spot)