from unittest import TestCase

from app.server.domain.game_piece import GamePiece


class TestGamePiece(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_piece = GamePiece(0, 0, 0)

    def test_update_coordinates(self):
        self.game_piece.update_coordinates(1, 2)
        self.assertEqual(1, self.game_piece.x_coordinate)
        self.assertEqual(2, self.game_piece.y_coordinate)
