class Envelope:
    def __init__(self, suspect_card=None, weapon_card=None, room_card=None):
        self.suspect_card = suspect_card
        self.weapon_card = weapon_card
        self.room_card = room_card

    def get_card_ids(self):
        return [self.suspect_card.id, self.weapon_card.id, self.room_card.id]

    @property
    def suspect_card(self):
        return self._suspect_card

    @suspect_card.setter
    def suspect_card(self, card):
        self._suspect_card = card

    @property
    def weapon_card(self):
        return self._weapon_card

    @weapon_card.setter
    def weapon_card(self, card):
        self._weapon_card = card

    @property
    def room_card(self):
        return self._room_card

    @room_card.setter
    def room_card(self, card):
        self._room_card = card
