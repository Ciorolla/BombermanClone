from random import randint


class RandomEmptyPosition:
    @staticmethod
    def generate(game):
        mapSize = game.map.size
        while True:
            x = randint(0, mapSize- 1)
            y = randint(0, mapSize-1)
            if not game.map.getObjectAt(x,y).isEmpty():
                continue

            for bomber in game.bombers:
                if bomber.x == x and bomber.y == y:
                    continue

            for powerup in game.powerups:
                if powerup.x == x and powerup.y == y:
                    continue

            return (x,y)