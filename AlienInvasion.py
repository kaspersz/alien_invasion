import sys

import pygame

class AlienInvasion:
    ''' Main class to manage the resources of the game'''

    def __init__(self):
        ''' Initialization of the game and creating the resources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (230,230,230)
        pygame.display.set_caption("Alien invasion")
    
    def run_game(self):
        ''' Beginning the game'''

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
