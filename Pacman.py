from MovableObject import MovableObject


class Pacman(MovableObject):
    COLOR = (255, 255, 0)  # Gelb

    def __init__(self, x, y, game):
        self.powered_up = False
        self.powerup_timer = 0  # Timer für die Power-Up-Dauer
        super().__init__(x, y, game)
