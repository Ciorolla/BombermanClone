from random import choice

from server.model.powerup.PowerUpSpeed import PowerUpSpeed
from server.model.powerup.PowerUpBombCount import PowerUpBombCount
from server.model.powerup.PowerUpBombPower import PowerUpBombPower
from server.model.powerup.PowerUpHealth import PowerUpHealth


class PowerUpCreator:
    available_powerups = [PowerUpBombCount, PowerUpBombPower, PowerUpSpeed]


    @staticmethod
    def create_random_powerup(position):
        return choice(PowerUpCreator.available_powerups)(position)
