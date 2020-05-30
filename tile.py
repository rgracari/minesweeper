import pygame

import constants

class Tile(pygame.sprite.Sprite):
    def __init__(self, y, x, size, tile_type):
        super().__init__()
        self.tile_type = tile_type
        self.image = pygame.Surface((size, size))
        if tile_type == constants.TILE_TYPE_BOMB:
            self.image.fill(constants.RED)
        else:
            self.image.fill(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (y, x)
    
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.tile_type == constants.TILE_TYPE_BOMB:
                print("BOOOOMB")