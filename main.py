#ChatGPT Threads:
#https://chat.openai.com/share/a86e367b-28c1-4293-8f7c-8eec79c80d59
#https://chat.openai.com/share/4f0fbbb7-6756-42a7-8345-c71dec94d2ab

import pygame
from Game import Game
from Level import Level


def main():
    # Erstellen Sie ein neues Spiel
    level = Level()
    game = Game(level=level)

    # Initialisierung von Pygame
    pygame.init()

    # Festlegung der Fenstergröße
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Festlegung des Fenstertitels
    pygame.display.set_caption("Pacman")

    # Starten Sie das Spiel
    game.start()

    # Beenden von Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
