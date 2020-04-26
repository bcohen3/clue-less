from collections import namedtuple


######################################################################
#
# Class Name: GameBoard
#   This class builds the game board matrix.
#
######################################################################

# BEGIN: GameBoard class
class GameBoard:
    # init(self)
    #
    # This method is the Game Board constructor.
    #
    # postcondition: The method creates the game board matrix.
    #
    # @author: Patricia Dunlap
    #
    def __init__(self):
        self.board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x'],
            ['x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'p', 'x', 'b', 'b', 'b', 'x', 'p', 'b', 'b', 'x'],
            ['b', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'b'],
            ['x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x'],
            ['b', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'x'],
            ['x', 'b', 'b', 'p', 'x', 'b', 'b', 'b', 'x', 'p', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x'],
            ['x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b', 'x'],
            ['x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x']
        ]

    def find_free_spot_in_room(self, room_id):
        Point = namedtuple('Point', 'x_coordinate y_coordinate')
        for room in self.rooms:
            if room['id'] == room_id:
                x = room['x_index']
                y = room['y_index']
                for y_coordinate in range(y, y+3):
                    for x_coordinate in range(x, x+3):
                        if self.board[y_coordinate][x_coordinate] == 'b':
                            return Point(x_coordinate, y_coordinate)
        return None

    def find_player_in_room(self, player_id, room_id):
        Point = namedtuple('Point', 'x_coordinate y_coordinate')
        for room in self.rooms:
            if room['id'] == room_id:
                x = room['x_index']
                y = room['y_index']
                for y_coordinate in range(y, y+3):
                    for x_coordinate in range(x, x+3):
                        if self.board[y_coordinate][x_coordinate] == player_id:
                            return Point(x_coordinate, y_coordinate)
        return None

    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))