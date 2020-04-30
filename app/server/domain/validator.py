from app.server.domain import player

######################################################################
#
# Class Name: Validator
#   This class validates the player's and weapon's movements.
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
    # postcondition: The method sets the values of the three parameters.
    #
    #
    def __init__(self, PlayerID, currPositionx, currPositiony):
        self.PlayerID = PlayerID
        self.currPositionx = currPositionx
        self.currPositiony = currPositiony

        # BEGIN: Create room, hallways and home attributes
        # Build game board corner rooms dictionary
        self.gameBoardCornerRoom = {
            4: {"id": 18, "name": "study", "isCornerRoom": 1,
                "type": "room", "adjacentHall": ('A', 'C'),
                "xIndex": set(range(1, 4, 1)),
                "yIndex": set(range(1, 4, 1))},
            5: {"id": 16, "name": "lounge", "isCornerRoom": 1,
                "type": "room", "adjacentHall": ('B', 'E'),
                "xIndex": set(range(9, 12, 1)),
                "yIndex": set(range(1, 4, 1))},
            6: {"id": 14, "name": "conservatory", "isCornerRoom": 1,
                "type": "room", "adjacentHall": ('H', 'K'),
                "xIndex": set(range(1, 4, 1)),
                "yIndex": set(range(9, 12, 1))},
            7: {"id": 12, "name": "kitchen", "isCornerRoom": 1,
                "type": "room", "adjacentHall": ('J', 'L'),
                "xIndex": set(range(9, 12, 1)),
                "yIndex": set(range(9, 12, 1))}
        }

        # Build game board non-corner rooms dictionary
        self.gameBoardOtherRoom = {
            0: {"id": 17, "name": "hall", "isCornerRoom": 0, "type": "room",
                    "adjacentHall": ('A', 'B', 'D'),
                    "xIndex": set(range(5, 8, 1)), "yIndex": set(range(1, 4, 1))},
            1: {"id": 19, "name": "library", "isCornerRoom": 0, "type": "room",
                    "adjacentHall": ('C', 'F', 'H'),
                    "xIndex": set(range(1, 4, 1)), "yIndex": set(range(5, 8, 1))},
            2: {"id": 20, "name": "billiard room", "isCornerRoom": 0, "type": "room",
                    "adjacentHall": ('D', 'F', 'I', 'G'),
                    "xIndex": set(range(5, 8, 1)), "yIndex": set(range(5, 8, 1))},
            3: {"id": 13, "name": "ball room", "isCornerRoom": 0, "type": "room",
                    "adjacentHall": ('K', 'I', 'L'),
                    "xIndex": set(range(5, 8, 1)), "yIndex": set(range(9, 12, 1))}
        }

        # Build game board hallways dictionary
        self.gameBoardHallwaysDict = {
           21: {"id": "21", "name": "A", "fullName": "hallway a", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 4, "yIndex": 2, "adjacentRoomA": "study", "adjacentRoomB": "hall"},
           22: {"id": "22","name": "B", "fullName": "hallway b", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 8, "yIndex": 2, "adjacentRoomA": "hall", "adjacentRoomB": "lounge"},
           23: {"id": "23", "name": "C", "fullName": "hallway c", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 2, "yIndex": 4, "adjacentRoomA": "study", "adjacentRoomB": "library"},
           25: {"id": "25", "name": "D", "fullName": "hallway d", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 6, "yIndex": 4, "adjacentRoomA": "hall", "adjacentRoomB": "billiard room"},
           27: {"id": "27", "name": "E", "fullName": "hallway e", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 10, "yIndex": 4, "adjacentRoomA": "lounge", "adjacentRoomB": "dining room"},
           24: {"id": "24", "name": "F", "fullName": "hallway f", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 4, "yIndex": 6, "adjacentRoomA": "library", "adjacentRoomB": "billiard room"},
           26: {"id": "26", "name": "G", "fullName": "hallway g", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 8, "yIndex": 6, "adjacentRoomA": "billiard room", "adjacentRoomB": "dining room"},
           28: {"id": "28", "name": "H", "fullName": "hallway h", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 2, "yIndex": 8, "adjacentRoomA": "library", "adjacentRoomB": "conservatory"},
           29: {"id": "29", "name": "I", "fullName": "hall i", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 6, "yIndex": 8, "adjacentRoomA": "billiard room", "adjacentRoomB": "ball room"},
           30: {"id": "30", "name": "J", "fullName": "hallway j", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 10, "yIndex": 8, "adjacentRoomA": "dining room", "adjacentRoomB": "kitchen"},
           31: {"id": "31", "name": "K", "fullName": "hallway k", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 4, "yIndex": 10, "adjacentRoomA": "conservatory", "adjacentRoomB": "ball room"},
           32: {"id": "32", "name": "L", "fullName": "hallway l", "isCornerRoom": 0, "type": "hallway",
                    "xIndex": 8, "yIndex": 10, "adjacentRoomA": "ball room", "adjacentRoomB": "kitchen"}
        }

        #Build game board players dictionary
        self.gameBoardPlayersDict = {
            0: {"id": 0, "name": "Miss Scarlet", "isCornerRoom": 0, "type": "home space",
                    "hallway": "B", "adjacentRoomA": "hall", "adjacentRoomB": "lounge",
                    "xIndex": 8, "yIndex": 0},
            1: {"id": 1, "name": "Mrs. White", "isCornerRoom": 0, "type": "home space",
                    "hallway": "L", "adjacentRoomA": "ball room", "adjacentRoomB": "kitchen",
                    "xIndex": 8, "yIndex": 12},
            2: {"id": 2, "name": "Mrs. Peacock", "isCornerRoom": 0, "type": "home space",
                    "hallway": "H", "adjacentRoomA": "library", "adjacentRoomB": "conservatory",
                    "xIndex": 0, "yIndex": 8},
            3: {"id": 3, "name": "Colonel Mustard", "isCornerRoom": 0, "type": "home space",
                    "hallway": "E", "adjacentRoomA": "lounge", "adjacentRoomB": "dining room",
                    "xIndex": 12, "yIndex": 4},
            4: {"id": 4, "name": "Professor Plum", "isCornerRoom": 0, "type": "home space",
                    "hallway": "C", "adjacentRoomA": "study", "adjacentRoomB": "library",
                    "xIndex": 0, "yIndex": 4},
            5: {"id": 5, "name": "Mr. Green", "isCornerRoom": 0, "type": "home space",
                     "hallway": "K", "adjacentRoomA": "conservatory", "adjacentRoomB": "ball room",
                     "xIndex": 4, "yIndex": 12}
        }

        #non-corner rooms list
        self.otherRooms = {self.gameBoardOtherRoom[0]['name'],
                            self.gameBoardOtherRoom[1]['name'],
                            self.gameBoardOtherRoom[2]['name'],
                            self.gameBoardOtherRoom[3]['name']}

    # checkRoomCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a corner room.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a corner room. If so,
    #                it returns the room id and name. If not, it returns -1 and false.
    #
    def checkRoomCoordRange(self, positionx, positiony):
        roomCornerResultID = -1
        roomCornerResultName = False

        # Set room result values according to the x and y coordinates
        for i in range(4, 8, 1):
            if self.gameBoardCornerRoom[i]['xIndex'] == positionx and \
                    self.gameBoardCornerRoom[i]['yIndex'] == positiony:
                roomCornerResultID = self.gameBoardCornerRoom[i]['id']
                roomCornerResultName = self.gameBoardCornerRoom[i]['name']
                break

        # return results
        return roomCornerResultID, roomCornerResultName

    # checkHomeSpaceCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a character's home space.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a character's home space. If so,
    #                it returns the character's id and name. If not, it returns -1 and false.
    #
    def checkHomeSpaceCoordRange(self, positionx, positiony):
        homeSpaceResultID = -1
        homeSpaceResultName = False

        # Set home space result values according to the x and y coordinates
        for i in range(0, 6, 1):
            if self.gameBoardPlayersDict[i]['xIndex'] == positionx and \
                    self.gameBoardPlayersDict[i]['yIndex'] == positiony:
                homeSpaceResultID = self.gameBoardPlayersDict[i]['id']
                homeSpaceResultName = self.gameBoardPlayersDict[i]['name']
                break

        # return results
        return homeSpaceResultID, homeSpaceResultName

    # checkHallwayCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a hallway.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a hallway. If so,
    #                it returns the hallway's ID and name . If not, it returns -1 and False.
    #
    def checkHallwayCoordRange(self, positionx, positiony):
        hallwayResultID = -1
        hallwayResultName = False


        # Set hallway result values according to the x and y coordinates
        for j in range(21, 33, 1):
            if self.gameBoardHallwaysDict[j]['xIndex'] == positionx and \
                   self.gameBoardHallwaysDict[j]['yIndex'] == positiony:
                hallwayResultID = self.gameBoardHallwaysDict[j]['id']
                hallwayResultName = self.gameBoardHallwaysDict[j]['name']
                break

        #return results
        return hallwayResultID, hallwayResultName

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
    # postcondition: The method validates the player's next move. If the move
    #                 is valid, it returns True. If the move is invalid,
    #                 it returns False.
    #
    def validatePlayerMove(self, PlayerID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        validationMesg = None
        isValidMove = False
        currentRoomIdx = 0

        #Get current player's location
        (curr_player_x, curr_player_y) = player.Player.get_coordinates(PlayerID)

        #Get current information on room, hallway, and home space
        (currentCornerRoomID, currentCornerRoomName) = self.checkRoomCoordRange(currPositionx, currPositiony)
        (currentHallwayID, currentHallwayName) = self.checkHallwayCoordRange(currPositionx, currPositiony)
        (currentCharacterHomeSpaceID, currentCharacterHomeSpaceName) = self.checkHomeSpaceCoordRange(currPositionx, currPositiony)

        #Get next information on room, hallway, and home space
        (nextCornerRoomID, nextCornerRoomName) = self.checkRoomCoordRange(nextCoordx, nextCoordy)
        (nextHallwayID, nextHallwayName) = self.checkHallwayCoordRange(nextCoordx, nextCoordy)
        (nextCharacterHomeSpaceID, nextCharacterHomeSpaceName) = self.checkHomeSpaceCoordRange(currPositionx, currPositiony)

        #Begin: If other room, set value for current and next movement
        if currentCornerRoomName == False and currentHallwayName == False and \
            currentCharacterHomeSpaceName == False:

            # determine which other room: current
            for k in range(1, 4, 1):
                if currPositionx in self.gameBoardOtherRoom[k]['xIndex'] and \
                    currPositiony in self.gameBoardOtherRoom[k]['yIndex']:
                    currentRoomIdx = k
                    currentRoomID = self.gameBoardOtherRoom[k]["id"]
                    break

        if nextCornerRoomName == False and nextHallwayName == False and \
            nextCharacterHomeSpaceName == False:

            # determine which other room: next
            for m in range(1, 4, 1):
                if nextCoordx in self.gameBoardOtherRoom[m]['xIndex'] and \
                    nextCoordy in self.gameBoardOtherRoom[m]['yIndex']:
                    nextRoomName = self.gameBoardOtherRoom[m]["name"]
                    break
        #End: If other room, set value for current and next movement

        #Player is moving from home space
        if currentCharacterHomeSpaceID != -1:
            homeAdjHall = self.gameBoardPlayersDict[currentCharacterHomeSpaceID]['hallway']
            homeAdjRoomA = self.gameBoardPlayersDict[currentCharacterHomeSpaceID]['adjacentRoomA']
            homeAdjRoomB = self.gameBoardPlayersDict[currentCharacterHomeSpaceID]['adjacentRoomB']

            #HomeNextMoveType1: Player is moving from home space to hallway, first move (not suggestion)
            if nextHallwayName != False and isSuggestion == False:
                if nextHallwayName == homeAdjHall:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid home space to hallway move. Did you mean the hallway between " + homeAdjRoomA.capitalize() + " and " + homeAdjRoomB.capitalize() + "?"

            #HomeNextMoveType2: Player is moving from home space to hallway, first move (suggestion)
            elif nextHallwayName != False and isSuggestion:
                isValidMove = True

            else:
                isValidMove = False
                validationMesg = "Invalid home space move. Did you mean to move to the nearest hallway?"

        #Player is currently located in one of the corner rooms
        elif currentCornerRoomName != False:
            #CornerNextMoveType1: Validate player is going from study to kitchen or vice versa
            if currentCornerRoomName == "study" and nextCornerRoomName == "kitchen" or \
                    currentCornerRoomName == "kitchen" and nextCornerRoomName == "study":
                isValidMove = True

            #CornerNextMoveType2: Validate player is going from lounge to conservatory or vice versa
            elif currentCornerRoomName == "lounge" and nextCornerRoomName == "conservatory" or \
                    currentCornerRoomName == "conservatory" and nextCornerRoomName == "lounge":
                isValidMove = True

            #CornerNextMoveType3: Validate player is going from corner room to adjacent hallway
            elif nextHallwayName != False:
                cornerAdjHall = self.gameBoardCornerRoom[currentCornerRoomID]['hallway']
                cornerAdjRoomA = self.gameBoardCornerRoom[currentCornerRoomID]['adjacentRoomA']
                cornerAdjRoomB = self.gameBoardCornerRoom[currentCornerRoomID]['adjacentRoomB']

                #CornerNextMoveType3a: not suggestion
                if nextHallwayName != False and isSuggestion == False:
                    if nextHallwayID == cornerAdjHall:
                        isValidMove = True
                    else:
                        isValidMove = False
                        validationMesg = "Invalid home space to hallway move. Did you mean the hallway between " + cornerAdjRoomA.capitalize() + " and " + cornerAdjRoomB.capitalize() + "?"

                #CornerNextMoveType3b: suggestion
                elif nextHallwayName != False and isSuggestion:
                    isValidMove = True

            #CornerNextMoveType4: Validate player is going from corner room to a non-corner room, suggestion move
            elif nextRoomName in self.otherRooms:
                #If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid corner to non-corner room move."

        #Player is currently located in a hallway
        elif currentHallwayName != False:
            #HallwayNextMoveType1: Validate player is not going to hallway to hallway
            if nextHallwayName != False:
                isValidMove = False
                validationMesg = "Invalid hallway move."

            #HallwayNextMoveType2: Validate player is going from hallway to adjacent room
            else:
                hallAdjRoomA = self.gameBoardHallwaysDict[currentHallwayID]['adjacentRoomA']
                hallAdjRoomB = self.gameBoardHallwaysDict[currentHallwayID]['adjacentRoomB']

                if hallAdjRoomA == nextRoomName or hallAdjRoomB == nextRoomName:
                    isValidMove = True
                else:
                   isValidMove = False
                   validationMesg = "Invalid hallway to adjacent room move."

        #Else, located in a non-corner room
        else:
            #NextMoveType1: Validate player is going from non-corner room to adjacent hallway
            if nextHallwayName != False:
                currRoomHalls = self.gameBoardOtherRoom[currentRoomIdx]['adjacentHall']

                if nextHallwayID in currRoomHalls:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid room to hallway move."

            #NextMoveType2: Confirm player is going from non-corner room to non-corner room because of a suggestion
            elif nextRoomName in self.otherRooms:
                # If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid non-corner to non-corner room move."

            #NextMoveType3: Confirm player is going from non-corner room to corner room because of a suggestion
            elif nextCornerRoomName != False:
                # If move is a result of a suggestion, valid move
                if isSuggestion:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid non-corner to corner room move."

        #return validation result
        return isValidMove, validationMesg

    # validateWeaponMove(self, WeaponID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus)
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
    # postcondition: The method validates the weapon's next move. If the move
    #                 is valid, it returns True. If the move is invalid,
    #                 it returns False.
    #
    def validateWeaponMove(self, WeaponID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        return False

#END: Validator class