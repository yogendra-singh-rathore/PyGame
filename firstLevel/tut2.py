"""
Create game Title Name on Window

Create Game Variable
"""
import pygame

x = pygame.init()
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game Specific Variable
exit_game = False
game_over = False