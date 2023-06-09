import sys

import pygame

from Pacman import Pacman
from Ghost import Ghost
from Pellet import Pellet
from PowerPellet import PowerPellet
from Wall import Wall
from globals import CELL_SIZE


class Game:
    def __init__(self, level):
        self.game_over = False
        self.level = level
        self.width = len(level.grid[0])
        self.height = len(level.grid)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.walls = []
        self.pellets = []
        self.power_pellets = []
        self.ghosts = []
        self.pacman = Pacman(1, 1, self)  # Erstelle Pacman an der Position (0, 0) mit Geschwindigkeit 2
        self.score = 0
        self.init_level()
        self.won = False
        self.power_pellet_img = pygame.transform.scale(pygame.image.load('powerpellet.png'), (CELL_SIZE, CELL_SIZE))
        self.ghost_img = pygame.transform.scale(pygame.image.load('ghost.png'), (CELL_SIZE, CELL_SIZE))
        self.pacman_img = pygame.transform.scale(pygame.image.load('pacman.png'), (CELL_SIZE, CELL_SIZE))


    def init_level(self):
        for y, row in enumerate(self.level.grid):
            for x, cell in enumerate(row):
                if cell == 'W':
                    self.walls.append(Wall(x, y, 1, 1))
                elif cell == 'P':
                    self.pellets.append(Pellet(x, y))
                elif cell == 'U':
                    self.power_pellets.append(PowerPellet(x, y))
                elif cell == 'G':
                    self.pellets.append(Pellet(x, y))
                    ghost = Ghost(x, y, list(Ghost.COLORS.keys())[len(self.ghosts) % len(Ghost.COLORS)], self)
                    self.ghosts.append(ghost)

    def start(self):
        running = True
        while running:
            # Ereignisverarbeitung
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pacman.move('up')
            elif keys[pygame.K_DOWN]:
                self.pacman.move('down')
            elif keys[pygame.K_LEFT]:
                self.pacman.move('left')
            elif keys[pygame.K_RIGHT]:
                self.pacman.move('right')

            self.update_game_state()
            if self.game_over:
                self.print_gameover_state()
            # Zum Beispiel, wir könnten das Level erneut zeichnen und dann Pacman und die Geister zeichnen:
            self.draw()

            # Aktualisieren des Bildschirms
            pygame.display.flip()

            # Begrenzen der Framerate
            self.clock.tick(2)

    def pause(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Drücken Sie "P", um das Spiel zu pausieren/fortzusetzen
                        pause = not pause

    def stop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def check_collision(self, movable_object, game_object):
        return movable_object.x == game_object.x and movable_object.y == game_object.y

    def update_game_state(self):
        # Prüfe auf Kollisionen zwischen Pacman und jedem Geist
        for ghost in self.ghosts:
            ghost.auto_move()
            if ghost.alive and self.check_collision(self.pacman, ghost):
                if self.pacman.powered_up:  # Wenn Pacman ein PowerPellet gegessen hat
                    print("Pacman hat einen Geist gefressen!")
                    ghost.respawn_timer = 30
                    ghost.alive = False
                    self.score += 10  # Erhöhe die Punktzahl deutlich mehr, wenn ein Geist gefressen wird
                else:
                    print("Pacman wurde von einem Geist erwischt!")
                    self.game_over = True
                    break  # Beende die Schleife, wenn Pacman von einem Geist erwischt wurde

        for power_pellet in self.power_pellets:
            if self.check_collision(self.pacman, power_pellet):
                print("Pacman hat ein PowerPellet gegessen!")
                self.power_pellets.remove(power_pellet)
                self.pacman.powered_up = True  # Pacman ist nun im Power-Up-Modus
                self.pacman.powerup_timer = 30  # Setzen Sie den Timer auf 30 Frames

        # Aktualisieren Sie den Power-Up-Timer
        if self.pacman.powered_up:
            if self.pacman.powerup_timer > 0:
                self.pacman.powerup_timer -= 1
            else:
                self.pacman.powered_up = False


        # Prüfe auf Kollisionen zwischen Pacman und jedem Pellet
        for pellet in self.pellets:
            if self.check_collision(self.pacman, pellet):
                print("Pacman hat ein Pellet gegessen!")
                # Entferne das Pellet aus der Liste
                self.pellets.remove(pellet)
                # Ersetze das 'P' im Grid durch ein '.'
                self.level.grid[pellet.y // CELL_SIZE][pellet.x // CELL_SIZE] = '.'
                # Erhöhe die Punktzahl des Spielers
                self.score += 1

        # Wenn alle Pellets gegessen wurden, beende das Spiel als gewonnen
        if len(self.pellets) == 0:
            print("Herzlichen Glückwunsch! Sie haben alle Pellets gegessen und das Spiel gewonnen!")
            self.game_over = True
            self.won = True

    def draw(self):
        self.screen.fill((0, 0, 0))  # Füllt den gesamten Bildschirm mit Schwarz
        for wall in self.walls:
            position = pygame.Rect(wall.x, wall.y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, Wall.COLOR, position)
        for pellet in self.pellets:
            position = pygame.Rect(pellet.x, pellet.y, CELL_SIZE, CELL_SIZE)
            pygame.draw.circle(self.screen, Pellet.COLOR, (pellet.x + CELL_SIZE/2, pellet.y + CELL_SIZE/2), Pellet.RADIUS)
        for power_pellet in self.power_pellets:
            self.screen.blit(self.power_pellet_img, (power_pellet.x, power_pellet.y))
        for ghost in self.ghosts:
            if ghost.alive:
                self.screen.blit(self.ghost_img, (ghost.x, ghost.y))

        self.screen.blit(self.pacman_img, (self.pacman.x, self.pacman.y))

    def print_gameover_state(self):
        # Erstellen Sie eine Schriftart für die Spielinformationen
        font = pygame.font.Font(None, 36)

        # Zeichnen Sie ein graues, halbtransparentes Rechteck über das gesamte Spiel
        overlay = pygame.Surface(
            (self.screen.get_width(), self.screen.get_height()))  # Erstellen Sie eine neue Oberfläche
        overlay.set_alpha(204)  # Legen Sie die Transparenz auf 50%
        overlay.fill((50, 50, 50))  # Füllen Sie die Oberfläche mit Grau
        self.screen.blit(overlay, (0, 0))  # Zeichnen Sie die Oberfläche auf den Bildschirm

        # Erstellen Sie einen Text, der den Punktestand anzeigt
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        score_text_position = score_text.get_rect(centerx=self.screen.get_width() / 2,
                                                  centery=self.screen.get_height() / 2 - 50)

        # Erstellen Sie einen Text, der den Gewinnzustand anzeigt
        if self.won:
            gameover_text = font.render("Congratulations! You won the game!", True, (255, 255, 255))
        else:
            gameover_text = font.render("Game Over. You lost.", True, (255, 255, 255))
        gameover_text_position = gameover_text.get_rect(centerx=self.screen.get_width() / 2,
                                                        centery=self.screen.get_height() / 2)

        # Zeichnen Sie die Texte auf den Bildschirm
        self.screen.blit(score_text, score_text_position)
        self.screen.blit(gameover_text, gameover_text_position)

        # Aktualisieren des Bildschirms
        pygame.display.flip()

        # Warten Sie einige Sekunden, bevor Sie das Programm beenden
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

