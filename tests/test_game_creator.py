from unittest import TestCase

from app.server.domain.game_creator import GameCreator


class TestGameCreator(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number_of_players = 4
        cls.game_creator = GameCreator(cls.number_of_players)

    def test_shuffles_deck_when_new_game_created(self):
        self.assertNotEqual(self.game_creator.deck.cards_by_id, self.game_creator.deck.cards)

    def test_creates_the_correct_number_of_players_when_new_game_created(self):
        self.assertEqual(4, len(self.game_creator.players))

    def test_puts_players_in_proper_order_when_new_game_created(self):
        self.assertEqual(3, self.game_creator.players[3].id)

    def test_gives_players_cards_when_new_game_created(self):
        self.assertEqual(5, len(self.game_creator.players[0].cards))
        self.assertEqual(4, len(self.game_creator.players[3].cards))

    def test_gives_players_x_coordinate_when_new_game_created(self):
        self.assertEqual(7, self.game_creator.players[1].x_coordinate)

    def test_gives_players_y_coordinate_when_new_game_created(self):
        self.assertEqual(9, self.game_creator.players[1].y_coordinate)

    def test_selects_suspect_card_for_envelope(self):
        self.assertEqual('suspect', self.game_creator.envelope.suspect_card.type)

    def test_selects_weapon_card_for_envelope(self):
        self.assertEqual('weapon', self.game_creator.envelope.weapon_card.type)

    def test_selects_room_card_for_envelope(self):
        self.assertEqual('room', self.game_creator.envelope.room_card.type)

    def test_removes_suspect_card_from_deck(self):
        self.assertNotIn(self.game_creator.envelope.suspect_card, self.game_creator.deck.cards)

    def test_removes_weapon_card_from_deck(self):
        self.assertNotIn(self.game_creator.envelope.weapon_card, self.game_creator.deck.cards)

    def test_removes_room_card_from_deck(self):
        self.assertNotIn(self.game_creator.envelope.room_card, self.game_creator.deck.cards)

    def test_creates_weapons(self):
        self.assertEqual(6, len(self.game_creator.weapons))

    def test_creates_weapons_correct_ids(self):
        self.assertEqual(self.number_of_players, self.game_creator.weapons[0].id)
        self.assertEqual(self.number_of_players+5, self.game_creator.weapons[5].id)

    def test_creates_game_board_with_appropriate_number_of_rows(self):
        self.assertEqual(11, len(self.game_creator.game_board_status.board))

    def test_creates_game_board_with_appropriate_number_of_columns(self):
        self.assertEqual(11, len(self.game_creator.game_board_status.board[0]))

    def test_adds_players_to_game_board(self):
        board = self.game_creator.game_board_status.board
        self.assertEqual(0, board[1][7])
        self.assertEqual(1, board[9][7])
        self.assertEqual(2, board[7][1])
        self.assertEqual(3, board[3][9])

