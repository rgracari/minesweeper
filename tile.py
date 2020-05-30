import pygame

import constants

class Tile(pygame.sprite.Sprite):    
    def __init__(self, y, x, size, tile_type):
        super().__init__()
        print(tile_type)
        self.size = size
        self.tile_type = tile_type
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (y, x)
        self.image.fill(constants.GREY)

        # if tile_type == constants.TILE_TYPE_BOMB:
        #     self.image.fill(constants.RED)
        # else:
        
    
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.tile_type == constants.TILE_TYPE_BOMB:
                print("BOOOOMB")
            elif self.tile_type != constants.TILE_TYPE_DEFAULT:
                print("CLICK")
                self.image.fill(constants.WHITE)
                myfont = pygame.font.SysFont(constants.FONT, self.size // 2)
                text_surface = myfont.render(str(self.tile_type), True, (0, 0, 0))
                text_rect = text_surface.get_rect()
                text_rect.center = (self.size / 2, self.size / 2)
                self.image.blit(text_surface, text_rect)