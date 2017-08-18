import abc
import pygame

import Colors


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

        g.lines(game_display, (255,255,255), True, self.point_list, 2)

    def update(self, e):
        for event in e.get():
            if event.type == pygame.KEY_DOWN:
                if event.key == pygame.LEFT:
                    pass
                if event.key == pygame.RIGHT:
                    pass
                if event.key == pygame.UP:
                    pass
                if event.key == pygame.DOWN:
                    pass


class Asteroid(Entity):
    
    def __init__(self):
        Entity.__init__(self, 100, 100, 1, 1) 
        self.radius = 10

        self.x_vel = 2
        self.y_vel = 2
    
    #TODO: Implement random shape later, temp using as circle
    def _create_shape():
        pass

    def draw(self, g, game_display):
        self.pos = (self.x, self.y)
        g.circle(game_display, Colors.WHITE, self.pos, 10, 1)

    def update(self, e):
       self.x += self.x_vel
       self.y += self.y_vel
        
