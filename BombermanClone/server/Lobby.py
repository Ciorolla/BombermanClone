from GameHandlerThread import GameHandlerThread


class Lobby:
    def __init__(self, lobbyID, hostClient):
        self.lobbyID = lobbyID
        self.host = hostClient
        self.players = []
        self.lobbyState = "WAITING"
        self.gameHandlerThread = GameHandlerThread(self)


    def startGame(self):
        self.lobbyState = "IN_GAME"
        self.gameHandlerThread.setup()
        self.gameHandlerThread.start()


    def addPlayer(self, player):
        self.players.append(player)
        self.broadcastLobbyState()

        player.messageHandlingFunction = self.handleClientMessage

    def removePlayer(self, player):
        self.players.remove(player)
        self.broadcastLobbyState()


    def broadcastLobbyState(self):
        self.broadcastData({"id": "LOBBY_STATE", "data": self.serialize()})

    def broadcastData(self, data):
        for player in self.players:
            player.sendData(data)

    def handleClientMessage(self, client_thread, message):
        playerID = self.players.index(client_thread)
        print(f"[LOBBY({self.lobbyState}) {self.lobbyID}] {message} {playerID}")

        if client_thread == self.host:
            self.handleHostCommand(message)

        if self.lobbyState == "WAITING":
            if message['id'] == "SKIN_SELECTION":
                self.gameHandlerThread.selectedSkins[playerID][0] = message['data']['bomber']
                self.gameHandlerThread.selectedSkins[playerID][1] = message['data']['bomb']


        elif self.lobbyState == "IN_GAME":

            actingPlayer = self.players.index(client_thread)
            print(f"[LOBBY(IN-GAME) {self.lobbyID}] {message} {actingPlayer}")
            self.gameHandlerThread.handleClientGameMessage(message, playerID)


    def handleHostCommand(self, message):
        if message['id'] == "SELECT_MAP":
            self.gameHandlerThread.selectedMap = message['map_name']
        if message['id'] == "START_GAME":
            self.startGame()

        self.broadcastLobbyState()


    def serialize(self):
        return {
            "lobby_ID": self.lobbyID,
            "lobby_state": self.lobbyState,
            "players": len(self.players),
            "selected_map": self.gameHandlerThread.selectedMap
        }