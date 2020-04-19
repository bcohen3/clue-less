from unittest import TestCase

from app.server.domain.room_card import RoomCard
from app.server.domain.suggestion import Suggestion
from app.server.domain.suspect_card import SuspectCard
from app.server.domain.weapon_card import WeaponCard


class TestSuggestion(TestCase):
    @classmethod
    def setUpClass(cls):
        suspect_card = SuspectCard(0, "Miss Scarlet")
        weapon_card = WeaponCard(8, "lead pipe")
        room_card = RoomCard(15, "library")
        cls.suggestion = Suggestion(suspect_card, weapon_card, room_card)

    def test_get_card_ids(self):
        self.assertEqual([0, 8, 15], self.suggestion.get_card_ids())
