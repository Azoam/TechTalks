import GameStates

class Test(GameStates.State):
    
    def __init__(self, game_display):
        GameStates.State.__init__(self, game_display)

    def draw(self, g):
        g.line(self.game_display, (255,255,255), (0,0), (100,100),2)

    def update(self):
        pass
