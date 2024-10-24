from server.model.Bomber import Bomber
from server.model.Bomb import Bomb
from server.model.powerup.PowerUpCreator import PowerUpCreator
from util.RandomEmptyPosition import RandomEmptyPosition
from server.model.map.MapElement import MapElement
from server.model.map.MapTile import MapTile
from server.model.Fire import Fire


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []
        self.aliveBombers = []
        self.bomberScore = []
        self.bombs = []
        self.powerups = []
        self.fires = []
        self.firesCord = [[0 for _ in range(map.size)] for _ in range(map.size)]
        self.bombCord = [[0 for _ in range(map.size)] for _ in range(map.size)]

        self.ticksToSpawnPowerUp = 600

        self.currentTick = 0
        self.lastPowerUpSpawnTick = 0
        
        self.isGame = True

    def tick(self):
        self.tickBombs()
        self.pickupPowerUps()
        self.tickFire()
        if self.shouldSpawnPowerUp():
            self.spawnPowerUp()
        self.currentTick += 1
        self.killBombers()
        self.gameEnd()


    def killBombers(self):
        for bomber in self.aliveBombers:
            if bomber.lives <= 0:
                self.bomberScore.append([self.bombers.index(bomber),self.currentTick])
                self.aliveBombers.remove(bomber)
    def gameEnd(self):
        if len(self.aliveBombers) <= 1:
            for bomber in self.aliveBombers:
                self.bomberScore.append([self.bombers.index(bomber), self.currentTick+1000])
                self.aliveBombers.remove(bomber)
            self.isGame = False
            print("to jest już koniec nie ma już nic")


    def tickBombs(self):
        for bomb in self.bombs:
            bomb.fuse -= 1
            if bomb.fuse == 0:
                self.bombBOOM(bomb)

    def tickFire(self):
        for fire in self.fires:
            fire.burn -= 1
            if fire.burn == 0:
                self.firesCord[fire.x][fire.y] -= 1
                self.fires.remove(fire)

    def pickupPowerUps(self):
        #TODO: rewrite this
        for bomber in self.bombers:
            for powerup in self.powerups:
                if bomber.x == powerup.x and bomber.y == powerup.y:
                    powerup.picked_up(bomber)
                    self.powerups.remove(powerup)


    def moveBomber(self, bomber, direction):
        if bomber not in self.bombers:
            raise ValueError("The provided bomber is not in the game!")

        if bomber.moveAvailable(self.currentTick) and bomber in self.aliveBombers:
            bomber.move(direction, self.map, self.firesCord)
            bomber.lastMoveTick = self.currentTick


    def addBombers(self, count):
        for i in range(count):
            bomber = Bomber(self.map.spawnPoints[i])
            self.bombers.append(bomber)
            self.aliveBombers.append(bomber)


    def applySkins(self, skinsDict):
        for i in range(len(self.bombers)):
            self.bombers[i].applySkin(skinsDict[i])


    def placeBomb(self, bomber):
        if bomber.bombCounter < bomber.bombLimit and self.bombCord[bomber.x][bomber.y] == 0:
            self.bombCord[bomber.x][bomber.y] = 1
            bomb = Bomb([bomber.x, bomber.y], bomber)
            self.bombs.append(bomb)
            bomber.bombCounter += 1
            #print("bomb has been planted")

    def shouldSpawnPowerUp(self):
        return self.currentTick - self.lastPowerUpSpawnTick >= self.ticksToSpawnPowerUp

    def spawnPowerUp(self):
        powerUpPosition = RandomEmptyPosition.generate(self)
        powerUp = PowerUpCreator.create_random_powerup(powerUpPosition)
        self.powerups.append(powerUp)
        self.lastPowerUpSpawnTick = self.currentTick

    def bombBOOM(self, bomb):
        bomb.bomber.bombCounter -= 1
        gora, dol, lewo, prawo = True, True, True, True
        self.bombCord[bomb.x][bomb.y] = 0

        for i in range(0, bomb.power + 1):
            if i == 0:
                self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y).whoImMap(), bomb.x, bomb.y)
                continue
            if gora:
                gora = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y + i).whoImMap(), bomb.x, bomb.y + i)
            if dol:
                dol = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y - i).whoImMap(), bomb.x, bomb.y - i)
            if lewo:
                lewo = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x - i, bomb.y).whoImMap(), bomb.x - i, bomb.y)
            if prawo:
                prawo = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x + i, bomb.y).whoImMap(), bomb.x + i, bomb.y)

        self.bombs.remove(bomb)

    def bombDestroyOrNot(self, mapElem, x, y):
        if mapElem == MapElement.WallDestructable:
            self.map.map[x][y] = MapTile(x, y)
            self.fires.append(Fire((x, y)))
            self.firesCord[x][y] += 1
            return False

        elif mapElem == MapElement.Maptile:
            self.fires.append(Fire((x, y)))
            self.firesCord[x][y] += 1
            for bomber in self.bombers:
                if bomber.x == x and bomber.y == y:
                    bomber.bomberDmg()
            return True

        return False

    def serialize(self):
        out = {
            "map": self.map.serialize(),
            "bombers": [bomber.serialize() for bomber in self.bombers],
            "powerups": [powerup.serialize() for powerup in self.powerups],
            "bombs": [bomb.serialize() for bomb in self.bombs],
            "fires": [fire.serialize() for fire in self.fires]
        }
        return out