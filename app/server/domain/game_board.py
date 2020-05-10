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
         ['x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
         ['b', 'b', 'b', 'b', 'b', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
      ]

      # Begin: Create room, hallways and home attributes
      # Build game board non-corner rooms dictionary
      self.gameBoardOtherRoomDict = {
         0: {"id": 17, "name": "hall", "altname": "Michaels Office",
             "isCornerRoom": 0, "type": "room",
             "adjacentHall": ('A', 'B', 'D'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": None,
             "xIndex": set(range(5, 8, 1)), "yIndex": set(range(1, 4, 1))},
         1: {"id": 19, "name": "library", "altname": "Bathroom",
             "isCornerRoom": 0, "type": "room",
             "adjacentHall": ('C', 'F', 'H'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": None,
             "xIndex": set(range(1, 4, 1)), "yIndex": set(range(5, 8, 1))},
         2: {"id": 20, "name": "billiard room", "altname": "Break Room",
             "isCornerRoom": 0, "type": "room",
             "adjacentHall": ('D', 'F', 'I', 'G'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": None,
             "xIndex": set(range(5, 8, 1)), "yIndex": set(range(5, 8, 1))},
         3: {"id": 15, "name": "dining room", "altname": "The Annex",
             "isCornerRoom": 0, "type": "room",
             "adjacentHall": ('E', 'G', 'J'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": None,
             "xIndex": set(range(9, 12, 1)), "yIndex": set(range(5, 8, 1))},
         4: {"id": 13, "name": "ball room", "altname": "Warehouse",
             "isCornerRoom": 0, "type": "room",
             "adjacentHall": ('K', 'I', 'L'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": None,
             "xIndex": set(range(5, 8, 1)), "yIndex": set(range(9, 12, 1))}
      }

      # Build game board corner rooms dictionary
      self.gameBoardCornerRoomDict = {
         5: {"id": 18, "name": "study", "altname": "Reception",
             "isCornerRoom": 1, "type": "room",
             "adjacentHall": ('A', 'C'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": "kitchen",
             "xIndex": set(range(1, 4, 1)),
             "yIndex": set(range(1, 4, 1))},
         6: {"id": 16, "name": "lounge", "altname": "Conference Room",
             "isCornerRoom": 1, "type": "room",
             "adjacentHall": ('B', 'E'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": "conservatory",
             "xIndex": set(range(9, 12, 1)),
             "yIndex": set(range(1, 4, 1))},
         7: {"id": 14, "name": "conservatory", "altname": "Lobby",
             "isCornerRoom": 1, "type": "room",
             "adjacentHall": ('H', 'K'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": "lounge",
             "xIndex": set(range(1, 4, 1)),
             "yIndex": set(range(9, 12, 1))},
         8: {"id": 12, "name": "kitchen", "altname": "Vance Refrigeration",
             "isCornerRoom": 1, "type": "room",
             "adjacentHall": ('J', 'L'), "adjacentRoomA": None,
             "adjacentRoomB": None, "secretPassage": "study",
             "xIndex": set(range(9, 12, 1)),
             "yIndex": set(range(9, 12, 1))}
      }

      # Build game board hallways dictionary
      self.gameBoardHallwaysDict = {
         21: {"id": "21", "name": "A", "altname": None,
              "isCornerRoom": 0,"type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "study",
              "adjacentRoomB": "hall", "secretPassage": None,
              "xIndex": 4, "yIndex": 2},
         22: {"id": "22", "name": "B", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "hall",
              "adjacentRoomB": "lounge", "secretPassage": None,
              "xIndex": 8, "yIndex": 2},
         23: {"id": "23", "name": "C", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "study",
              "adjacentRoomB": "library", "secretPassage": None,
              "xIndex": 2, "yIndex": 4},
         25: {"id": "25", "name": "D", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "hall",
              "adjacentRoomB": "billiard room", "secretPassage": None,
              "xIndex": 6, "yIndex": 4},
         27: {"id": "27", "name": "E", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "lounge",
              "adjacentRoomB": "dining room", "secretPassage": None,
              "xIndex": 10, "yIndex": 4},
         24: {"id": "24", "name": "F", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "library",
              "adjacentRoomB": "billiard room", "secretPassage": None,
              "xIndex": 4, "yIndex": 6},
         26: {"id": "26", "name": "G", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "billiard room",
              "adjacentRoomB": "dining room", "secretPassage": None,
              "xIndex": 8, "yIndex": 6},
         28: {"id": "28", "name": "H", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "library",
              "adjacentRoomB": "conservatory", "secretPassage": None,
              "xIndex": 2, "yIndex": 8},
         29: {"id": "29", "name": "I", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "billiard room",
              "adjacentRoomB": "ball room", "secretPassage": None,
              "xIndex": 6, "yIndex": 8},
         30: {"id": "30", "name": "J", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "dining room",
              "adjacentRoomB": "kitchen", "secretPassage": None,
              "xIndex": 10, "yIndex": 8},
         31: {"id": "31", "name": "K", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "conservatory",
              "adjacentRoomB": "ball room", "secretPassage": None,
              "xIndex": 4, "yIndex": 10},
         32: {"id": "32", "name": "L", "altname": None,
              "isCornerRoom": 0, "type": "hallway",
              "adjacentHall": None, "adjacentRoomA": "ball room",
              "adjacentRoomB": "kitchen", "secretPassage": None,
              "xIndex": 8, "yIndex": 10}
      }

      # Build game board players dictionary
      self.gameBoardPlayersDict = {
         0: {"id": 0, "name": "Miss Scarlet", "altname": "Dwight",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "B",
             "adjacentRoomA": "hall",
             "adjacentRoomB": "lounge", "secretPassage": None,
             "xIndex": 8, "yIndex": 0},
         1: {"id": 1, "name": "Colonel Mustard", "altname": "Jim",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "E",
             "adjacentRoomA": "lounge",
             "adjacentRoomB": "dining room", "secretPassage": None,
             "xIndex": 12, "yIndex": 4},
         2: {"id": 2, "name": "Mrs. White", "altname": "Michael",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "L",
             "adjacentRoomA": "ball room",
             "adjacentRoomB": "kitchen", "secretPassage": None,
             "xIndex": 8, "yIndex": 12},
         3: {"id": 3, "name": "Mr. Green", "altname": "Pam",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "K",
             "adjacentRoomA": "conservatory",
             "adjacentRoomB": "ball room", "secretPassage": None,
             "xIndex": 4, "yIndex": 12},
         4: {"id": 4, "name": "Mrs. Peacock", "altname": "Kelly",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "H",
             "adjacentRoomA": "library",
             "adjacentRoomB": "conservatory", "secretPassage": None,
             "xIndex": 0, "yIndex": 8},
         5: {"id": 5, "name": "Professor Plum", "altname": "Phyllis",
             "isCornerRoom": 0, "type": "home space", "adjacentHall": "C",
             "adjacentRoomA": "study",
             "adjacentRoomB": "library", "secretPassage": None,
             "xIndex": 0, "yIndex": 4}
      }
      # END: Creating room, hallways and home attributes


      #Begin: Build game locations
      self.rooms = dict.copy(self.gameBoardOtherRoomDict)
      self.rooms.update(self.gameBoardCornerRoomDict)
      self.rooms.update(self.gameBoardHallwaysDict)
      self.roomKeys = self.rooms.keys()

      #Rooms only
      self.roomsOnlyDict = self.gameBoardCornerRoomDict.copy()
      self.roomsOnlyDict.update(self.gameBoardOtherRoomDict)
      #End: Build game locations

      # passage coords list
      self.passageCoords = {
         0: {"id": 18, "cornerRoom": "study", "altname": "Reception", "xIndex": 3, "yIndex": 3},
         1: {"id": 16, "cornerRoom": "lounge", "altname": "Conference Room", "xIndex": 9, "yIndex": 3},
         2: {"id": 12, "cornerRoom": "kitchen", "altname": "Vance Refrigeration", "xIndex": 9, "yIndex": 9},
         3: {"id": 14, "cornerRoom": "conservatory", "altname": "Lobby", "xIndex": 3, "yIndex": 9}
      }

   def find_free_spot_in_room(self, room_id):
      Point = namedtuple('Point', 'x_coordinate y_coordinate')

      #loop through room and hallway keys
      for roomIdx in self.roomKeys:
         if self.rooms[roomIdx]['id'] == room_id:
            x = self.rooms[roomIdx]['xIndex']
            y = self.rooms[roomIdx]['yIndex']

            #If hallway, set hallway coordinates
            if self.rooms[roomIdx]['type'] == "hallway":
               if self.board[y][x] == 'b':
                  return Point(x, y)
               else:
                  return None

            #Else is room
            elif self.rooms[roomIdx]['type'] == "room":
               for y_coordinate in y:
                  for x_coordinate in x:
                     if self.board[y_coordinate][x_coordinate] == 'b':
                        return Point(x_coordinate, y_coordinate)

            #Invalid room id
            else:
               return None

   def find_player_in_room(self, player_id, room_id):
      Point = namedtuple('Point', 'x_coordinate y_coordinate')
      for roomIdx in self.roomKeys:
         if self.rooms[roomIdx]['id'] == room_id:
            x = self.rooms[roomIdx]['xIndex']
            y = self.rooms[roomIdx]['yIndex']

            # If hallway, set hallway coordinates
            if self.rooms[roomIdx]['type'] == "hallway":
               return None

            # Else is room
            elif self.rooms[roomIdx]['type'] == "room":
               for y_coordinate in y:
                  for x_coordinate in x:
                     if self.board[y_coordinate][x_coordinate] == player_id:
                        return Point(x_coordinate, y_coordinate)

            # Invalid room id
            else:
               return None

      return None

   def find_weapon_in_room(self, weapon_id, room_id):
      Point = namedtuple('Point', 'x_coordinate y_coordinate')
      for roomIdx in self.roomKeys:
         if self.rooms[roomIdx]['id'] == room_id:
            x = self.rooms[roomIdx]['xIndex']
            y = self.rooms[roomIdx]['yIndex']

            # If hallway, set hallway coordinates
            if self.rooms[roomIdx]['type'] == "hallway":
               return None

            # Else is room
            elif self.rooms[roomIdx]['type'] == "room":
               for y_coordinate in y:
                  for x_coordinate in x:
                     if self.board[y_coordinate][x_coordinate] == weapon_id:
                        return Point(x_coordinate, y_coordinate)

            # Invalid room id
            else:
               return None

      return None

   def print_board(self):
      for row in self.board:
         print(" ".join(map(str, row)))
