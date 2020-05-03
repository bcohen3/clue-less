from app.server.domain import validator
from app.server.domain import player
from app.server.domain import weapon

class GameRunner:
    def __init__(self, deck, envelope, player_list, weapon_list, game_board):
        self.deck = deck
        self.envelope = envelope
        self.player_list = player_list
        self.weapon_list = weapon_list
        self.current_player = player_list[0]
        self.game_board_status = game_board
        self.weapon_id = None

    def check_suggestion(self, suggestion):
        suspect_id = suggestion.suspect_card.id
        room_id = suggestion.room_card.id
        weapon_id = suggestion.weapon_card.id

        self.move_to_room(suspect_id, weapon_id, room_id, True)

        suggestion_cards = set(suggestion.get_card_ids())
        for player in self.player_list:
            player_card_ids = player.get_card_ids()
            player_cars = set(player_card_ids)
            shared = suggestion_cards & player_cars
            if shared:
                return self.deck.get_card_data_by_id(shared.pop())

        return None

    def move_to_room(self, player_id, weapon_id, room_id, is_suggestion):

        player_free_spot = self.game_board_status.find_free_spot_in_room(room_id)
        player_x_coordinate = player_free_spot.x_coordinate
        player_y_coordinate = player_free_spot.y_coordinate

        self.move_player(player_id, player_x_coordinate, player_y_coordinate, is_suggestion)

        #If weapon_id is not null
        if weapon_id != None:
            weapon_free_spot = self.game_board_status.find_free_spot_in_room(room_id)
            weapon_x_coordinate = weapon_free_spot.x_coordinate
            weapon_y_coordinate = weapon_free_spot.y_coordinate

            self.move_weapon(weapon_id, weapon_x_coordinate, weapon_y_coordinate)


    def check_accusation(self, accusation):
        if set(accusation.get_card_ids()) == set(self.envelope.get_card_ids()):
            self.current_player.is_winner = True
        else:
            self.current_player.is_loser = True

        return self.current_player.is_winner

    # validatePlayerMove(self, player_id, x_coordinate, y_coordinate, isSuggestion):
    #
    # This method accepts three parameters and validates the player's next move.
    #
    # @param player_id integer representing the Player's unique ID
    # @param x_coordinate integer representing the Player's next position, x coordinate
    # @param y_coordinate integer representing the Player's next position, y coordinate
    # @param isSuggestion boolean representing the whether the move request is a result of a suggestion
    #
    # postcondition: The method validates the player's next move. If the move
    #                 is valid, it returns True, message and suggestion locations. If the move is invalid,
    #                 it returns False.
    #
    def validate_move(self, player_id, x_coordinate, y_coordinate, is_suggestion):
        suggested_locations = None
        suggested_locations_mesg = None

        curr_player_id = player_id

        (curr_player_x, curr_player_y) = player.Player.get_coordinates(curr_player_id)
        check_move = validator.Validator(curr_player_id, x_coordinate, y_coordinate, self.game_board_status)
        (is_valid, validation_mesg) = check_move.validatePlayerMove(curr_player_id, curr_player_x, curr_player_y, x_coordinate, y_coordinate, is_suggestion)

        if not is_suggestion:
            (suggested_locations, suggested_locations_mesg) = check_move.findValidLocations(player_id)

        return is_valid, validation_mesg, suggested_locations, suggested_locations_mesg


    # move_player(self, player_id, x_coordinate, y_coordinate, isSuggestion):
    #
    # This method accepts four parameters and moves the player to the next location, if valid.
    #
    # @param player_id integer representing the Player's unique ID
    # @param x_coordinate integer representing the Player's next position, x coordinate
    # @param y_coordinate integer representing the Player's next position, y coordinate
    # @param isSuggestion boolean representing the whether the move request is a result of a suggestion
    #
    # postcondition: The method moves the player to the next location if valid.
    #                If move was successful, it returns True. If the move is invalid, it returns False.
    #
    def move_player(self, player_id, x_coordinate, y_coordinate, is_suggestion):
        is_valid_move = False
        validation_message = None
        curr_player_id = self.player_list[player_id]
        (curr_player_x, curr_player_y) = player.Player.get_coordinates(curr_player_id)

        # Validate move and if valid, move player
        (is_valid_move, validation_message, suggested_locations, suggested_locations_mesg) = self.validate_move(curr_player_id, x_coordinate, y_coordinate, is_suggestion)

        if is_valid_move:
            #set previous space to blank
            self.game_board_status.board[curr_player_y][curr_player_x] = 'b'

            # update current player's location to new coordinates
            player.Player.update_coordinates(self.current_player, x_coordinate, y_coordinate)

            #update new location to current player
            self.game_board_status.board[y_coordinate][x_coordinate] = player_id

            return True, validation_message, suggested_locations, suggested_locations_mesg

        else:
            return False, validation_message, suggested_locations, suggested_locations_mesg

    def get_weapon_by_id(self, weapon_id):
        for weapon in self.weapon_list:
            if weapon.id == weapon_id:
                return weapon

    # move_weapon(self, weapon_id, x_coordinate, y_coordinate):
    #
    # This method accepts three parameters and moves the weapon to the next location, if valid.
    #
    # @param weapon_id integer representing the Weapon's unique ID
    # @param x_coordinate integer representing the Weapon's next position, x coordinate
    # @param y_coordinate integer representing the Weapon's next position, y coordinate
    #
    # postcondition: The method moves the weapon to the next location if valid. If move was successful,
    #                it returns True. If the move is invalid, it returns False.
    #
    def move_weapon(self, weapon_id, x_coordinate, y_coordinate):
        curr_weapon_id = self.get_weapon_by_id(weapon_id)

        # Get weapon current location
        (curr_weapon_x, curr_weapon_y) = weapon.Weapon.get_coordinates(curr_weapon_id)

        # set previous space to blank
        self.game_board_status.board[curr_weapon_y][curr_weapon_x] = 'b'

        # update current player's location to new coordinates
        weapon.Weapon.update_coordinates(curr_weapon_id, x_coordinate, y_coordinate)

        # update new location to current weapon
        self.game_board_status.board[x_coordinate][y_coordinate] = weapon_id

    def update_current_player(self):
        current_player_id = self.current_player.id
        next_player_id = current_player_id + 1

        #If next player count does not exceed total number of elements in list
        if next_player_id <= len(self.player_list) - 1:
            while self.player_list[next_player_id].is_loser is True:
                next_player_id += 1

            self.current_player = self.player_list[next_player_id]

        #Else, reset and find next player
        else:
            next_player_id = 0
            while self.player_list[next_player_id].is_loser is True:
                next_player_id += 1

            self.current_player = self.player_list[next_player_id]

