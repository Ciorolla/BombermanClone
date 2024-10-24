import pygame
from MainLoop import MainLoop

def main(windowSize=800):
    print('start')
    pygame.init()
    screen = pygame.display.set_mode((windowSize, windowSize))
    mainloop = MainLoop(screen)
    mainloop.run()


if __name__ == '__main__':
    main()