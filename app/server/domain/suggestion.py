class Suggestion:
    def __init__(self, suspect_card, weapon_card, room_card, is_accusation=False):
        self.suspect_card = suspect_card
        self.weapon_card = weapon_card
        self.room_card = room_card
        self.is_accusation = is_accusation

    def get_card_ids(self):
        return [self.suspect_card.id, self.weapon_card.id, self.room_card.id]
