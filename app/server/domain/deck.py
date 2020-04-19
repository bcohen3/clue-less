import random

import numpy

from app.server.domain.room_card import RoomCard
from app.server.domain.suspect_card import SuspectCard
from app.server.domain.weapon_card import WeaponCard


class Deck:
    cards_by_id = [SuspectCard(0, "Miss Scarlet"), SuspectCard(1, "Mrs. White"), SuspectCard(2, "Mrs. Peacock"),
                   SuspectCard(3, "Colonel Mustard"), SuspectCard(4, "Professor Plum"), SuspectCard(5, "Mr. Green"),
                   WeaponCard(6, "wrench"), WeaponCard(7, "candlestick"), WeaponCard(8, "lead pipe"),
                   WeaponCard(9, "rope"), WeaponCard(10, "revolver"), WeaponCard(11, "knife"), RoomCard(12, "kitchen"),
                   RoomCard(13, "ball room"), RoomCard(14, "conservatory"), RoomCard(15, "dining room"),
                   RoomCard(16, "lounge"), RoomCard(17, "hall"), RoomCard(18, "study"), RoomCard(19, "library"),
                   RoomCard(20, "billiard room")]
    cards = cards_by_id.copy()

    def get_card_data_by_id(self, card_id):
        return self.cards_by_id[card_id]

    def shuffle(self):
        random.shuffle(self.cards)

    def chunk_cards(self, number_of_players):
        return numpy.array_split(numpy.array(self.cards), number_of_players)