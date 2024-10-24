import pygame

from util.SpriteLoader import SpriteLoader
from server.model.map.MapElement import MapElement

class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*64, y*64, 64, 64)
        self.sprite = SpriteLoader.loadSprite('tile')


    def isEmpty(self):
        return True

    def whoImMap(self):
        return MapElement.Maptile