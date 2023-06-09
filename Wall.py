from GameObject import GameObject


class Wall(GameObject):
    COLOR = (0, 0, 255)  # Blau

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
