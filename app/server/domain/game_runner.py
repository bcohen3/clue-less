from app.server.domain import validator
from app.server.domain import player

class GameRunner:
    def __init__(self, deck, envelope, player_list, weapon_list, game_board):
        self.deck = deck
        self.envelope = envelope
        self.player_list = player_list
        self.weapon_list = weapon_list
        self.current_player = player_list[0]
        self.game_board_status = game_board

    def check_suggestion(self, suggestion):
        suspect_id = suggestion.suspect_card.id
        room_id = suggestion.room_card.id

        self.move_to_room(suspect_id, room_id)

        suggestion_cards = set(suggestion.get_card_ids())
        for player in self.player_list:
            player_card_ids = player.get_card_ids()
            player_cars = set(player_card_ids)
            shared = suggestion_cards & player_cars
            if shared:
                return self.deck.get_card_data_by_id(shared.pop())

        return None

    def move_to_room(self, player_id, room_id):
        free_spot = self.game_board_status.find_free_spot_in_room(room_id)
        x_coordinate = free_spot.x_coordinate
        y_coordinate = free_spot.y_coordinate

        self.move_player(player_id, x_coordinate, y_coordinate)

    def check_accusation(self, accusation):
        if set(accusation.get_card_ids()) == set(self.envelope.get_card_ids()):
            self.current_player.is_winner = True
        else:
            self.current_player.is_loser = True

        return self.current_player.is_winner

    # validatePlayerMove(self, player_id, x_coordinate, y_coordinate):
    #
    # This method accepts three parameters and validates the player's next move.
    #
    # @param player_id integer representing the Player's unique ID
    # @param x_coordinate integer representing the Player's next position, x coordinate
    # @param y_coordinate integer representing the Player's next position, y coordinate
    #
    # postcondition: The method validates the player's next move. If the move
    #                 is valid, it returns True. If the move is invalid,
    #                 it returns False.
    #
    def validatePlayerMove(self, player_id, x_coordinate, y_coordinate):
        curr_player_id = player_id
        (curr_player_x, curr_player_y) = player.Player.get_coordinates(curr_player_id)

        checkMove = validator.Validator(curr_player_id, x_coordinate, y_coordinate)
        isValid = checkMove.validatePlayerMove(curr_player_id, curr_player_x, curr_player_y, x_coordinate, y_coordinate, False,  self.game_board_status)
        return isValid

    # move_player(self, player_id, x_coordinate, y_coordinate):
    #
    # This method accepts three parameters and moves the player to the next location, if valid.
    #
    # @param player_id integer representing the Player's unique ID
    # @param x_coordinate integer representing the Player's next position, x coordinate
    # @param y_coordinate integer representing the Player's next position, y coordinate
    #
    # postcondition: The method moves the player to the next location if valid. If the move
    #                 is valid. If move was successful, it returns True. If the move is invalid,
    #                 it returns False.
    #
    def move_player(self, player_id, x_coordinate, y_coordinate):
        isValidMove = False
        validation_message = None
        curr_player = self.player_list[player_id]
        (curr_player_x, curr_player_y) = player.Player.get_coordinates(curr_player)

        # Validate whether move and if valid, move player
        (isValidMove, validation_message) = self.validatePlayerMove(curr_player, x_coordinate, y_coordinate)

        if isValidMove:
            # set previous space to blank
            self.game_board_status.board[curr_player_y][curr_player_x] = 'b'

            #update current player's location to new coordinates
            player.Player.update_coordinates(self, x_coordinate, y_coordinate)

            #update new location to curent player
            self.game_board_status.board[y_coordinate][x_coordinate] = player_id

            return True, validation_message
        else:
            return False, validation_message

    # TODO add move weapon validation
    def validate_weapon_move(self):
        return True

    def get_weapon_by_id(self, weapon_id):
        for weapon in self.weapon_list:
            if weapon.id == weapon_id:
                return weapon

    # TODO move weapon to room when suggestion is made
    def move_weapon(self, weapon_id, x_coordinate, y_coordinate):
        if self.validate_weapon_move() is True:
            weapon = self.get_weapon_by_id(weapon_id)
            self.game_board_status.board[weapon.x_coordinate][weapon.y_coordinate] = 'b'
            weapon.up_coordinatea(x_coordinate, y_coordinate)
            self.game_board_status.board[weapon.x_coordinate][weapon.y_coordinate] = weapon_id

    def update_current_player(self):
        current_player_id = self.current_player.id
        next_player_id = current_player_id + 1

        while self.player_list[next_player_id].is_loser is True:
            next_player_id += 1

        self.current_player = self.player_list[next_player_id]
