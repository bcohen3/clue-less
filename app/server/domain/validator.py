######################################################################
#
# Class Name: Validator
#   This class validates the player's and weapon's movements.
#
# @author Patricia Dunlap
# @version 1.0
#
######################################################################

#BEGIN: Validator class
class Validator:

    # init(self, PlayerID, currPositionx, currPositiony)
    #
    # This method accepts three parameters and is a parametrized constructor for the Validator class.
    #
    # @param PlayerID integer representing the Player's unique ID
    # @param currPositionx integer representing the Player's current position, x coordinate
    # @param currPositiony integer representing the Player's current position, y coordinate
    #
    # precondition: PlayerID is an integer
    # precondition: positionx is an integer
    # precondition: positiony is an integer
    #
    # postcondition: The method sets the values of the three parameters.
    #
    # @author: Patricia Dunlap
    #
    def __init__(self, PlayerID, currPositionx, currPositiony):
        self.PlayerID = PlayerID
        self.currPositionx = currPositionx
        self.currPositiony = currPositiony

        # temp set for other rooms: REMOVE WHEN NOT NEEDED
        self.otherRooms = {"hall", "library", "billiard room", "dining room", "ballroom"}


    # checkRoomCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a corner room.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # precondition: positionx is an integer
    # precondition: positiony is an integer
    #
    # postcondition: The method checks whether the coordinates are a corner room. If so,
    #                it returns the room name. If not, it returns false.
    #
    # @author: Patricia Dunlap
    #
    def checkRoomCoordRange(self, positionx, positiony):
        # result
        roomResult = "false"

        # Study room
        studyXCoords = set(range(0, 11, 1))
        studyYCoords = set(range(11, 21, 1))

        # Lounge room
        loungeXCoords = set(range(21, 31, 1))
        loungeYCoords = set(range(31, 41, 1))

        # Kitchen room
        kitchenXCoords = set(range(41, 51, 1))
        kitchenYCoords = set(range(51, 61, 1))

        # Conservatory room
        conservatoryXCoords = set(range(61, 71, 1))
        conservatoryYCoords = set(range(71, 81, 1))

        # Set roomResult value based on the x and y coordinates
        if (positionx in studyXCoords) and (positiony in studyYCoords):
            roomResult = "study"
        elif (positionx in loungeXCoords) and (positiony in loungeYCoords):
            roomResult = "lounge"
        elif (positionx in kitchenXCoords) and (positiony in kitchenYCoords):
            roomResult = "kitchen"
        elif (positionx in conservatoryXCoords) and (
                positiony in conservatoryYCoords):
            roomResult = "conservatory"
        else:
            roomResult = "false"

        # return result
        return roomResult

    # checkHallwayCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a hallway.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # precondition: positionx is an integer
    # precondition: positiony is an integer
    #
    # postcondition: The method checks whether the coordinates are a hallway. If so,
    #                it returns 1 (true). If not, it returns 0 (false).
    #
    # @author: Patricia Dunlap
    #
    def checkHallwayCoordRange(self, positionx, positiony):
        # result
        hallwayResult = 0

        # Hallway A
        hallAXCoords = set(range(0, 6, 1))
        hallAYCoords = set(range(6, 11, 1))

        # Hallway B
        hallBXCoords = set(range(11, 16, 1))
        hallBYCoords = set(range(16, 21, 1))

        # Hallway C
        hallCXCoords = set(range(21, 26, 1))
        hallCYCoords = set(range(26, 31, 1))

        # Hallway D
        hallDXCoords = set(range(31, 36, 1))
        hallDYCoords = set(range(36, 41, 1))

        # Hallway E
        hallEXCoords = set(range(41, 46, 1))
        hallEYCoords = set(range(46, 51, 1))

        # Hallway F
        hallFXCoords = set(range(51, 56, 1))
        hallFYCoords = set(range(56, 61, 1))

        # Hallway G
        hallGXCoords = set(range(61, 66, 1))
        hallGYCoords = set(range(66, 71, 1))

        # Hallway H
        hallHXCoords = set(range(71, 76, 1))
        hallHYCoords = set(range(76, 81, 1))

        # Hallway I
        hallIXCoords = set(range(81, 86, 1))
        hallIYCoords = set(range(86, 91, 1))

        # Hallway J
        hallJXCoords = set(range(91, 96, 1))
        hallJYCoords = set(range(96, 101, 1))

        # Hallway K
        hallKXCoords = set(range(101, 106, 1))
        hallKYCoords = set(range(106, 111, 1))

        # Hallway L
        hallLXCoords = set(range(111, 116, 1))
        hallLYCoords = set(range(116, 121, 1))

        # Set hallwayResult value based on the x and y coordinates
        if positionx in hallAXCoords and positiony in hallAYCoords or \
                positionx in hallBXCoords and positiony in hallBYCoords or \
                positionx in hallCXCoords and positiony in hallCYCoords or \
                positionx in hallDXCoords and positiony in hallDYCoords or \
                positionx in hallEXCoords and positiony in hallEYCoords or \
                positionx in hallFXCoords and positiony in hallFYCoords or \
                positionx in hallGXCoords and positiony in hallGYCoords or \
                positionx in hallHXCoords and positiony in hallHYCoords or \
                positionx in hallIXCoords and positiony in hallIYCoords or \
                positionx in hallJXCoords and positiony in hallJYCoords or \
                positionx in hallKXCoords and positiony in hallKYCoords or \
                positionx in hallLXCoords and positiony in hallLYCoords:
            hallwayResult = 1

        #Set to false, not in hallway
        else:
            hallwayResult = 0

        #return results
        return hallwayResult

    # validatePlayerMove(PlayerID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus)
    #
    # This method accepts seven parameters and validates the player's next move.
    #
    # @param PlayerID integer representing the Player's unique ID
    # @param currPositionx integer representing the Player's current position, x coordinate
    # @param currPositiony integer representing the Player's current position, y coordinate
    # @param nextPositionx integer representing the Player's next position, x coordinate
    # @param nextPositiony integer representing the Player's next position, y coordinate
    # @param isSuggestion integer representing the whether the move is a result of a suggestion/accusation
    # @param GameBoardStatus integer representing the Clue-Less game board status
    #
    # precondition: PlayerID is an integer
    # precondition: currPositionx is an integer
    # precondition: currPositiony is an integer
    # precondition: nextPositionx is an integer
    # precondition: nextPositiony is an integer
    # precondition: isSuggestion is an integer value (0 or 1)
    # precondition: GameBoardStatus is an integer
    #
    # postcondition: The method validates the player's next move. If the move
    #                 is valid, it returns 1 (true). If the move is invalid,
    #                 it returns 0 (false).
    #
    # @author: Patricia Dunlap
    #
    def validatePlayerMove(self, PlayerID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        #set default value for isValidMove
        isValidMove = 0

        #check current location
        currentCornerRoomName = self.checkRoomCoordRange(currPositionx, currPositiony)
        currentIsHallway = self.checkHallwayCoordRange(currPositionx, currPositiony)
        # **TO DO**: Need non-corner room coordinates

        #check next location
        nextCornerRoomName = self.checkRoomCoordRange(nextCoordx, nextCoordy)
        nextIsHallway = self.checkHallwayCoordRange(nextCoordx, nextCoordy)
        # **TO DO**: Need non-corner room coordinates
        nextRoomName = "Library"

        #Player is currently located in one of the corner rooms
        if currentCornerRoomName != "false":
            #CornerNextMoveType1: Validate player is going from study to kitchen or vice versa
            if currentCornerRoomName == "study" and nextCornerRoomName == "kitchen" or \
                    currentCornerRoomName == "kitchen" and nextCornerRoomName == "study":
                isValidMove = 1

            #CornerNextMoveType2: Validate player is going from lounge to conservatory or vice versa
            elif currentCornerRoomName == "lounge" and nextCornerRoomName == "conservatory" or \
                    currentCornerRoomName == "conservatory" and nextCornerRoomName == "lounge":
                isValidMove = 1

            #CornerNextMoveType3: Validate player is going from corner room to adjacent hallway
            elif nextIsHallway:
                # **TO DO**: check hallway move is adjacent to an adjacent room
                isValidMove = 1

            #CornerNextMoveType4: Validate player is going from corner room to a non-corner room, suggestion move
            elif nextRoomName in self.otherRooms:
                #If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = 1
                else:
                    isValidMove = 0

        #Player is currently located in a hallway
        elif currentIsHallway:
            #HallwayNextMoveType1: Validate player is not going to hallway to hallway
            if nextIsHallway == 0:
                isValidMove = 1

            #HallwayNextMoveType2: Validate player is going from hallway to adjacent room
            #  **TO DO**: Need hallway-adjacent room relationships

        #Else, located in a non-corner room
        else:
            #NextMoveType1: Validate player is going from non-corner room to adjacent hallway
            # **TO DO**: Need hallway-adjacent room relationships
            if nextIsHallway == 1:
                isValidMove = 1

            #NextMoveType2: Confirm player is going from non-corner room to non-corner room because of a suggestion
            elif nextRoomName in self.otherRooms:
                # If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = 1
                else:
                    isValidMove = 0

            #NextMoveType3: Confirm player is going from non-corner room to corner room because of a suggestion
            elif nextCornerRoomName != "false":
                # If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = 1
                else:
                    isValidMove = 0

        #return validation result
        return isValidMove

    # validateWeaponMove(self, WeaponID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
    #
    # This method accepts seven parameters and validates the weapon's next move.
    #
    # @param WeaponID integer representing the Weapon's unique ID
    # @param currPositionx integer representing the Weapon's current position, x coordinate
    # @param currPositiony integer representing the Weapon's current position, y coordinate
    # @param nextPositionx integer representing the Weapon's next position, x coordinate
    # @param nextPositiony integer representing the Weapon's next position, y coordinate
    # @param isSuggestion integer representing the whether the move is a result of a suggestion/accusation
    # @param GameBoardStatus integer representing the Clue-Less game board status
    #
    # precondition: WeaponID is an integer
    # precondition: currPositionx is an integer
    # precondition: currPositiony is an integer
    # precondition: nextPositionx is an integer
    # precondition: nextPositiony is an integer
    # precondition: isSuggestion is an integer value (0 or 1)
    # precondition: GameBoardStatus is an integer
    #
    # postcondition: The method validates the weapon's next move. If the move
    #                 is valid, it returns 1 (true). If the move is invalid,
    #                 it returns 0 (false).
    #
    # @author: Patricia Dunlap
    #
    def validateWeaponMove(self, WeaponID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        return 1

#END: Validator class