from Lobby import Lobby


class LobbyManager:
    def __init__(self):
        self.lobbies = {}
        self.nextLobbyID = 1

    def hostLobby(self, hostClient):
        lobby = Lobby(self.nextLobbyID, hostClient)
        lobby.addPlayer(hostClient)

        self.lobbies[self.nextLobbyID] = lobby
        self.nextLobbyID += 1


    def joinLobby(self, lobby_id, player):
        if lobby_id in self.lobbies:
            lobby = self.lobbies[lobby_id]
            lobby.addPlayer(player)


    def getLobbies(self):
        return [lobby.serialize() for lobby in self.lobbies.values() if lobby.host.is_alive]