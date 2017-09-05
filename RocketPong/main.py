#module imports
import pygame

#personal imports
import colors
import gamescreen 

#basic game settings
pygame.init()
game_display = pygame.display.set_mode((640,480))
pygame.display.set_caption("Rocket Pong")
game_clock = pygame.time.Clock()

#user defined game stuff
game_screen = gamescreen.GameScreen()
CRASHED = False

while not CRASHED:

    #fill screen 
    game_display.fill(colors.BLACK)
    
    #update screen
    game_screen.input()
    game_screen.update()
    game_screen.draw(game_display)

    pygame.display.update()
    game_clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True

#if game crashed, exit pygame and python
pygame.quit()
quit()
