import pygame

from util.SpriteLoader import SpriteLoader


class PowerUp:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

        self.spriteName = 'unknown'

    def picked_up(self, bomber):
        raise NotImplementedError(f"{self.__class__.__name__} does not implement picked_up()!")

    def whoImServer(self):
        raise NotImplementedError(f"{self.__class__.__name__} does not implement whoImServer()!")

    def serialize(self):
        out = {
            "x": self.x,
            "y": self.y,
            "sprite_name": self.spriteName
        }
        return out