class GameRules:
    moves = {'left': (0, 0, 0, 1), 'right': (0, 0, 1, 0), 'up': (1, 0, 0, 0), 'down': (0, 1, 0, 0)}

    def move(self, direction):
        return self.moves[direction]
