import pygame
import GameStates, TestState

#constants
FPS = 60
SCREEN_SIZE = (800,600)
TITLE = "Asteroids"
CRASHED = False


#very first thing you need to do
pygame.init()

#setting up window settings
game_display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)

#creating game state manager
test_state = TestState.Test(game_display)
game_state_manager = GameStates.StateManager(test_state)

#Used a game clock to impose a certain FPS
clock = pygame.time.Clock()

#create gameloop
while not CRASHED:
    
    #get input
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            CRASHED = True

    #draw over previous frame & update
    game_display.fill((0,0,0))

    #game state update & render
    game_state_manager.update_current_state(pygame.event)
    game_state_manager.draw_current_state(pygame.draw)
    
    #update the frame and update the game clock
    pygame.display.update()
    clock.tick(60)

#if exited loop, close window and quit game
pygame.quit()
quit()
