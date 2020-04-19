class GamePiece:
    def __init__(self, game_piece_id, x_coordinate, y_coordinate):
        self.id = game_piece_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def update_coordinates(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
