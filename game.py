import pygame
import random

from tile import Tile
import constants

class Game:
    def __init__(self, surface, width, height, size):
        self.surface = surface
        self.width = width
        self.height = height
        self.all_sprites = pygame.sprite.Group()
        self.grid = self.generate_map(size)

    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.all_sprites.draw(self.surface)

    def generate_map(self, size):
        schema = [[0 for x in range(0, size)] for y in range(0, size)] 
        schema = self.plant_random_bomb_in_schema(schema, size, size * 2)
        schema = self.set_numbers_near_bombs(schema, size)
        self.add_sprites_from_schema(schema, size)

    def add_sprites_from_schema(self, schema, size):
        for y in range(0, size):
            for x in range(0, size):
                tile_size = (self.width // size) - 1
                tile = Tile(y * (tile_size + 1), x * (tile_size + 1), tile_size, schema[y][x])
                self.all_sprites.add(tile)
    
    def printer(self, grid):
        for line in grid:
            print(line)

    def set_numbers_near_bombs(self, schema, size):
        """
        ( x,  y)
        (-1, -1) (0, -1) (1, -1)   
        (-1,  0) (0,  0) (1,  0)
        (-1,  1) (0,  1) (1,  1)
        """
        neighbour = [(1, 1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (-1, -1)]
        for y, line in enumerate(schema):
            for x, item in enumerate(line):
                number_of_bomb_near = 0
                if schema[y][x] == constants.TILE_TYPE_BOMB:
                    continue
                for neighbour_pos in neighbour:
                    if (neighbour_pos[0] + y >= 0 and neighbour_pos[0] + y < size and
                        neighbour_pos[1] + x >= 0 and neighbour_pos[1] + x < size): 
                            if schema[y + neighbour_pos[0]][x + neighbour_pos[1]] == constants.TILE_TYPE_BOMB:
                                number_of_bomb_near += 1
                schema[y][x] = number_of_bomb_near
        return schema


    def plant_random_bomb_in_schema(self, schema, size, nb_of_bomb):
        for i in range(0, nb_of_bomb):
            schema[random.randrange(0, size, 1)][random.randrange(0, size, 1)] = constants.TILE_TYPE_BOMB
        return schema