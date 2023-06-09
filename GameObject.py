from globals import CELL_SIZE


class GameObject:
    def __init__(self, x, y):
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
