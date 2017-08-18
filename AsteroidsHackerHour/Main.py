import pygame

from Constants import GameData, Colors
import GameStates, GameScreens


#very first thing you need to do
pygame.init()

#setting up window settings
game_display = pygame.display.set_mode(GameData.SCREEN_SIZE)
pygame.display.set_caption(GameData.TITLE)

#creating game state manager
test_state = GameScreens.GameScreen(game_display)
game_state_manager = GameStates.StateManager(test_state)

#Used a game clock to impose a certain FPS
clock = pygame.time.Clock()

#create gameloop
while not GameData.CRASHED:
    
    #get input
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            GameData.CRASHED = True

    #draw over previous frame & update
    game_display.fill(Colors.BLACK)

    #game state update & render
    game_state_manager.update_current_state(pygame.event)
    game_state_manager.draw_current_state(pygame.draw)
    
    #update the frame and update the game clock
    pygame.display.update()
    clock.tick(60)

#if exited loop, close window and quit game
pygame.quit()
quit()
