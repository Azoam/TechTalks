#system level imports
import pygame

#user created imports
from Constants import Colors
import GameStates
import GameObjects

class GameScreen(GameStates.State):
    
    def __init__(self, game_display):
        GameStates.State.__init__(self, game_display)
        self.player = GameObjects.Player()
        self.asteroid = GameObjects.Asteroid()

    def draw(self, g):
        self.player.draw(g, self.game_display)
        self.asteroid.draw(g, self.game_display)

    def update(self, e):
        self.player.update(e)
        self.asteroid.update(e)
