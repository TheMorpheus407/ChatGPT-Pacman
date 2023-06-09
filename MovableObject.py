from GameObject import GameObject
from globals import CELL_SIZE

class MovableObject(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y)
        self.speed = CELL_SIZE
        self.game = game  # Referenz zum Game Objekt, um auf Wände und andere Spielobjekte zugreifen zu können

    def move(self, direction):
        # Kopiere die aktuellen Koordinaten, bevor wir versuchen, uns zu bewegen
        old_x, old_y = self.x, self.y

        # Versuche, dich zu bewegen
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

        # Prüfe auf Kollisionen mit Wänden
        for wall in self.game.walls:
            if self.game.check_collision(self, wall):
                # Bei Kollision mit einer Wand, setze die Koordinaten zurück auf die alten Werte
                self.x, self.y = old_x, old_y
                break
