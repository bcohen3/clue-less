from app.server.domain.card import Card


class SuspectCard(Card):
    def __init__(self, card_id, value):
        super().__init__(card_id, 'suspect')
        self.value = value
