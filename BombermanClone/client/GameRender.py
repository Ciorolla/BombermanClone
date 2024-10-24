import pygame

from util.SpriteLoader import SpriteLoader


class GameRender:
    def __init__(self, screen):
        self.screen = screen
        self.scale_factor = None
        self.tileSpriteNames = {1: "tile", 2: "wall", 3: "wall_destructable"}

        self.dataToRender = None

    def setDataToRender(self, gameData):
        self.dataToRender = gameData

    def drawGame(self):
        if self.dataToRender is None:
            return

        if self.scale_factor is None:
            self.calculateScaleFactor(len(self.dataToRender['map']))

        self.cleanWindow()

        self.drawMap(self.dataToRender['map'])
        self.drawBombers(self.dataToRender['bombers'])
        self.drawPowerUps(self.dataToRender['powerups'])
        self.drawBombs(self.dataToRender['bombs'])
        self.drawFires(self.dataToRender['fires'])

        pygame.display.update()
        self.dataToRender = None


    def cleanWindow(self):
        self.screen.fill((68, 85, 90))


    def drawMap(self, mapData):
        mapSize = len(mapData)
        for i in range(mapSize):
            for j in range(mapSize):
                tile = mapData[j][i]
                image, rect = self.createImageAndRect(i, j, self.tileSpriteNames[tile])
                scaled_image, scaled_rect = self.scaleImageAndRect(image, rect)
                self.screen.blit(scaled_image, scaled_rect)

    def drawBombers(self, bombersData):
        for bomberData in bombersData:
            image, rect = self.createImageAndRect(bomberData["x"], bomberData["y"], bomberData["sprite_name"])
            scaled_image, scaled_rect = self.scaleImageAndRect(image, rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawBombs(self, bombsData):
        for bombData in bombsData:
            image, rect = self.createImageAndRect(bombData["x"], bombData["y"], bombData["sprite_name"])
            scaled_image, scaled_rect = self.scaleImageAndRect(image, rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawFires(self, firesData):
        for fireData in firesData:
            image, rect = self.createImageAndRect(fireData["x"], fireData["y"], fireData["sprite_name"])
            scaled_image, scaled_rect = self.scaleImageAndRect(image, rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawPowerUps(self, powerupsData):
        for powerupData in powerupsData:
            image, rect = self.createImageAndRect(powerupData["x"], powerupData["y"], powerupData["sprite_name"])
            scaled_image, scaled_rect = self.scaleImageAndRect(image, rect)
            self.screen.blit(scaled_image, scaled_rect)


    def createImageAndRect(self, x,y, spriteName):
        image = SpriteLoader.loadSprite(spriteName).image
        rect = pygame.Rect(x * 64, y * 64, 64, 64)
        return image, rect


    def scaleImageAndRect(self, image, rect):
        scaled_image = pygame.transform.scale_by(image, self.scale_factor)
        scaled_rect = scaled_image.get_rect(topleft=(rect.x * self.scale_factor, rect.y * self.scale_factor))
        return scaled_image, scaled_rect

    def calculateScaleFactor(self, mapSize):
        self.scale_factor = self.screen.get_width() / (64 * mapSize)
        print(self.scale_factor)
