import numpy as np

######################################################################
#
# Class Name: GameBoard
#   This class builds the game board matrix.
#
# @author Patricia Dunlap
# @version 1.0
#
######################################################################

#BEGIN: GameBoard class
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
        #BEGIN: Create room, hallways and home attributes
        #build corner room dictionaries
        self.studyRoomDict = {
            "id": 18,
            "name": "study",
            "isCornerRoom": 1,
            "type": "room"
        }
        self.loungeRoomDict = {
            "id": 16,
            "name": "lounge",
            "isCornerRoom": 1,
            "type": "room"
        }
        self.conservatoryRoomDict = {
            "id": 14,
            "name": "conservatory",
            "isCornerRoom": 1,
            "type": "room"
        }
        self.kitchenGDict = {
            "id": 12,
            "name": "kitchen",
            "isCornerRoom": 1,
            "type": "room"
        }

        #build non-corner room dictionaries
        self.hallRoomDict = {
            "id": 17,
            "name": "hall",
            "isCornerRoom": 0,
            "type": "room"
        }
        self.libraryRoomDict = {
            "id": 19,
            "name": "library",
            "isCornerRoom": 0,
            "type": "room"
        }
        self.billiardRoomDict = {
            "id": 20,
            "name": "billiard room",
            "isCornerRoom": 0,
            "type": "room"
        }
        self.diningRoomDict = {
            "id": 15,
            "name": "dining",
            "isCornerRoom": 0,
            "type": "room"
        }
        self.ballroomRoomDict = {
            "id": 13,
            "name": "ball room",
            "isCornerRoom": 0,
            "type": "room"
        }

        #build hallway dictionaries
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
        # END: Create room, hallways and home attributes


        # createGameBoardMatrix()
        #
        # This method accepts no parameters and creates the game board array.
        #
        # postcondition: The method creates the GameBoard array and returns it.
        #
        # @author: Patricia Dunlap
        #
        def createGameBoardMatrix():
            # Build GameBoardArray matrix
            self.gameBoardArray = np.array(
                [18, 18, 18, 21, 17, 17, 17, 22, 16, 16, 16],
                [18, 18, 18, 0, 17, 17, 17, 0, 16, 16, 16],
                [18, 18, 18, 0, 17, 17, 17, 0, 16, 16, 16],
                [23, 0, 0, 25, 0, 0, 0, 0, 0, 0, 27],
                [19, 19, 19, 24, 20, 20, 20, 26, 15, 15, 15],
                [19, 19, 19, 0, 20, 20, 20, 0, 15, 15, 15],
                [19, 19, 19, 0, 20, 20, 20, 0, 15, 15, 15],
                [28, 0, 0, 29, 0, 0, 0, 0, 0, 0, 30],
                [14, 14, 14, 31, 13, 13, 13, 32, 12, 12, 12],
                [14, 14, 14, 0, 13, 13, 13, 0, 12, 12, 12],
                [14, 14, 14, 0, 13, 13, 13, 0, 12, 12, 12])

            gameBoardMatrix = self.gameBoardArray

            return gameBoardMatrix