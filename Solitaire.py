import random
import math
import pygame
import sys
from pygame.locals import *
def make_card_deck():
    f = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    s = ['S','H','D','C']

    cards = []
    for face in f:
        for suit in s:
            cards.append(str(face)+str(suit))
    # print(len(cards))
            
            
    return cards

   

def make_card_dict(cards):
    card_dict = {}
    for card in cards:
        card_dict[card]="PNG/" + card +".png"
        
    return card_dict
   
# def shuffled_cards():
    # deck = ['4H', '5H', '10D', '4D', '5H', '3S', '5H', '8C', '3S', '5D', '3C', '6C', '7S',
    #         '5D', 'AS', '6D', '7H', 'QS', 'QC', 'QD', '3S', '3D', '2S', '8D', '7H', '4D',
    #         '10S', '9S', '9S', '2H', 'JC', '1H', '9D', '3D', '8H', '7H', '9H', '3H', 'JH',
    #         'JC', 'AD', '6D', 'QC', '7S', '6C', 'AD', '3D', 'KC', '8S', '1S', 'KD']
    # key = {'2S': 'PNG/2S.png', '2H': 'PNG/2H.png', '2D': 'PNG/2D.png', '2C': 'PNG/2C.png',
    #        '3S': 'PNG/3S.png', '3H': 'PNG/3H.png', '3D': 'PNG/3D.png', '3C': 'PNG/3C.png',
    #        '4S': 'PNG/4S.png', '4H': 'PNG/4H.png', '4D': 'PNG/4D.png', '4C': 'PNG/4C.png',
    #        '5S': 'PNG/5S.png', '5H': 'PNG/5H.png', '5D': 'PNG/5D.png', '5C': 'PNG/5C.png',
    #        '6S': 'PNG/6S.png', '6H': 'PNG/6H.png', '6D': 'PNG/6D.png', '6C': 'PNG/6C.png',
    #        '7S': 'PNG/7S.png', '7H': 'PNG/7H.png', '7D': 'PNG/7D.png', '7C': 'PNG/7C.png',
    #        '8S': 'PNG/8S.png', '8H': 'PNG/8H.png', '8D': 'PNG/8D.png', '8C': 'PNG/8C.png',
    #        '9S': 'PNG/9S.png', '9H': 'PNG/9H.png', '9D': 'PNG/9D.png', '9C': 'PNG/9C.png',
    #        '10S': 'PNG/10S.png', '10H': 'PNG/10H.png', '10D': 'PNG/10D.png', '10C': 'PNG/10C.png',
    #        'JS': 'PNG/JS.png', 'JH': 'PNG/JH.png', 'JD': 'PNG/JD.png', 'JC': 'PNG/JC.png',
    #        'QS': 'PNG/QS.png', 'QH': 'PNG/QH.png', 'QD': 'PNG/QD.png', 'QC': 'PNG/QC.png',
    #        'KS': 'PNG/KS.png', 'KH': 'PNG/KH.png', 'KD': 'PNG/KD.png', 'KC': 'PNG/KC.png',
    #        'AS': 'PNG/AS.png', 'AH': 'PNG/AH.png', 'AD': 'PNG/AD.png', 'AC': 'PNG/AC.png'}

def shuffle(dk):
    shuffled_deck=[]
    
    while len(dk)>0:
        pos = random.randint(0,len(dk)-1)

        
        print("deck",dk)

        # print("pos", pos)
        shuffled_deck.append(dk.pop(pos))
        
    return shuffled_deck
    
        
def get_cells(x,y):
    if x < 300:
        if y < 470:
            return 0


def main():
    deck = make_card_deck()
    imgs = make_card_dict(deck)
    # print(deck)
    # print(imgs)
    deck = shuffle(deck)
    
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    running = True
    GREEN = (0, 255, 0)
    BLACK = (0,0,0)
    screen.fill(GREEN)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            x,y = pygame.mouse.get_pos()
            print (x)
            get_cells(x,y)
            if event.type == pygame.QUIT or event.type == KEYDOWN:
                pygame.display.quit()
            elif event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            elif event.type == MOUSEBUTTONDOWN and get_cells(x,y) == 0:
                img = pygame.image.load(imgs[deck.pop()])
                print('1')
                screen.blit(img, (0, 0))
            
            img2 = pygame.image.load('resized 2.png')
            screen.blit(img2, (0,0))
            pygame.draw.line(screen, BLACK, (300,0), (300,470))
            pygame.draw.line(screen, BLACK, (0, 470), (300,470))
            pygame.draw.line(screen, BLACK, (570,470), (1920,470))
            pygame.draw.line(screen, BLACK, (570,470), (570, 0))
            pygame.draw.line(screen, BLACK, (920,470), (920, 0))
        pygame.display.flip()    
main()
