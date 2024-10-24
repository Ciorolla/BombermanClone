from server.model.powerup.PowerUp import PowerUp


class PowerUpSpeed(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.spriteName = 'powerupspeed'

    def picked_up(self, bomber):
        bomber.ticksNeededToMove -= 1

    def whoImServer(self):
        return "powerupspeed"