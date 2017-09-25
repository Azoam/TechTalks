#system level imports
from random import randint
import abc
import pygame
import sys

#user level imports
from Constants import Colors, GameData


class Entity:
    
    __metaclass__ = abc.ABCMeta

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    @abc.abstractmethod
    def draw(self, g):
        return

    @abc.abstractmethod
    def upate(self, e):
        return


class Player(Entity):

    def __init__(self):
        self.x_vel = 0
        self.y_vel = 0

        self.x_cords = [100, 80, 90, 110, 120]
        self.y_cords = [100, 150, 140, 140, 150]
        self.point_list = [] 

        Entity.__init__(self, 10, 10, 10, 10)
    
    def draw(self, g, game_display):
        for x, y  in zip(self.x_cords, self.y_cords):
            self.point_list.append((x,y))

        g.lines(game_display, Colors.WHITE, True, self.point_list, 2)

    def update(self, e):
        for event in e.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.LEFT:
                    print("test")
                if event.key == pygame.RIGHT:
                    pass
                if event.key == pygame.UP:
                    pass
                if event.key == pygame.DOWN:
                    pass

class Asteroid(Entity): 

    def __init__(self):
        Entity.__init__(self, 100, 100, 1, 1) 
        
        #sets the radius of the asteroid to be 10
        self.radius = 10
        
        #spawns with random direction
        self.x_vel = randint(-4,4)
        self.y_vel = randint(-4,4)
        self.point_list = self._create_shape()
    
    def _create_shape(self):

        RND_ORIGIN = (randint(10,630), randint(10,470))
        asteroid_convex = []
        
        #3 upperleft quadrant
        for i in range(0,2):
            coord = (RND_ORIGIN[0]+randint(-50,-1), RND_ORIGIN[1] + randint(-50,-1))
            asteroid_convex.append(coord)

        #3 upperright quadrant
        for i in range(0,2):
            coord = (RND_ORIGIN[0]+randint(1,50), RND_ORIGIN[1] + randint(-50,-1))
            asteroid_convex.append(coord)

        #3 botteleft quadrant
        for i in range(0,2):
            coord = (RND_ORIGIN[0]+randint(1,50), RND_ORIGIN[1] + randint(1,50))
            asteroid_convex.append(coord)

        #3 bottomright quadrant
        for i in range(0,2):
            coord = (RND_ORIGIN[0]+randint(-50,-1), RND_ORIGIN[1] + randint(1,50))
            asteroid_convex.append(coord)

        return asteroid_convex

    def draw(self, g, game_display):
        self.pos = (self.x, self.y)
        g.lines(game_display, Colors.WHITE, True, self.point_list, 2)

    def update(self, e):
        #updates the position of the asteroid
        updated_pos = [] 
        for coord in self.point_list:
            updated_pos.append((coord[0] + self.x_vel, coord[1] + self.y_vel))

        self.point_list = updated_pos
        
        #wraps the asteroid around the screen
        for coord in self.point_list:
            if coord[0] > GameData.SCREEN_SIZE[0]:
                pass
                #update list to the left
            elif coord[0] < 0:
                pass
                #update list to the right
            elif coord[1] > GameData.SCREEN_SIZE[1]:
                pass
                #update list to the top 
            elif coord[1] < 0:
                pass
                #update list to the bottom

