from app.server.domain.card import Card


class WeaponCard(Card):
    def __init__(self, card_id, value):
        super().__init__(card_id, 'weapon')
        self.value = value
