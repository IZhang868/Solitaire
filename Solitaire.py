import random
import math
import pygame
import sys
from pygame.locals import *
def shuffled_cards():
    deck = ['4H', '5H', '10D', '4D', '5H', '3S', '5H', '8C', '3S', '5D', '3C', '6C', '7S',
            '5D', 'AS', '6D', '7H', 'QS', 'QC', 'QD', '3S', '3D', '2S', '8D', '7H', '4D',
            '10S', '9S', '9S', '2H', 'JC', '1H', '9D', '3D', '8H', '7H', '9H', '3H', 'JH',
            'JC', 'AD', '6D', 'QC', '7S', '6C', 'AD', '3D', 'KC', '8S', '1S', 'KD']
    key = {'2S': 'PNG/2S.png', '2H': 'PNG/2H.png', '2D': 'PNG/2D.png', '2C': 'PNG/2C.png',
           '3S': 'PNG/3S.png', '3H': 'PNG/3H.png', '3D': 'PNG/3D.png', '3C': 'PNG/3C.png',
           '4S': 'PNG/4S.png', '4H': 'PNG/4H.png', '4D': 'PNG/4D.png', '4C': 'PNG/4C.png',
           '5S': 'PNG/5S.png', '5H': 'PNG/5H.png', '5D': 'PNG/5D.png', '5C': 'PNG/5C.png',
           '6S': 'PNG/6S.png', '6H': 'PNG/6H.png', '6D': 'PNG/6D.png', '6C': 'PNG/6C.png',
           '7S': 'PNG/7S.png', '7H': 'PNG/7H.png', '7D': 'PNG/7D.png', '7C': 'PNG/7C.png',
           '8S': 'PNG/8S.png', '8H': 'PNG/8H.png', '8D': 'PNG/8D.png', '8C': 'PNG/8C.png',
           '9S': 'PNG/9S.png', '9H': 'PNG/9H.png', '9D': 'PNG/9D.png', '9C': 'PNG/9C.png',
           '10S': 'PNG/10S.png', '10H': 'PNG/10H.png', '10D': 'PNG/10D.png', '10C': 'PNG/10C.png',
           'JS': 'PNG/JS.png', 'JH': 'PNG/JH.png', 'JD': 'PNG/JD.png', 'JC': 'PNG/JC.png',
           'QS': 'PNG/QS.png', 'QH': 'PNG/QH.png', 'QD': 'PNG/QD.png', 'QC': 'PNG/QC.png',
           'KS': 'PNG/KS.png', 'KH': 'PNG/KH.png', 'KD': 'PNG/KD.png', 'KC': 'PNG/KC.png',
           'AS': 'PNG/AS.png', 'AH': 'PNG/AH.png', 'AD': 'PNG/AD.png', 'AC': 'PNG/AC.png'}

def get_cells(x,y):
    if x < 300:
        if y < 300:
            return 0
def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    running = True
    GREEN = (0, 255, 0)
    screen.fill(GREEN)
    pygame.display.flip()
    shuffled_cards()
    while True:
        for event in pygame.event.get():
            img = pygame.image.load('resized 9s.png')
            x,y = pygame.mouse.get_pos()
            print (x)
            get_cells(x,y)
            if event.type == pygame.QUIT:
                pygame.display.quit()
<<<<<<< HEAD
            elif event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            elif event.type == MOUSEBUTTONDOWN:
                print('1')
                screen.blit(img, (pygame.mouse.get_pos()))
            pygame.draw.line(screen, BLACK, (300,0), (300,400))
            pygame.draw.line(screen, BLACK, (0, 400), (300,400))
        pygame.display.flip()    
main()
=======
                break
            pygame.draw.line(200, 0)
main()
>>>>>>> 80ef2bd09979364fc88ebd8981da848d42fe093b
