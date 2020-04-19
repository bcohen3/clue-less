from unittest import TestCase

from app.server.domain.deck import Deck
from app.server.domain.player import Player


class TestPlayer(TestCase):
    @classmethod
    def setUpClass(cls):
        cards = Deck().cards_by_id[0:3]
        cls.player = Player(0, 0, 0, cards)

    def test_get_card_ids(self):
        self.assertEqual([0, 1, 2], self.player.get_card_ids())
