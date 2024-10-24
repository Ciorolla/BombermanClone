from server.model.powerup.PowerUp import PowerUp


class PowerUpBombPower(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.spriteName = 'powerupbombpower'

    def picked_up(self, bomber):
        bomber.bombPower +=1

    def whoImServer(self):
        return "powerupbombpower"