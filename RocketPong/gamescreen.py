# module import
import pygame

# personal imports
import colors
from entities import Player

class GameScreen:

    def __init__(self):
        font = pygame.font.SysFont("ubuntu", 15)
        self.label = font.render("Test Text", 1, colors.WHITE)
        self.player = Player(10,10,50,50)


    def input(self):
        pass


    def update(self):
        self.player.update()


    def draw(self, game_display):
       # game_display.blit(self.label, (100,100))
       self.player.draw(game_display)

