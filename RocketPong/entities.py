#pygame imports
import pygame
from abc import ABCMeta, abstractmethod

#module imports
import colors

#base class for all objects in the game
class Entity(pygame.Rect):
    
    __metaclass__ = ABCMeta

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height

    def has_collided(self, rect):
        if pygame.Rect.contains(rect):
            return True

        return False
    
    @abstractmethod
    def update(self):
        return 
    
    @abstractmethod
    def draw(self, game_display):
        return 

#player class that we will control
class Player(Entity):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y = self.y - 1
                if event.key == pygame.K_DOWN:
                    self.y = self.y + 1

    def draw(self, game_display):
        coords = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(game_display, colors.RED, coords)
