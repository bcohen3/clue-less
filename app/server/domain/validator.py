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
    def __init__(self, PlayerID, currPositionx, currPositiony, gameBoardStatus):
        self.PlayerID = PlayerID
        self.currPositionx = currPositionx
        self.currPositiony = currPositiony
        self.gameBoardStatus = gameBoardStatus

        #non-corner rooms list
        self.otherRooms = {self.gameBoardStatus.gameBoardOtherRoomDict[0]['name'],
                            self.gameBoardStatus.gameBoardOtherRoomDict[1]['name'],
                            self.gameBoardStatus.gameBoardOtherRoomDict[2]['name'],
                            self.gameBoardStatus.gameBoardOtherRoomDict[3]['name']}

    # checkRoomCoordRange(positionx, positiony)
    #
    # This method accepts two parameters and checks whether the coordinates are a corner room.
    #
    # @param positionx integer representing the x coordinate of the position
    # @param positiony integer representing the y coordinate of the position
    #
    # postcondition: The method checks whether the coordinates are a corner room. If so,
    #                it returns the room id and name. If not, it returns -1 and False.
    #
    def checkRoomCoordRange(self, positionx, positiony):
        roomCornerResultID = -1
        roomCornerResultName = False

        # Set room result values according to the x and y coordinates
        for i in range(5, 9, 1):
            if positionx in self.gameBoardStatus.gameBoardCornerRoomDict[i]['xIndex']  and \
                    positiony in self.gameBoardStatus.gameBoardCornerRoomDict[i]['yIndex']:
                roomCornerResultID = self.gameBoardStatus.gameBoardCornerRoomDict[i]['id']
                roomCornerResultName = self.gameBoardStatus.gameBoardCornerRoomDict[i]['name']
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
            if self.gameBoardStatus.gameBoardPlayersDict[i]['xIndex'] == positionx and \
                    self.gameBoardStatus.gameBoardPlayersDict[i]['yIndex'] == positiony:
                homeSpaceResultID = self.gameBoardStatus.gameBoardPlayersDict[i]['id']
                homeSpaceResultName = self.gameBoardStatus.gameBoardPlayersDict[i]['name']
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
            if self.gameBoardStatus.gameBoardHallwaysDict[j]['xIndex'] == positionx and \
                   self.gameBoardStatus.gameBoardHallwaysDict[j]['yIndex'] == positiony:
                hallwayResultID = self.gameBoardStatus.gameBoardHallwaysDict[j]['id']
                hallwayResultName = self.gameBoardStatus.gameBoardHallwaysDict[j]['name']
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
    def validatePlayerMove(self, PlayerID, currPositionx, currPositiony, nextCoordx, nextCoordy, isSuggestion):
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
                if currPositionx in self.gameBoardStatus.gameBoardOtherRoomDict[k]['xIndex'] and \
                    currPositiony in self.gameBoardStatus.gameBoardOtherRoomDict[k]['yIndex']:
                    currentRoomIdx = k
                    currentRoomID = self.gameBoardStatus.gameBoardOtherRoomDict[k]["id"]
                    break

        if nextCornerRoomName == False and nextHallwayName == False and \
            nextCharacterHomeSpaceName == False:

            # determine which other room: next
            for m in range(0, 5, 1):
                if nextCoordx in self.gameBoardStatus.gameBoardOtherRoomDict[m]['xIndex'] and \
                    nextCoordy in self.gameBoardStatus.gameBoardOtherRoomDict[m]['yIndex']:
                    nextRoomName = self.gameBoardStatus.gameBoardOtherRoomDict[m]["name"]
                    break
        #End: If other room, set value for current and next movement

        #Player is moving from home space
        if currentCharacterHomeSpaceID != -1:
            homeAdjHall = self.gameBoardStatus.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentHall']
            homeAdjRoomA = self.gameBoardStatus.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentRoomA']
            homeAdjRoomB = self.gameBoardStatus.gameBoardPlayersDict[int(currentCharacterHomeSpaceID)]['adjacentRoomB']

            #HomeNextMoveType1: Player is moving from home space to hallway, first move (not suggestion)
            if nextHallwayName != False and isSuggestion == False:
                if nextHallwayName == homeAdjHall:
                    isValidMove = True
                else:
                    isValidMove = False
                    validationMesg = "Invalid home space to hallway move. Did you mean the hallway between " + homeAdjRoomA.capitalize() + " and " + homeAdjRoomB.capitalize() + "?"

            # HomeNextMoveType2: Player is moving from home space to room, suggestion
            elif isSuggestion:
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
                for i in range(0, 9, 1):
                    if  self.gameBoardStatus.roomsOnlyDict[i]['id'] == currentCornerRoomID:
                        cornerAdjHall = self.gameBoardStatus.gameBoardCornerRoomDict[i]['adjacentHall']
                        cornerAdjRoomA = self.gameBoardStatus.gameBoardCornerRoomDict[i]['adjacentRoomA']
                        cornerAdjRoomB = self.gameBoardStatus.gameBoardCornerRoomDict[i]['adjacentRoomB']
                        break

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
                hallAdjRoomA = self.gameBoardStatus.gameBoardHallwaysDict[int(currentHallwayID)]['adjacentRoomA']
                hallAdjRoomB = self.gameBoardStatus.gameBoardHallwaysDict[int(currentHallwayID)]['adjacentRoomB']

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
                currRoomHalls = self.gameBoardStatus.gameBoardOtherRoomDict[currentRoomIdx]['adjacentHall']

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
       locationsMesg = None
       locationIsAvailable = None
       secretLocationIsAvailable = None

       (currPositionx, currPositiony) = player.Player.get_coordinates(playerID)
       (HallwayID, HallwayName) = self.checkHallwayCoordRange(currPositionx, currPositiony)
       (CharacterHomeSpaceID, CharacterHomeSpaceName) = self.checkHomeSpaceCoordRange(currPositionx, currPositiony)

       # Home space - hallway list
       if CharacterHomeSpaceID != -1:
          #get nearest hallway
          location = self.gameBoardStatus.gameBoardPlayersDict[CharacterHomeSpaceID]['adjacentHall']

          #loop through hallway list
          for p in range(21, 33, 1):
             if self.gameBoardStatus.gameBoardHallwaysDict[p]['name'] == location:
                # check location is available
                locationIsAvailable = self.gameBoardStatus.find_free_spot_in_room(self.gameBoardStatus.gameBoardHallwaysDict[p]['id'])

                # If so, include location in list
                if locationIsAvailable != None:
                    locationResultList.append(self.gameBoardStatus.gameBoardHallwaysDict[p]['id'])
                    locationResultList.append(self.gameBoardStatus.gameBoardHallwaysDict[p]['name'])
                    break
                else:
                    locationsMesg = "Hallway currently occupied."

       # Hallway location - room list
       elif HallwayID != -1:
          # Get rooms adjacent to hallway
          locations = [self.gameBoardStatus.gameBoardHallwaysDict[int(HallwayID)]['adjacentRoomA'],
                       self.gameBoardStatus.gameBoardHallwaysDict[int(HallwayID)]['adjacentRoomB']]

          # Loop through room list
          for location in locations:
             for q in range(0, 9, 1):
                if self.gameBoardStatus.roomsOnlyDict[q]['name'] == location:
                    # check location is available
                    locationIsAvailable = self.gameBoardStatus.find_free_spot_in_room(self.gameBoardStatus.roomsOnlyDict[q]['id'])

                    # If so, include location in list
                    if locationIsAvailable != None:
                        locationResultList.append(self.gameBoardStatus.roomsOnlyDict[q]['id'])
                        locationResultList.append(self.gameBoardStatus.roomsOnlyDict[q]['name'])
                    else:
                        locationsMesg = "Adjacent rooms currently full."

       # Room location - hallway list
       else:
          for u in range(0, 9, 1):
             if currPositionx in self.gameBoardStatus.roomsOnlyDict[u]['xIndex'] and \
                     currPositiony in self.gameBoardStatus.roomsOnlyDict[u]['yIndex']:

                # Get adjacent hallways
                locations = self.gameBoardStatus.roomsOnlyDict[u]['adjacentHall']

                # Loop through adjacent hallways list
                for location in locations:
                    # check location is available
                    for t in range(21, 33, 1):
                        if self.gameBoardStatus.gameBoardHallwaysDict[t]['name'] == location:
                            locationIsAvailable = self.gameBoardStatus.find_free_spot_in_room(self.gameBoardStatus.gameBoardHallwaysDict[t]['id'])
                            break

                    # If so, include hallway location in list
                    if locationIsAvailable != None:
                        locationResultList.append(self.gameBoardStatus.gameBoardHallwaysDict[t]['id'])
                        locationResultList.append(self.gameBoardStatus.gameBoardHallwaysDict[t]['name'])

                # Hallway is currently occupied, check if room is a corner room - secret passage
                if self.gameBoardStatus.roomsOnlyDict[u]['isCornerRoom'] == 1:

                    # Begin: Check secret passage availability
                    for passage in self.gameBoardStatus.passageCoords:
                        if self.gameBoardStatus.passageCoords[passage]['cornerRoom'] == \
                                    self.gameBoardStatus.gameBoardCornerRoomDict[u]['secretPassage']:

                            # Check secret passage room availability
                            secretLocationIsAvailable = self.gameBoardStatus.find_free_spot_in_room(self.gameBoardStatus.passageCoords[passage]['id'])

                            if secretLocationIsAvailable != None:
                                locationResultList.append(self.gameBoardStatus.passageCoords[passage]['id'])
                                locationResultList.append(self.gameBoardStatus.passageCoords[passage]['cornerRoom'])
                    # End: Check secret passage availability

                # Hallway is currently occupied, room is not a corner room
                if locationIsAvailable != None and self.gameBoardStatus.roomsOnlyDict[u]['isCornerRoom'] == 0:
                    locationsMesg = "Adjacent hallways are full."
                # Hallway is currently occupied and passage room is full
                elif locationIsAvailable != None and secretLocationIsAvailable == None:
                    locationsMesg = "Adjancent hallways and secret passage are occupied or full."

       return locationResultList, locationsMesg

#END: Validator class