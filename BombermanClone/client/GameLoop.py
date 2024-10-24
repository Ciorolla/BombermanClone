import pygame

from server.model.KeyAction import KeyAction
from client.GameRender import GameRender


class GameLoop:
    def __init__(self, screen,connection,mainLoop):
        self.mainLoop = mainLoop
        self.keyHandler = KeyAction()
        self.render = GameRender(screen)
        self.connection = connection



    def tick(self):
        self.keyHandler.handle(pygame.key.get_pressed())
        self.render.drawGame()

    def handleServerMessage(self, message):
        if message['id'] == "GAME_STATE":
            state = message["data"]
            self.render.setDataToRender(state)
            response = {
                "id": "ACTION",
                "action": self.keyHandler.lastAction
            }
            self.connection.send_message(response)
            self.keyHandler.actionHandled()
        elif message['id'] == "END_STATE":
            self.mainLoop.endloop.setLeaderBoard(message['data'])
            self.mainLoop.state = 2
