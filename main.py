import pygame
import random

import constants
from game import Game

pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Minesweeper")
pygame.font.init()
clock = pygame.time.Clock()

game = Game(screen, constants.WIDTH, constants.HEIGHT, constants.DIFFICULTY_EASY)

running = True
while running:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP1:
                game = Game(screen, constants.WIDTH, constants.HEIGHT, constants.DIFFICULTY_EASY)
            elif event.key == pygame.K_KP2:
                game = Game(screen, constants.WIDTH, constants.HEIGHT, constants.DIFFICULTY_MEDIUM)
            elif event.key == pygame.K_KP3:
                game = Game(screen, constants.WIDTH, constants.HEIGHT, constants.DIFFICULTY_HARD)
                
    # Main Loop Functions
    screen.fill(constants.BLACK)
    game.update()
    game.draw()

    pygame.display.flip()

pygame.quit()