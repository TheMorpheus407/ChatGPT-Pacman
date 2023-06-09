from MovableObject import MovableObject


class Ghost(MovableObject):
    COLORS = {
        'blinky': (255, 0, 0),
        'pinky': (255, 105, 180),
        'inky': (0, 255, 255),
        'clyde': (255, 165, 0)
    }

    def __init__(self, x, y, color, game):
        super().__init__(x, y, game)
        self.color = color
        self.start_x = self.x
        self.start_y = self.y
        self.did_move = False
        self.alive = True
        self.respawn_timer = 30

    def respawn(self):
        self.alive = True
        self.respawn_timer = 30
        self.x, self.y = self.start_x, self.start_y

    def auto_move(self):
        if not self.alive:
            self.respawn_timer -= 1
            if self.respawn_timer <= 0:
                self.respawn()
            self.did_move = True
            return
        if self.did_move:
            self.did_move = False
            return
        best_distance = None
        best_move = None
        for direction in ['up', 'down', 'left', 'right']:
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
            collision_with_wall = False
            for wall in self.game.walls:
                if self.game.check_collision(self, wall):
                    collision_with_wall = True
                    break

            if not collision_with_wall:
                distance_to_pacman = abs(self.x - self.game.pacman.x) + abs(self.y - self.game.pacman.y)
                if best_distance is None or \
                        (self.game.pacman.powered_up and distance_to_pacman > best_distance) or \
                        (not self.game.pacman.powered_up and distance_to_pacman < best_distance):
                    best_distance = distance_to_pacman
                    best_move = direction

            # Setze die Koordinaten zurück auf die alten Werte
            self.x, self.y = old_x, old_y

        if best_move is not None:
            # Bewege den Geist in die beste Richtung
            super().move(best_move)
            self.did_move = True