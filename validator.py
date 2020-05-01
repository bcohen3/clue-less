from app.server.domain.game_board import GameBoard
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

        #non-corner rooms list
        self.otherRooms = {GameBoard.gameBoardOtherRoomDict[0]['name'],
                            GameBoard.gameBoardOtherRoomDict[1]['name'],
                            GameBoard.gameBoardOtherRoomDict[2]['name'],
                            GameBoard.gameBoardOtherRoomDict[3]['name']}

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
        for i in range(5, 9, 1):
            if positionx in GameBoard.gameBoardCornerRoomDict[i]['xIndex']  and \
                    positiony in GameBoard.gameBoardCornerRoomDict[i]['yIndex']:
                roomCornerResultID = GameBoard.gameBoardCornerRoomDict[i]['id']
                roomCornerResultName = GameBoard.gameBoardCornerRoomDict[i]['name']
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
            if GameBoard.gameBoardPlayersDict[i]['xIndex'] == positionx and \
                    GameBoard.gameBoardPlayersDict[i]['yIndex'] == positiony:
                homeSpaceResultID = GameBoard.gameBoardPlayersDict[i]['id']
                homeSpaceResultName = GameBoard.gameBoardPlayersDict[i]['name']
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
            if GameBoard.gameBoardHallwaysDict[j]['xIndex'] == positionx and \
                   GameBoard.gameBoardHallwaysDict[j]['yIndex'] == positiony:
                hallwayResultID = GameBoard.gameBoardHallwaysDict[j]['id']
                hallwayResultName = GameBoard.gameBoardHallwaysDict[j]['name']
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
        nextRoomName = None

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
            for k in range(0, 5, 1):
                if currPositionx in GameBoard.gameBoardOtherRoomDict[k]['xIndex'] and \
                    currPositiony in GameBoard.gameBoardOtherRoomDict[k]['yIndex']:
                    currentRoomIdx = k
                    currentRoomID = GameBoard.gameBoardOtherRoomDict[k]["id"]
                    break

        if nextCornerRoomName == False and nextHallwayName == False and \
            nextCharacterHomeSpaceName == False:

            # determine which other room: next
            for m in range(0, 5, 1):
                if nextCoordx in GameBoard.gameBoardOtherRoomDict[m]['xIndex'] and \
                    nextCoordy in GameBoard.gameBoardOtherRoomDict[m]['yIndex']:
                    nextRoomName = GameBoard.gameBoardOtherRoomDict[m]["name"]
                    break
        #End: If other room, set value for current and next movement

        #Player is moving from home space
        if currentCharacterHomeSpaceID != -1:
            homeAdjHall = GameBoard.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentHallway']
            homeAdjRoomA = GameBoard.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentRoomA']
            homeAdjRoomB = GameBoard.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentRoomB']

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
                cornerAdjHall = GameBoard.gameBoardCornerRoomDict[int(currentCornerRoomID)]['adjacentHall']
                cornerAdjRoomA = GameBoard.gameBoardCornerRoomDict[int(currentCornerRoomID)]['adjacentRoomA']
                cornerAdjRoomB = GameBoard.gameBoardCornerRoomDict[int(currentCornerRoomID)]['adjacentRoomB']

                #CornerNextMoveType3a: not suggestion
                if nextHallwayName != False and isSuggestion == False:
                    if nextHallwayName in cornerAdjHall:
                        isValidMove = True
                    else:
                        isValidMove = False
                        validationMesg = "Invalid corner room to hallway move. Did you mean the hallway between " + cornerAdjRoomA.capitalize() + " and " + cornerAdjRoomB.capitalize() + "?"

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
                hallAdjRoomA = GameBoard.gameBoardHallwaysDict[int(currentHallwayID)]['adjacentRoomA']
                hallAdjRoomB = GameBoard.gameBoardHallwaysDict[int(currentHallwayID)]['adjacentRoomB']

                if nextCornerRoomName != False and hallAdjRoomA == nextCornerRoomName or hallAdjRoomB == nextCornerRoomName:
                    isValidMove = True
                elif nextCornerRoomName == False and hallAdjRoomA == nextRoomName or hallAdjRoomB == nextRoomName:
                    isValidMove = True
                else:
                   isValidMove = False
                   validationMesg = "Invalid hallway to adjacent room move."

        #Else, located in a non-corner room
        else:
            #NextMoveType1: Validate player is going from non-corner room to adjacent hallway
            if nextHallwayName != False:
                currRoomHalls = GameBoard.gameBoardOtherRoomDict[currentRoomIdx]['adjacentHall']

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


    # findValidLocations(self, playerID)
    #
    # This method accepts one parameter. It suggests where the player can move.
    #
    # @param playerID integer representing the x coordinate position
    #
    # postcondition: The method determines valid location(s) for the player. It returns their IDs and names.
    #
    def findValidLocations(self, playerID):
       locationResultList = []
       roomsOnlyDict = GameBoard.gameBoardCornerRoomDict.copy()
       roomsOnlyDict.update(GameBoard.gameBoardOtherRoomDict)

       (currPositionx, currPositiony) = player.Player.get_coordinates(playerID)
       (HallwayID, HallwayName) = self.checkHallwayCoordRange(currPositionx, currPositiony)
       (CharacterHomeSpaceID, CharacterHomeSpaceName) = self.checkHomeSpaceCoordRange(currPositionx, currPositiony)

       # Home space - hallway list
       if CharacterHomeSpaceID != -1:
          location = GameBoard.gameBoardPlayersDict[CharacterHomeSpaceID]['adjacentHallway']

          for p in range(21, 33, 1):
             if GameBoard.gameBoardHallwaysDict[p]['name'] == location:
                locationResultList.append(GameBoard.gameBoardHallwaysDict[p]['id'])
                locationResultList.append(GameBoard.gameBoardHallwaysDict[p]['name'])
                break

       # Hallway location - room list
       elif HallwayID != -1:
          locations = [GameBoard.gameBoardHallwaysDict[int(HallwayID)]['adjacentRoomA'],
                       GameBoard.gameBoardHallwaysDict[int(HallwayID)]['adjacentRoomB']]

          for location in locations:
             for p in range(0, 9, 1):
                if roomsOnlyDict[p]['name'] == location:
                   locationResultList.append(roomsOnlyDict[p]['id'])
                   locationResultList.append(roomsOnlyDict[p]['name'])

       # Room location - hallway list
       else:
          for q in range(0, 9, 1):
             if currPositionx in roomsOnlyDict[q]['xIndex'] and \
                     currPositiony in roomsOnlyDict[q]['yIndex']:

                locations = [roomsOnlyDict[q]['adjacentHall']]

                for location in locations:
                   locationResultList.append(roomsOnlyDict[q]['id'])
                   locationResultList.append(roomsOnlyDict[q]['name'])

       return locationResultList

#END: Validator class