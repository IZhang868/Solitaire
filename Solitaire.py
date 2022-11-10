import random
import math
import pygame
import sys
from pygame.locals import *
import PNG
def card_random():
def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    running = True
    Board_Color = (6, 124, 53)
    BLACK = (0, 0, 0)
    screen.fill(Board_Color)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.display.quit()
            elif event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
                x = pygame.mouse.get_pos
            pygame.draw.line(screen, BLACK, (300,0), (300,400))
            img = pygame.image.load('resized 9s.png')
            screen.blit(img, (0,0))
        pygame.display.flip()    
main()