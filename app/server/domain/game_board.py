from collections import namedtuple


######################################################################
#
# Class Name: GameBoard
#   This class builds the game board matrix.
#
# @author Patricia Dunlap
# @version 1.0
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
            ['b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'p', 'x', 'b', 'b', 'b', 'x', 'p', 'b', 'b'],
            ['x', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x'],
            ['b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b'],
            ['x', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x'],
            ['b', 'b', 'p', 'x', 'b', 'b', 'b', 'x', 'p', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'x', 'b', 'b', 'b', 'x', 'b', 'b', 'b']
        ]

        # BEGIN: Create room, hallways and home attributes
        self.studyRoomDict = {
            "id": 18,
            "name": "study",
            "isCornerRoom": 1,
            "type": "room",
            "x_index": 0,
            "y_index": 0
        }

        self.hallRoomDict = {
            "id": 17,
            "name": "hall",
            "isCornerRoom": 0,
            "type": "room",
            "x_index": 4,
            "y_index": 0
        }

        self.loungeRoomDict = {
            "id": 16,
            "name": "lounge",
            "isCornerRoom": 1,
            "type": "room",
            "x_index": 8,
            "y_index": 0
        }

        self.libraryRoomDict = {
            "id": 19,
            "name": "library",
            "isCornerRoom": 0,
            "type": "room",
            "x_index": 0,
            "y_index": 4
        }

        self.billiardRoomDict = {
            "id": 20,
            "name": "billiard room",
            "isCornerRoom": 0,
            "type": "room",
            "x_index": 4,
            "y_index": 4
        }

        self.diningRoomDict = {
            "id": 15,
            "name": "dining",
            "isCornerRoom": 0,
            "type": "room",
            "x_index": 8,
            "y_index": 4
        }

        self.conservatoryRoomDict = {
            "id": 14,
            "name": "conservatory",
            "isCornerRoom": 1,
            "type": "room",
            "x_index": 0,
            "y_index": 8
        }

        self.ballroomRoomDict = {
            "id": 13,
            "name": "ball room",
            "isCornerRoom": 0,
            "type": "room",
            "x_index": 4,
            "y_index": 8
        }

        self.kitchenDict = {
            "id": 12,
            "name": "kitchen",
            "isCornerRoom": 1,
            "type": "room",
            "x_index": 8,
            "y_index": 8
        }

        # build hallway dictionaries
        self.hallwayADict = {
            "id": 21,
            "name": "hallway a",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayBDict = {
            "id": 22,
            "name": "hallway b",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayCDict = {
            "id": 23,
            "name": "hallway c",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayDDict = {
            "id": 25,
            "name": "hallway d",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayEDict = {
            "id": 27,
            "name": "hallway e",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayFDict = {
            "id": 24,
            "name": "hallway f",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayGDict = {
            "id": 26,
            "name": "hallway g",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayHDict = {
            "id": 28,
            "name": "hallway h",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayIDict = {
            "id": 29,
            "name": "hall i",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayJDict = {
            "id": 30,
            "name": "hallway j",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayKDict = {
            "id": 31,
            "name": "hallway k",
            "isCornerRoom": 0,
            "type": "hallway"
        }
        self.hallwayLDict = {
            "id": 32,
            "name": "hallway l",
            "isCornerRoom": 0,
            "type": "hallway"
        }

        # build home space dictionaries
        self.mrsWhiteHomeSpaceDict = {
            "id": 1,
            "name": "Mrs. White",
            "isCornerRoom": 0,
            "type": "home space"
        }
        self.mrsGreenHomeSpaceDict = {
            "id": 5,
            "name": "Mr. Green",
            "isCornerRoom": 0,
            "type": "home space"
        }
        self.mrsPeacockHomeSpaceDict = {
            "id": 2,
            "name": "Mrs. Peacock",
            "isCornerRoom": 0,
            "type": "home space"
        }
        self.profPlumHomeSpaceDict = {
            "id": 4,
            "name": "Professor Plum",
            "isCornerRoom": 0,
            "type": "home space"
        }
        self.missScarlettHomeSpaceDict = {
            "id": 0,
            "name": "Miss Scarlet",
            "isCornerRoom": 0,
            "type": "home space"
        }
        self.colMustardHomeSpaceDict = {
            "id": 3,
            "name": "Colonel Mustard",
            "isCornerRoom": 0,
            "type": "home space"
        }

        self.rooms = [self.studyRoomDict, self.hallRoomDict, self.loungeRoomDict, self.libraryRoomDict,
                      self.billiardRoomDict, self.diningRoomDict, self.conservatoryRoomDict, self.ballroomRoomDict,
                      self.kitchenDict]

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