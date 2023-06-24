import pygame, sys
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('main/graphics/test/tile.png').convert_alpha()
        #self.image = pygame.image.load('main/graphics/test/tile.png').set_colorkey(pygame.Color(223, 72, 197))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)