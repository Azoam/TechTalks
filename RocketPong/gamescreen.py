import pygame
import colors

class GameScreen:

    def __init__(self):
        font = pygame.font.SysFont("ubuntu", 15)
        self.label = font.render("Test Text", 1, colors.WHITE)
    
    def input(self):
        pass

    def update(self):
        pass

    def draw(self, game_display):
       game_display.blit(self.label, (100,100)) 
