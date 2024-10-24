import os
from server.model.map.Map import Map
from server.model.map.MapTile import MapTile
from server.model.map.Wall import Wall
from server.model.map.WallDestructable import WallDestructable


class MapLoader():
    @staticmethod
    def fromFile(mapName):
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, 'resources', mapName + '.txt')
        with open(file_path, 'r') as f:
            lines = f.readlines()

        size = int(lines[0])
        map = [[None for _ in range(size)] for _ in range(size)]
        spawnPoints = []

        map_tiles = [line.split() for line in lines[1:]]
        for i in range(size):
            for j in range(size):
                tile = map_tiles[i][j]
                if tile == 'S':
                    map[i][j] = MapTile(i, j)
                    spawnPoints.append((i,j))
                elif tile == 'T':
                    map[i][j] = MapTile(i, j)
                elif tile == 'W':
                    map[i][j] = Wall(i,j)
                elif tile == 'D':
                    map[i][j] = WallDestructable(i, j)
                else:
                    raise ValueError(f"Invalid tile type: {tile} at position ({i}, {j})")

        mapData = {
            "size": size,
            "map": map,
            "spawnPoints": spawnPoints
        }
        return Map(mapData)