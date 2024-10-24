from enum import Enum

class Directions(Enum):

    UP = (0,-1)
    LEFT = (-1,0)
    RIGHT = (1,0)
    DOWN = (0,1)