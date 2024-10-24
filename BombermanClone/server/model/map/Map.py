class Map:
    def __init__(self, mapData):
        self.size = mapData['size']
        self.map = mapData['map']
        self.spawnPoints = mapData['spawnPoints']



    def getObjectAt(self, x, y):
        return self.map[x][y]

    def serialize(self):
        out = [[self.getObjectAt(x,y).whoImMap().value for x in range(self.size)] for y in range(self.size)]
        return out