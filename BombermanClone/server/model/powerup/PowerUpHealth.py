from server.model.powerup.PowerUp import PowerUp


class PowerUpHealth(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.spriteName = 'poweruphealth'

    def picked_up(self, bomber):
        bomber.lives +=1

    def whoImServer(self):
        return "poweruphealth"