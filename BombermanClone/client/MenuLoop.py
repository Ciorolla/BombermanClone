import pygame
import pygame_gui

from util.SkinManager import SkinManager
from util.SpriteLoader import SpriteLoader


class MenuLoop:
    def __init__(self, screen, connection):
        self.screen = screen
        self.connection = connection
        self.screen_rect = screen.get_rect()
        self.manager = pygame_gui.UIManager((800, 800))
        self.messageHandler = None

        self.playerType = "NONE"

        ###
        ### MAIN MENU
        ###
        self.mainMenuPanel = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                         manager=self.manager)

        self.titleLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (100, 100)),
                                                      text='BOMBERMAN',
                                                      manager=self.manager,
                                                      container=self.mainMenuPanel)

        self.hostGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 200), (200, 100)),
                                                           text='Host game',
                                                           manager=self.manager,
                                                           container=self.mainMenuPanel)

        self.joinGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 300), (200, 100)),
                                                           text='Join game',
                                                           manager=self.manager,
                                                           container=self.mainMenuPanel)


        ###
        ### INSIDE LOBBY
        ###
        self.lobbyPanel = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                      manager=self.manager)

        self.lobbyInfoLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (500, 100)),
                                                     text='',
                                                     manager=self.manager,
                                                     container=self.lobbyPanel)

        ## SKIN SELECTION PANEL
        self.availableBomberSkins = SkinManager.getAvailableBomberSkins()
        self.selectedBomberSkin = 0
        self.availableBombSkins = SkinManager.getAvailableBombSkins()
        self.selectedBombSkin = 0

        self.skinSelectionPanel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((100, 200), (600, 300)),
                                                             manager=self.manager,
                                                             container=self.lobbyPanel)

        self.selectedBomberSkinImage = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((86, 86), (128, 128)),
                                                                   image_surface=SpriteLoader.loadSprite("bomber").image,
                                                                   manager=self.manager,
                                                                   container=self.skinSelectionPanel)

        self.previousBomberSkinButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((44, 134), (32, 32)),
                                                                     text='<',
                                                                     manager=self.manager,
                                                                     container=self.skinSelectionPanel)

        self.nextBomberSkinButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((224, 134), (32, 32)),
                                                                     text='>',
                                                                     manager=self.manager,
                                                                     container=self.skinSelectionPanel)

        self.selectedBombSkinImage = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((386, 86), (128, 128)),
                                                                   image_surface=SpriteLoader.loadSprite("bomb").image,
                                                                   manager=self.manager,
                                                                   container=self.skinSelectionPanel)

        self.previousBombSkinButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((344, 134), (32, 32)),
                                                                     text='<',
                                                                     manager=self.manager,
                                                                     container=self.skinSelectionPanel)

        self.nextBombSkinButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((514, 134), (32, 32)),
                                                                     text='>',
                                                                     manager=self.manager,
                                                                     container=self.skinSelectionPanel)


        ## HOST ONLY PANEL
        self.hostSettingsPanel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((100, 500), (600, 200)),
                                                             manager=self.manager,
                                                             container=self.lobbyPanel)

        self.map1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 25), (100, 50)),
                                                 text='Map 1',
                                                 manager=self.manager,
                                                 container=self.hostSettingsPanel)

        self.map2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 25), (100, 50)),
                                                 text='Map 2',
                                                 manager=self.manager,
                                                 container=self.hostSettingsPanel)

        self.map3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 25), (100, 50)),
                                                 text='Map 3',
                                                 manager=self.manager,
                                                 container=self.hostSettingsPanel)

        self.startGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 100), (200, 75)),
                                                            text='Start game',
                                                            manager=self.manager,
                                                            container=self.hostSettingsPanel)

        self.hostSettingsPanel.hide()
        self.lobbyPanel.hide()


        ###
        ### LOBBY SELECTION
        ###

        self.lobbySelection = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                     manager=self.manager)

        self.lobbySelectionLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 25), (800, 75)),
                                                               text="Available lobbies:",
                                                               manager=self.manager,
                                                               container=self.lobbySelection)

        self.availableLobbies = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((100, 100), (600, 550)),
                                                             manager=self.manager,
                                                             container=self.lobbySelection)

        self.lobbySelection.hide()
        self.lobbyListButton = []
        self.lobbyListRoomId = []


    def tick(self):
        self.screen.fill((68, 85, 90))
        self.manager.draw_ui(self.screen)

    def updateLobbyData(self, lobbyData):
        self.lobbyInfoLabel.set_text(f'numer pokoju: {lobbyData["lobby_ID"]} mapa: {lobbyData["selected_map"]}  ilosc graczy {lobbyData["players"]}')
        self.lobbyPanel.show()

        if self.playerType == "HOST":
            self.hostSettingsPanel.show()

        if self.playerType =="GUEST":
            self.hostSettingsPanel.hide()


    def showLobbies(self, lobbies):
        self.lobbyListButton.clear()
        self.lobbyListRoomId.clear()
        counter = 0
        for lobby in lobbies:
            if lobby["lobby_state"] == "WAITING":
                infoLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, counter * 50), (500, 50)),
                                                        text=f'ID: {lobby["lobby_ID"]} state: {lobby["lobby_state"]}, players: {lobby["players"]}, selected map: {lobby["selected_map"]}',
                                                        manager=self.manager,
                                                        container=self.availableLobbies)
                joinButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, counter * 50), (100, 50)),
                                                      text=f'JOIN',
                                                      manager=self.manager,
                                                      container=self.availableLobbies)

                self.lobbyListRoomId.append(lobby["lobby_ID"])
                self.lobbyListButton.append(joinButton)
                counter +=1
        print(lobbies)
        self.lobbySelection.show()

    def handleMenuEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if self.messageHandler is None:
                print("Button clicked, but there is no hanlder to handle it!")
                return

            if event.ui_element == self.joinGameButton:
                data = {"id": "LIST_LOBBY"}
                self.messageHandler(data)
                self.mainMenuPanel.hide()

            if event.ui_element == self.hostGameButton:
                data = {"id": "HOST_LOBBY"}
                self.playerType = "HOST"
                self.messageHandler(data)
                self.mainMenuPanel.hide()

            if event.ui_element == self.map1:
                data = {"id": "SELECT_MAP", "map_name": "map1"}
                self.messageHandler(data)

            if event.ui_element == self.map2:
                data = {"id": "SELECT_MAP", "map_name": "map2"}
                self.messageHandler(data)

            if event.ui_element == self.map3:
                data = {"id": "SELECT_MAP", "map_name": "map3"}
                self.messageHandler(data)

            if event.ui_element == self.startGameButton:
                data = {"id": "START_GAME"}
                self.messageHandler(data)

            if event.ui_element in self.lobbyListButton:
                self.playerType = "GUEST"
                data = {"id": "JOIN_LOBBY", "lobby_id": self.lobbyListRoomId[self.lobbyListButton.index(event.ui_element)]}
                self.messageHandler(data)
                self.lobbySelection.hide()

            if event.ui_element == self.nextBomberSkinButton:
                self.selectedBomberSkin += 1
                self.updateSelectedSkins()

            if event.ui_element == self.previousBomberSkinButton:
                self.selectedBomberSkin -= 1
                self.updateSelectedSkins()

            if event.ui_element == self.nextBombSkinButton:
                self.selectedBombSkin += 1
                self.updateSelectedSkins()

            if event.ui_element == self.previousBombSkinButton:
                self.selectedBombSkin -= 1
                self.updateSelectedSkins()


    def updateSelectedSkins(self):
        self.selectedBomberSkin %= len(self.availableBomberSkins)
        self.selectedBombSkin %= len(self.availableBombSkins)
        newSelectedBomberSkin = self.availableBomberSkins[self.selectedBomberSkin]
        newSelectedBombSkin = self.availableBombSkins[self.selectedBombSkin]

        data = {"id": "SKIN_SELECTION", "data": {"bomber": newSelectedBomberSkin, "bomb": newSelectedBombSkin}}
        self.messageHandler(data)

        self.selectedBomberSkinImage.set_image(SpriteLoader.loadSprite(newSelectedBomberSkin).image)
        self.selectedBombSkinImage.set_image(SpriteLoader.loadSprite(newSelectedBombSkin).image)

    def listenForMessages(self, messageHandler):
        self.messageHandler = messageHandler
