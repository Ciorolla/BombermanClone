import pygame
import pygame_gui


class EndLoop:
    def __init__(self, screen, connection):
        self.screen = screen
        self.connection = connection
        self.screen_rect = screen.get_rect()
        self.manager = pygame_gui.UIManager((800, 800))
        self.leaderboard = []

        self.endPanel = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                    manager=self.manager)
        self.titleLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (100, 100)),
                                                      text='Leaderboard',
                                                      manager=self.manager,
                                                      container=self.endPanel)
        self.players = []

    def tick(self):
        self.screen.fill((68, 85, 90))
        self.manager.draw_ui(self.screen)

    def setLeaderBoard(self, leaderboard):
        leaderboard.reverse()
        counter = 0
        for player in leaderboard:
            self.players.append(
                pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 200 + counter * 100), (500, 100)),
                                            text=f'bomber{player[0] + 1} Wynik: {player[1]}',
                                            manager=self.manager,
                                            container=self.endPanel))
            counter += 1
