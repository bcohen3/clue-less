from collections import namedtuple


######################################################################
#
# Class Name: GameBoard
#   This class builds the game board matrix.
#
######################################################################

# BEGIN: GameBoard class
class GameBoard:
   # BEGIN: Create room, hallways and home attributes
   # Build game board non-corner rooms dictionary
   gameBoardOtherRoomDict = {
      0: {"id": 17, "name": "hall", "isCornerRoom": 0, "type": "room",
          "adjacentHall": ('A', 'B', 'D'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(5, 8, 1)), "yIndex": set(range(1, 4, 1))},
      1: {"id": 19, "name": "library", "isCornerRoom": 0,
          "type": "room",
          "adjacentHall": ('C', 'F', 'H'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(1, 4, 1)), "yIndex": set(range(5, 8, 1))},
      2: {"id": 20, "name": "billiard room", "isCornerRoom": 0,
          "type": "room",
          "adjacentHall": ('D', 'F', 'I', 'G'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(5, 8, 1)), "yIndex": set(range(5, 8, 1))},
      3: {"id": 15, "name": "dining room", "isCornerRoom": 0,
          "type": "room",
          "adjacentHall": ('E', 'G', 'J'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(9, 12, 1)), "yIndex": set(range(5, 8, 1))},
      4: {"id": 13, "name": "ball room", "isCornerRoom": 0,
          "type": "room",
          "adjacentHall": ('K', 'I', 'L'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(5, 8, 1)), "yIndex": set(range(9, 12, 1))}
   }

   # Build game board corner rooms dictionary
   gameBoardCornerRoomDict = {
      5: {"id": 18, "name": "study", "isCornerRoom": 1,
          "type": "room",
          "adjacentHall": ('A', 'C'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(1, 4, 1)),
          "yIndex": set(range(1, 4, 1))},
      6: {"id": 16, "name": "lounge", "isCornerRoom": 1,
          "type": "room",
          "adjacentHall": ('B', 'E'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(9, 12, 1)),
          "yIndex": set(range(1, 4, 1))},
      7: {"id": 14, "name": "conservatory", "isCornerRoom": 1,
          "type": "room",
          "adjacentHall": ('H', 'K'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(1, 4, 1)),
          "yIndex": set(range(9, 12, 1))},
      8: {"id": 12, "name": "kitchen", "isCornerRoom": 1,
          "type": "room",
          "adjacentHall": ('J', 'L'), "adjacentRoomA": None,
          "adjacentRoomB": None,
          "xIndex": set(range(9, 12, 1)),
          "yIndex": set(range(9, 12, 1))}
   }

   # Build game board hallways dictionary
   gameBoardHallwaysDict = {
      21: {"id": "21", "name": "A", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "study",
           "adjacentRoomB": "hall",
           "xIndex": 4, "yIndex": 2},
      22: {"id": "22", "name": "B", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "hall",
           "adjacentRoomB": "lounge",
           "xIndex": 8, "yIndex": 2},
      23: {"id": "23", "name": "C", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "study",
           "adjacentRoomB": "library",
           "xIndex": 2, "yIndex": 4},
      25: {"id": "25", "name": "D", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "hall",
           "adjacentRoomB": "billiard room",
           "xIndex": 6, "yIndex": 4},
      27: {"id": "27", "name": "E", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "lounge",
           "adjacentRoomB": "dining room",
           "xIndex": 10, "yIndex": 4},
      24: {"id": "24", "name": "F", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "library",
           "adjacentRoomB": "billiard room",
           "xIndex": 4, "yIndex": 6},
      26: {"id": "26", "name": "G", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "billiard room",
           "adjacentRoomB": "dining room",
           "xIndex": 8, "yIndex": 6},
      28: {"id": "28", "name": "H", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "library",
           "adjacentRoomB": "conservatory",
           "xIndex": 2, "yIndex": 8},
      29: {"id": "29", "name": "I", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "billiard room",
           "adjacentRoomB": "ball room",
           "xIndex": 6, "yIndex": 8},
      30: {"id": "30", "name": "J", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "dining room",
           "adjacentRoomB": "kitchen",
           "xIndex": 10, "yIndex": 8},
      31: {"id": "31", "name": "K", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "conservatory",
           "adjacentRoomB": "ball room",
           "xIndex": 4, "yIndex": 10},
      32: {"id": "32", "name": "L", "isCornerRoom": 0,
           "type": "hallway",
           "adjacentHall": None, "adjacentRoomA": "ball room",
           "adjacentRoomB": "kitchen",
           "xIndex": 8, "yIndex": 10}
   }

   # Build game board players dictionary
   gameBoardPlayersDict = {
      0: {"id": 0, "name": "Miss Scarlet", "isCornerRoom": 0,
          "type": "home space", "adjacentHallway": "B",
          "adjacentRoomA": "hall",
          "adjacentRoomB": "lounge",
          "xIndex": 8, "yIndex": 0},
      1: {"id": 1, "name": "Colonel Mustard", "isCornerRoom": 0,
          "type": "home space",
          "adjacentHallway": "E", "adjacentRoomA": "lounge",
          "adjacentRoomB": "dining room",
          "xIndex": 12, "yIndex": 4},
      2: {"id": 2, "name": "Mrs. White", "isCornerRoom": 0,
          "type": "home space",
          "adjacentHallway": "L", "adjacentRoomA": "ball room",
          "adjacentRoomB": "kitchen",
          "xIndex": 8, "yIndex": 12},
      3: {"id": 3, "name": "Mr. Green", "isCornerRoom": 0,
          "type": "home space",
          "adjacentHallway": "K", "adjacentRoomA": "conservatory",
          "adjacentRoomB": "ball room",
          "xIndex": 4, "yIndex": 12},
      4: {"id": 4, "name": "Mrs. Peacock", "isCornerRoom": 0,
          "type": "home space",
          "adjacentHallway": "H", "adjacentRoomA": "library",
          "adjacentRoomB": "conservatory",
          "xIndex": 0, "yIndex": 8},
      5: {"id": 5, "name": "Professor Plum", "isCornerRoom": 0,
          "type": "home space",
          "adjacentHallway": "C", "adjacentRoomA": "study",
          "adjacentRoomB": "library",
          "xIndex": 0, "yIndex": 4}
   }

   # passage coords list
   passageCoords = {
      0: {"id": 0, "cornerRoom": "study", "xIndex": 3, "yIndex": 3},
      1: {"id": 1, "cornerRoom": "lounge", "xIndex": 9, "yIndex": 3},
      2: {"id": 2, "cornerRoom": "kitchen", "xIndex": 9, "yIndex": 9},
      3: {"id": 3, "cornerRoom": "kitchen", "xIndex": 3, "yIndex": 9}
   }
   # END: Creating room, hallways and home attributes

   # init(self)
   #
   # This method is the Game Board constructor.
   #
   # postcondition: The method creates the game board matrix.
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

      self.rooms = [self.gameBoardCornerRoomDict, self.gameBoardOtherRoomDict,
                    self.gameBoardHallwaysDict]

   def find_free_spot_in_room(self, room_id):
      Point = namedtuple('Point', 'x_coordinate y_coordinate')
      for room in self.rooms:
         if room['id'] == room_id:
            x = room['xIndex']
            y = room['yIndex']
            for y_coordinate in range(y, y + 3):
               for x_coordinate in range(x, x + 3):
                  if self.board[y_coordinate][x_coordinate] == 'b':
                     return Point(x_coordinate, y_coordinate)
      return None

   def find_player_in_room(self, player_id, room_id):
      Point = namedtuple('Point', 'x_coordinate y_coordinate')
      for room in self.rooms:
         if room['id'] == room_id:
            x = room['xIndex']
            y = room['yIndex']
            for y_coordinate in range(y, y + 3):
               for x_coordinate in range(x, x + 3):
                  if self.board[y_coordinate][x_coordinate] == player_id:
                     return Point(x_coordinate, y_coordinate)
      return None

   def print_board(self):
      for row in self.board:
         print(" ".join(map(str, row)))
