import sys
import pygame

from configfile import clock, FPS
from game import GameGroup


while True:
    for event in pygame.event.get():
        GameGroup.update(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(FPS)
