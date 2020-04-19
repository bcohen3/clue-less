from app.server.domain.game_piece import GamePiece


class Player(GamePiece):
    def __init__(self, player_id, x_coordinate, y_coordinate, cards, is_winner=False, is_loser=False):
        super().__init__(player_id, x_coordinate, y_coordinate)
        self.cards = cards
        self.is_winner = is_winner
        self.is_loser = is_loser

    def get_card_ids(self):
        return [card.id for card in self.cards]
