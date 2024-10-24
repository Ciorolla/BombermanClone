from server.model.map.MapTile import MapTile
from util.SpriteLoader import SpriteLoader
from server.model.map.MapElement import MapElement

class WallDestructable(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = SpriteLoader.loadSprite('wall_destructable')


    def isEmpty(self):
        return False

    def whoImMap(self):
        return MapElement.WallDestructable