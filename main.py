import pygame
import random

import constants
from game import Game

pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

game = Game(screen, constants.WIDTH, constants.HEIGHT)

running = True
while running:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Main Loop Functions
    game.update()
    game.draw()

    pygame.display.flip()

pygame.quit()