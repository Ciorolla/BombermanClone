import pygame


class KeyAction:
    def __init__(self):
        self.lastAction = None


    def handle(self, key):
        if key[pygame.K_a]:
            self.lastAction = "LEFT"
        if key[pygame.K_d]:
            self.lastAction = "RIGHT"
        if key[pygame.K_w]:
            self.lastAction = "UP"
        if key[pygame.K_s]:
            self.lastAction = "DOWN"
        if key[pygame.K_e]:
            self.lastAction = "BOMB"

    def actionHandled(self):
        self.lastAction = "NONE"
