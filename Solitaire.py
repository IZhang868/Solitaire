import random
import math
import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit
                sys.exit
                break
        pygame.display.update()
    GREEN = (0, 255, 0)
    
main()