from Pellet import Pellet


class PowerPellet(Pellet):
    COLOR = (255, 182, 193)  # Hellrosa
    def __init__(self, x, y):
        super().__init__(x, y)