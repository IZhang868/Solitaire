import random
import math
import pygame
import sys
from pygame.locals import *
def card_random():
    #         0    1    2    3
    suits = ['H', 'S', 'D', 'C']
    #               0   1   2   3   4   5   6   7   8   9 indexing
    card_number = ['1','2','3','4','5','6','7','8','9','10']
    randomized_card_list = []
    suits_random = random.randint(0,3)
    card_random = random.randint(0,9)
    print(card_random)
    print(suits_random)
    for i in range(0,52):
        final_card = card_number[card_random] + suits[suits_random]
        randomized_card_list.append(final_card)
        
    return(randomized_card_list)
    
#def main():
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
#main()
card_random()