from collections import defaultdict

from server.model.game.Game import Game
from util.MapLoader import MapLoader


class GameCreator:
    selectedSkins = defaultdict(lambda: ["bomber", "bomb"])
    @staticmethod
    def createGameUsingMapFile(mapName, bomberCount):
        gameMap = MapLoader.fromFile(mapName)
        game = Game(gameMap)
        game.addBombers(bomberCount)
        return game