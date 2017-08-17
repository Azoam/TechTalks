import GameStates
import GameObjects

class Test(GameStates.State):
    
    def __init__(self, game_display):
        GameStates.State.__init__(self, game_display)
        self.player = GameObjects.Player()

    def draw(self, g):
        self.player.draw(g, self.game_display)

    def update(self):
        pass
