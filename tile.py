import pygame

import constants

class Tile(pygame.sprite.Sprite):    
    def __init__(self, y, x, size, tile_type):
        super().__init__()
        self.size = size
        self.tile_type = tile_type
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (y, x)
        self.image.fill(constants.GREY)
