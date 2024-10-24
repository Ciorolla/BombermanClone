import os
import pygame


class SpriteLoader(object):
    loadedSprites = {}
    @classmethod
    def loadSprite(cls, spriteName):
        if spriteName in cls.loadedSprites:
            return cls.loadedSprites[spriteName]

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        sprite_path = os.path.join(parent_dir, 'resources', 'sprites', spriteName + '.png')

        img = pygame.image.load(sprite_path)
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        cls.loadedSprites[spriteName] = sprite
        return sprite

