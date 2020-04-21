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

        suggestion_cards = suggestion.get_card_ids()
        for player in self.player_list:
            player_card_ids = player.get_card_ids()
            for i in range(0, 3):
                if suggestion_cards[i] == player_card_ids[i]:
                    return self.deck.get_card_data_by_id(player_card_ids[i])

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

    # TODO add move player validation
    def validatePlayerMove(self):
        return True

    # TODO how will client send this data?
    def move_player(self, player_id, x_coordinate, y_coordinate):
        player = self.player_list[player_id]
        if self.validatePlayerMove() is True:
            self.game_board_status.board[player.y_coordinate][player.x_coordinate] = 'b'
            player.update_coordinates(x_coordinate, y_coordinate)
            self.game_board_status.board[player.y_coordinate][player.x_coordinate] = player_id

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
