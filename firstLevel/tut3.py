"""
Create game Title Name on Window

Create Game Variable

Fix Game Window (Hold Window)
        Game Loop
Infinity loop window may me it will not respond but it hold window
"""
import pygame

x = pygame.init()
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game Specific Variable
exit_game = False
game_over = False

# Create a Game Loop
while not exit_game:
    pass

pygame.quit()
quit()