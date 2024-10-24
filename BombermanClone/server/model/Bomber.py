import pygame

from util.SpriteLoader import SpriteLoader


class Bomber:

    def __init__(self, position, lives=3):
        self.lives = lives
        self.x = position[0]
        self.y = position[1]
        self.spriteName = 'bomber'
        self.bombSpriteName = 'bomb'

        self.lastMoveTick = 0
        self.ticksNeededToMove = 20

        self.bombLimit = 1
        self.bombCounter = 0
        self.bombPower = 2


    def move(self, direction, board, firesCord):
        # TODO tu trzeba będize jakiś validator dowalić ale kolizji póki co nie ogarniam i no bez mapy też cięzko
        dir_x = direction.value[0]
        dir_y = direction.value[1]
        if self.lives > 0 and board.getObjectAt(dir_x + self.x, dir_y + self.y).isEmpty():
            self.x += dir_x
            self.y += dir_y
            if firesCord[self.x][self.y] > 0:
                self.bomberDmg()
            return True
        return False

    def moveAvailable(self, currentTicks):
        return currentTicks - self.lastMoveTick >= self.ticksNeededToMove

    def bomberDmg(self):
        self.lives -= 1
        if self.lives == 0:
            print("koniec gry")

    def applySkin(self, skin):
        self.spriteName = skin[0]
        self.bombSpriteName = skin[1]

    def whoImString(self):
        return "Bomberman"

    def serialize(self):
        out = {
            "lives": self.lives,
            "x": self.x,
            "y": self.y,
            "sprite_name": self.spriteName
        }
        return out