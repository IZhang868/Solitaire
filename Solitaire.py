import random
import math
import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    running = True
    GREEN = (0, 255, 0)
    screen.fill(GREEN)
    pygame.display.flip()
    while running == True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running == False
            pygame.draw.line(200, 0)
main()