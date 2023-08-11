import pygame


pygame.init()
game_size = width, height = 545, 725
screen = pygame.display.set_mode(game_size)
pygame.display.set_caption('2048 by Nemo_Semi')
clock = pygame.time.Clock()
FPS = 144
size_of_map = 4