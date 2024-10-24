from server.model.powerup.PowerUp import PowerUp


class PowerUpBombCount(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.spriteName = 'powerupbombcount'

    def picked_up(self, bomber):
        bomber.bombLimit +=1

    def whoImServer(self):
        return "powerupbombcount"