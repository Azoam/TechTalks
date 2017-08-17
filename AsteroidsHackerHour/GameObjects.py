import abc
import sys

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
    def upate(self):
        return

class Player(Entity):

    def __init__(self):
        self.x_cords = [100, 80, 90, 110, 120]
        self.y_cords = [100, 150, 140, 140, 150]
        self.point_list = [] 
        Entity.__init__(self, 10, 10, 10, 10)
    
    def draw(self, g, game_display):
        for x, y  in zip(self.x_cords, self.y_cords):
            self.point_list.append((x,y))

        g.lines(game_display, (255,255,255), True, self.point_list, 2)

def update(self):
        pass
