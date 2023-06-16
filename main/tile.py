import pygame, sys
from settings import *

#C:/Users/Fjodor/Projects/FirstGameEverMade/FirstGameEverMade/main/graphics/test/tile.png

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('main/graphics/test/tile.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)