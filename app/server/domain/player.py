from app.server.domain.game_piece import GamePiece


class Player(GamePiece):
    def __init__(self, player_id, x_coordinate, y_coordinate, cards, is_winner=False, is_loser=False):
        super().__init__(player_id, x_coordinate, y_coordinate)
        self.cards = cards
        self.is_winner = is_winner
        self.is_loser = is_loser
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_card_ids(self):
        return [card.id for card in self.cards]

    # get_coordinates(self)
    #
    # This method accepts no parameters and returns the current player's coordinates
    #
    def get_coordinates(self):
        return self.x_coordinate, self.y_coordinate

    # update_coordinates(self, x_coordinate, y_coordinate)
    #
    # This overload method accepts two parameters and sets the current player's x and y coodinates.
    #
    # @param x_coordinate integer representing the Player's next position, x coordinate
    # @param y_coordinate integer representing the Player's next position, y coordinate
    #
    # postcondition: The method moves the player to the x and y coordinates.
    #
    def update_coordinates(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

