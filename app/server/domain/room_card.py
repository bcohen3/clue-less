from app.server.domain.card import Card


class RoomCard(Card):
    def __init__(self, card_id, value):
        super().__init__(card_id, 'room')
        self.value = value
