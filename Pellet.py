from GameObject import GameObject


class Pellet(GameObject):
    COLOR = (255, 255, 255)  # Weiß
    RADIUS = 2

    def __init__(self, x, y):
        super().__init__(x, y)