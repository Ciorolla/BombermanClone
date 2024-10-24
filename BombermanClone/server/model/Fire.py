import pygame

from util.SpriteLoader import SpriteLoader

class Fire:
    def __init__(self,position):
        self.x = position[0]
        self.y = position[1]
        self.burn = 50
        self.spriteName = 'fire'

    def serialize(self):
        out = {
            "x": self.x,
            "y": self.y,
            "sprite_name": self.spriteName
        }
        return out
