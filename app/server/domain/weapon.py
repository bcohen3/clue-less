from app.server.domain.game_piece import GamePiece

######################################################################
#
# Class Name: Weapon
#   This class tracks and manages the weapon's movements.
#
######################################################################

#BEGIN: Weapon class
class Weapon(GamePiece):
    def __init__(self, weapon_id, x_coordinate, y_coordinate, cards):
        super().__init__(weapon_id, x_coordinate, y_coordinate)
        self.cards = cards
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_card_ids(self):
        return [card.id for card in self.cards]

    # get_coordinates(self)
    #
    # This method accepts no parameters and returns the current weapon's coordinates
    #
    def get_coordinates(self):
        return self.x_coordinate, self.y_coordinate

    # update_coordinates(self, x_coordinate, y_coordinate)
    #
    # This overload method accepts two parameters and sets the current weapon's x and y coodinates.
    #
    # @param x_coordinate integer representing the Weapon's next position, x coordinate
    # @param y_coordinate integer representing the Weapon's next position, y coordinate
    #
    # postcondition: The method moves the weapon to x and y coordinates.
    #
    def update_coordinates(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

#END: Weapon class