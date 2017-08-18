import abc

class State:
    '''
    Purpose: Abstract class that defines a level/menu for a game
    Author: Douglas Rudolph
    '''   

    #makes class abstract
    __metaclass__ = abc.ABCMeta

    def __init__(self, game_display):
        self.game_display = game_display
    
    @abc.abstractmethod
    def draw(self, g):
        return
    
    @abc.abstractmethod
    def update(self, e):
        return

class StateManager:

    def __init__(self, start_state):
        self._current_state = None
        self.set_state(start_state)

    def draw_current_state(self, g):
        self._current_state.draw(g)

    def update_current_state(self, e):
        self._current_state.update(e)

    def set_state(self, new_state):
        self._current_state = new_state

