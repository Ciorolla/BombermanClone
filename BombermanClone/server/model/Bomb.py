class Bomb:
    def __init__(self,position,bomber):
        self.x = position[0]
        self.y = position[1]
        self.power = bomber.bombPower
        self.fuse = 150
        self.spriteName = bomber.bombSpriteName
        self.bomber = bomber

    def serialize(self):
        out = {
            "x": self.x,
            "y": self.y,
            "sprite_name": self.spriteName
        }
        return out

