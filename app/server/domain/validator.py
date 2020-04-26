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
        #Corner Room dictionary
        self.gameBoardCornerRoom = {
            "study": {"id": 18, "name": "study", "isCornerRoom": 1, "type": "room",
                    "x_index": set(range(1, 4, 1)), "y_index": set(range(1, 4, 1))},
            "lounge": {"id": 16, "name": "lounge", "isCornerRoom": 1, "type": "room",
                    "x_index": set(range(9, 12, 1)), "y_index": set(range(1, 4, 1))},
            "conservatory": {"id": 14, "name": "conservatory", "isCornerRoom": 1, "type": "room",
                    "x_index": set(range(1, 4, 1)), "y_index": set(range(9, 12, 1))},
            "kitchen": {"id": 12, "name": "kitchen", "isCornerRoom": 1, "type": "room",
                    "x_index": set(range(9, 12, 1)), "y_index": set(range(9, 12, 1))}
        }

        #Non-Corner Room dictionary
        self.gameBoardOtherRoom = {
            0: {"id": 17, "name": "hall", "isCornerRoom": 0, "type": "room",
                    "x_index": set(range(5, 8, 1)), "y_index": set(range(1, 4, 1)), "adjacent_hall": ('A', 'B', 'D')},
            1: {"id": 19, "name": "library", "isCornerRoom": 0, "type": "room",
                    "x_index": set(range(1, 4, 1)), "y_index": set(range(5, 8, 1)), "adjacent_hall": ('C', 'F', 'H')},
            2: {"id": 20, "name": "billiard room", "isCornerRoom": 0, "type": "room",
                    "x_index": set(range(5, 8, 1)), "y_index": set(range(5, 8, 1)), "adjacent_hall": ('D', 'F', 'I', 'G')},
            3: {"id": 13, "name": "ball room", "isCornerRoom": 0, "type": "room",
                    "x_index": set(range(5, 8, 1)), "y_index": set(range(9, 12, 1)), "adjacent_hall": ('K', 'I', 'L')}
        }

        # build hallway dictionaries
        self.hallwayADict = {
            "id": 21,
            "name": "hallway a",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 4,
            "y_index": 2,
            "adjacent_room_a": "study",
            "adjacent_room_b": "hall"
        }
        self.hallwayBDict = {
            "id": 22,
            "name": "hallway b",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 8,
            "y_index": 2,
            "adjacent_room_a": "hall",
            "adjacent_room_b": "lounge"
        }
        self.hallwayCDict = {
            "id": 23,
            "name": "hallway c",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 2,
            "y_index": 4,
            "adjacent_room_a": "study",
            "adjacent_room_b": "library"
        }
        self.hallwayDDict = {
            "id": 25,
            "name": "hallway d",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 6,
            "y_index": 4,
            "adjacent_room_a": "hall",
            "adjacent_room_b": "billiard room"
        }
        self.hallwayEDict = {
            "id": 27,
            "name": "hallway e",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 10,
            "y_index": 4,
            "adjacent_room_a": "lounge",
            "adjacent_room_b": "dining room"
        }
        self.hallwayFDict = {
            "id": 24,
            "name": "hallway f",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 4,
            "y_index": 6,
            "adjacent_room_a": "library",
            "adjacent_room_b": "billiard room"
        }
        self.hallwayGDict = {
            "id": 26,
            "name": "hallway g",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 8,
            "y_index": 6,
            "adjacent_room_a": "billiard room",
            "adjacent_room_b": "dining room"
        }
        self.hallwayHDict = {
            "id": 28,
            "name": "hallway h",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 2,
            "y_index": 8,
            "adjacent_room_a": "library",
            "adjacent_room_b": "conservatory"
        }
        self.hallwayIDict = {
            "id": 29,
            "name": "hall i",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 6,
            "y_index": 8,
            "adjacent_room_a": "billiard room",
            "adjacent_room_b": "ball room"
        }
        self.hallwayJDict = {
            "id": 30,
            "name": "hallway j",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 10,
            "y_index": 8,
            "adjacent_room_a": "dining room",
            "adjacent_room_b": "kitchen"
        }
        self.hallwayKDict = {
            "id": 31,
            "name": "hallway k",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 4,
            "y_index": 10,
            "adjacent_room_a": "conservatory",
            "adjacent_room_b": "ball room"
        }
        self.hallwayLDict = {
            "id": 32,
            "name": "hallway l",
            "isCornerRoom": 0,
            "type": "hallway",
            "x_index": 8,
            "y_index": 10,
            "adjacent_room_a": "ball room",
            "adjacent_room_b": "kitchen"
        }
        self.gameBoardHallwaysDict = {
           21: {"id": "A", "name": "hallway a", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 4, "y_index": 2, "adjacent_room_a": "study", "adjacent_room_b": "hall"},
           22: {"id": "B", "name": "hallway b", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 8, "y_index": 2, "adjacent_room_a": "hall", "adjacent_room_b": "lounge"},
           23: {"id": "C", "name": "hallway c", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 2, "y_index": 4, "adjacent_room_a": "study", "adjacent_room_b": "library"},
           25: {"id": "D", "name": "hallway d", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 6, "y_index": 4, "adjacent_room_a": "hall", "adjacent_room_b": "billiard room"},
           27: {"id": "E", "name": "hallway e", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 10, "y_index": 4, "adjacent_room_a": "lounge", "adjacent_room_b": "dining room"},
           24: {"id": "F", "name": "hallway f", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 4, "y_index": 6, "adjacent_room_a": "library", "adjacent_room_b": "billiard room"},
           26: {"id": "G", "name": "hallway g", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 8, "y_index": 6, "adjacent_room_a": "billiard room", "adjacent_room_b": "dining room"},
           28: {"id": "H", "name": "hallway h", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 2, "y_index": 8, "adjacent_room_a": "library", "adjacent_room_b": "conservatory"},
           29: {"id": "I", "name": "hall i", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 6, "y_index": 8, "adjacent_room_a": "billiard room", "adjacent_room_b": "ball room"},
           30: {"id": "J", "name": "hallway j", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 10, "y_index": 8, "adjacent_room_a": "dining room", "adjacent_room_b": "kitchen"},
           31: {"id": "K", "name": "hallway k", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 4, "y_index": 10, "adjacent_room_a": "conservatory", "adjacent_room_b": "ball room"},
           32: {"id": "L", "name": "hallway l", "isCornerRoom": 0, "type": "hallway",
                    "x_index": 8, "y_index": 10, "adjacent_room_a": "ball room", "adjacent_room_b": "kitchen"}
        }

        # build home space dictionaries
        self.mrsWhiteHomeSpaceDict = {
            "id": 1,
            "name": "Mrs. White",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 8,
            "y_index": 12,
            "hallway": 'L',
            "adjacent_room_a": "ball room",
            "adjacent_room_b": "kitchen"
        }
        self.mrsGreenHomeSpaceDict = {
            "id": 5,
            "name": "Mr. Green",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 4,
            "y_index": 12,
            "hallway": 'K',
            "adjacent_room_a": "conservatory",
            "adjacent_room_b": "ball room"
        }
        self.mrsPeacockHomeSpaceDict = {
            "id": 2,
            "name": "Mrs. Peacock",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 0,
            "y_index": 8,
            "hallway": 'H',
            "adjacent_room_a": "library",
            "adjacent_room_b": "conservatory"
        }
        self.profPlumHomeSpaceDict = {
            "id": 4,
            "name": "Professor Plum",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 0,
            "y_index": 4,
            "hallway": 'C',
            "adjacent_room_a": "study",
            "adjacent_room_b": "library"
        }
        self.missScarlettHomeSpaceDict = {
            "id": 0,
            "name": "Miss Scarlet",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 8,
            "y_index": 0,
            "hallway": 'B',
            "adjacent_room_a": "hall",
            "adjacent_room_b": "lounge"
        }
        self.colMustardHomeSpaceDict = {
            "id": 3,
            "name": "Colonel Mustard",
            "isCornerRoom": 0,
            "type": "home space",
            "x_index": 12,
            "y_index": 4,
            "hallway": 'E',
            "adjacent_room_a": "lounge",
            "adjacent_room_b": "dining room"
        }
        self.gameBoardPlayersDict = {
            0: {"id": 0, "name": "Miss Scarlet", "isCornerRoom": 0, "type": "home space",
                    "x_index": 8, "y_index": 0, "hallway": 'B', "adjacent_room_a": "hall",
                    "adjacent_room_b": "lounge"},
            1: {"id": 1, "name": "Mrs. White", "isCornerRoom": 0, "type": "home space",
                    "x_index": 8, "y_index": 12, "hallway": 'L', "adjacent_room_a": "ball room",
                    "adjacent_room_b": "kitchen"},
            2: {"id": 2, "name": "Mrs. Peacock", "isCornerRoom": 0, "type": "home space",
                    "x_index": 0, "y_index": 8, "hallway": 'H', "adjacent_room_a": "library",
                    "adjacent_room_b": "conservatory"},
            3: {"id": 3, "name": "Colonel Mustard", "isCornerRoom": 0, "type": "home space",
                    "x_index": 12, "y_index": 4, "hallway": 'E', "adjacent_room_a": "lounge",
                    "adjacent_room_b": "dining room",},
            4: {"id": 4, "name": "Professor Plum", "isCornerRoom": 0, "type": "home space",
                    "x_index": 0, "y_index": 4, "hallway": 'C', "adjacent_room_a": "study",
                    "adjacent_room_b": "library"},
            5: {"id": 5, "name": "Mr. Green", "isCornerRoom": 0, "type": "home space",
                    "x_index": 4, "y_index": 12, "hallway": 'K', "adjacent_room_a": "conservatory",
                    "adjacent_room_b": "ball room"}
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
    #                it returns the room name. If not, it returns false.
    #
    def checkRoomCoordRange(self, positionx, positiony):
        roomResult = False

        # Set roomResult value based on the x and y coordinates
        if positionx in self.gameBoardCornerRoom['study']['x_index'] and positiony in self.gameBoardCornerRoom['study']['y_index']:
            roomResult = self.gameBoardCornerRoom['study']['name']
        elif positionx in self.gameBoardCornerRoom['lounge']['x_index'] and positiony in self.gameBoardCornerRoom['lounge']['y_index']:
            roomResult = self.gameBoardCornerRoom['lounge']['name']
        elif positionx in self.gameBoardCornerRoom['kitchen']['x_index'] and positiony in self.gameBoardCornerRoom['kitchen']['y_index']:
            roomResult = self.gameBoardCornerRoom['kitchen']['name']
        elif positionx in self.gameBoardCornerRoom['conservatory']['x_index'] and positiony in self.gameBoardCornerRoom['conservatory']['y_index']:
            roomResult = self.gameBoardCornerRoom['conservatory']['name']
        else:
            roomResult = False

        # return result
        return roomResult

    # checkHomeSpaceCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a character's home space.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a character's home space. If so,
    #                it returns the character's name. If not, it returns false.
    #
    def checkHomeSpaceCoordRange(self, positionx, positiony):
        homeSpaceResult = False

        # Set homeSpaceResult value based on the x and y coordinates
        if (positionx == self.mrsWhiteHomeSpaceDict['x_index']) and (positiony == self.mrsWhiteHomeSpaceDict['y_index']):
            homeSpaceResult = self.mrsWhiteHomeSpaceDict['id']
        elif (positionx == self.mrsGreenHomeSpaceDict['x_index']) and (positiony == self.mrsGreenHomeSpaceDict['y_index']):
            homeSpaceResult = self.mrsGreenHomeSpaceDict['id']
        elif (positionx == self.mrsPeacockHomeSpaceDict['x_index']) and (positiony == self.mrsPeacockHomeSpaceDict['y_index']):
            homeSpaceResult = self.mrsPeacockHomeSpaceDict['id']
        elif (positionx == self.profPlumHomeSpaceDict['x_index']) and (positiony == self.profPlumHomeSpaceDict['y_index']):
            homeSpaceResult = self.profPlumHomeSpaceDict['id']
        elif (positionx == self.missScarlettHomeSpaceDict['x_index']) and (positiony == self.missScarlettHomeSpaceDict['y_index']):
            homeSpaceResult = self.missScarlettHomeSpaceDict['id']
        elif (positionx == self.colMustardHomeSpaceDict['x_index']) and (positiony == self.colMustardHomeSpaceDict['y_index']):
            homeSpaceResult = self.colMustardHomeSpaceDict['id']
        else:
            homeSpaceResult = False

        # return result
        return homeSpaceResult

    # checkHallwayCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a hallway.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a hallway. If so,
    #                it returns True. If not, it returns False.
    #
    def checkHallwayCoordRange(self, positionx, positiony):
        hallwayID = None
        hallwayResult = 0


        # Set hallwayResult value based on the x and y coordinates
        if positionx == self.hallwayADict['x_index'] and positiony == self.hallwayADict['y_index'] or \
                positionx == self.hallwayBDict['x_index'] and positiony == self.hallwayBDict['y_index'] or \
                positionx == self.hallwayCDict['x_index'] and positiony == self.hallwayCDict['y_index'] or \
                positionx == self.hallwayDDict['x_index'] and positiony == self.hallwayDDict['y_index'] or \
                positionx == self.hallwayEDict['x_index'] and positiony == self.hallwayEDict['y_index'] or \
                positionx == self.hallwayFDict['x_index'] and positiony == self.hallwayFDict['y_index'] or \
                positionx == self.hallwayGDict['x_index'] and positiony == self.hallwayGDict['y_index'] or \
                positionx == self.hallwayHDict['x_index'] and positiony == self.hallwayHDict['y_index'] or \
                positionx == self.hallwayIDict['x_index'] and positiony == self.hallwayIDict['y_index'] or \
                positionx == self.hallwayJDict['x_index'] and positiony == self.hallwayJDict['y_index'] or \
                positionx == self.hallwayKDict['x_index'] and positiony == self.hallwayKDict['y_index'] or \
                positionx == self.hallwayLDict['x_index'] and positiony == self.hallwayLDict['y_index']:

            #determine which hallway
            for j in range(21, 33, 1):
                if self.gameBoardHallwaysDict[j]["x_index"] == positionx and \
                   self.gameBoardHallwaysDict[j]["y_index"] == positiony:
                    hallwayID = self.gameBoardHallwaysDict[j]["id"]
                    break

            hallwayResult = True

        #Set to false, not in hallway
        else:
            hallwayResult = False

        #return results
        return hallwayResult, hallwayID

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
    #
    def validatePlayerMove(self, PlayerID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        validationMesg = None
        isValidMove = False
        currentRoomIdx = 0

        #Get current player's location
        (curr_player_x, curr_player_y) = player.Player.get_coordinates(PlayerID)

        #Determine whether current location is either corner room or hallway
        currentCornerRoomName = self.checkRoomCoordRange(currPositionx, currPositiony)
        (currentIsHallway, currentHallwayID) = self.checkHallwayCoordRange(currPositionx, currPositiony)
        currentIsCharacterHomeSpace = self.checkHomeSpaceCoordRange(currPositionx, currPositiony)

        #Determine whether  next location is either corner room or hallway
        nextCornerRoomName = self.checkRoomCoordRange(nextCoordx, nextCoordy)
        (nextIsHallway, nextHallwayID) = self.checkHallwayCoordRange(nextCoordx, nextCoordy)
        nextIsCharacterHomeSpace = self.checkHomeSpaceCoordRange(nextCoordx, nextCoordy)

        #Begin: If other room, set value for current and/or next room names
        if currentCornerRoomName == False and currentIsHallway == False and \
            currentIsCharacterHomeSpace == False:
            # determine which other room
            for k in range(1, 4, 1):
                if currPositionx in self.gameBoardOtherRoom[k]['x_index'] and \
                    currPositiony in self.gameBoardOtherRoom[k]['y_index']:
                    currentRoomIdx = k
                    currentRoomID = self.gameBoardOtherRoom[k]["id"]
                    break

        if nextCornerRoomName == False and nextIsHallway == False and \
            nextIsCharacterHomeSpace == False:
            # determine which other room
            for l in range(1, 4, 1):
                if nextCoordx in self.gameBoardOtherRoom[l]["x_index"] and \
                    nextCoordy in self.gameBoardOtherRoom[l]["y_index"]:
                    nextRoomName = self.gameBoardOtherRoom[l]["name"]
                    break
        #End: If other room, set value for current and/or next room names


        #Player is moving from home space
        if currentIsCharacterHomeSpace != False:
            homeAdjHall = self.gameBoardPlayersDict[currentIsCharacterHomeSpace]["hallway"]
            homeAdjRoomA = self.gameBoardPlayersDict[currentIsCharacterHomeSpace]["adjacent_room_a"]
            homeAdjRoomB = self.gameBoardPlayersDict[currentIsCharacterHomeSpace]["adjacent_room_b"]

            #HomeNextMoveType1: Player is moving from home space to hallway, first move (not suggestion)
            if nextIsHallway and isSuggestion == False:
                if nextHallwayID == homeAdjHall:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid home space to hallway move. Did you mean the hallway between " + homeAdjRoomA.capitalize() + " and " + homeAdjRoomB.capitalize() + "?"

            #HomeNextMoveType2: Player is moving from home space to hallway, first move (suggestion)
            elif nextIsHallway and isSuggestion:
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
            elif nextIsHallway:
                cornerAdjHall = self.gameBoardCornerRoom[currentCornerRoomName]["hallway"]
                cornerAdjRoomA = self.gameBoardCornerRoom[currentCornerRoomName]["adjacent_room_a"]
                cornerAdjRoomB = self.gameBoardCornerRoom[currentCornerRoomName]["adjacent_room_b"]

                #CornerNextMoveType3a: not suggestion
                if nextIsHallway and isSuggestion == False:
                    if nextHallwayID == cornerAdjHall:
                        isValidMove = True
                    else:
                        isValidMove = False
                        validationMesg = "Invalid home space to hallway move. Did you mean the hallway between " + cornerAdjRoomA.capitalize() + " and " + cornerAdjRoomB.capitalize() + "?"

                #CornerNextMoveType3b: suggestion
                elif nextIsHallway and isSuggestion:
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
        elif currentIsHallway:
            #HallwayNextMoveType1: Validate player is not going to hallway to hallway
            if nextIsHallway == True:
                isValidMove = False
                validationMesg = "Invalid hallway move."

            #HallwayNextMoveType2: Validate player is going from hallway to adjacent room
            else:
                hallAdjRoomA = self.gameBoardHallwaysDict[currentHallwayID]["adjacent_room_a"]
                hallAdjRoomB = self.gameBoardHallwaysDict[currentHallwayID]["adjacent_room_b"]

                if hallAdjRoomA == nextRoomName or hallAdjRoomB == nextRoomName:
                    isValidMove = True
                else:
                   isValidMove = False
                   validationMesg = "Invalid hallway to adjacent room move."

        #Else, located in a non-corner room
        else:
            #NextMoveType1: Validate player is going from non-corner room to adjacent hallway
            if nextIsHallway == True:
                currRoomHalls = self.gameBoardOtherRoom[currentRoomIdx]["adjacent_hall"]

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
            elif nextCornerRoomName != "false":
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
    #
    def validateWeaponMove(self, WeaponID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion, GameBoardStatus):
        return False

#END: Validator class