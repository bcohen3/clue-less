from unittest import TestCase

from app.server.domain.envelope import Envelope
from app.server.domain.room_card import RoomCard
from app.server.domain.suspect_card import SuspectCard
from app.server.domain.weapon_card import WeaponCard


class TestEnvelope(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.envelope = Envelope()

    def test_get_card_ids(self):
        self.envelope.suspect_card = SuspectCard(0, "Miss Scarlet")
        self.envelope.weapon_card = WeaponCard(8, "lead pipe")
        self.envelope.room_card = RoomCard(15, "library")
        self.assertEqual([0, 8, 15], self.envelope.get_card_ids())
