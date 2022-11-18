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
        card_dict[card]="PNG/" + card  +"_ltl.png"
        
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
    
    #draw card
    if x < 300 and x > 0:
        if y < 300:
            return 0,0
    #ace area
    if x < 770 and x > 570: 
        if y < 310:
            return 570,0
    #first row
    if y > 300:
        if x < 300 and x >= 0:
            return 0,310
    #second row
    if y > 300:
        if x > 300 and x <= 450:
            return 250,310
    #third row
    if y > 300 and y < 610:
        if x > 500 and x <= 700:
            return 500,310
    #fourth row
    if y > 300 and y < 610:
        if x > 750 and x <= 950:
            return 750,310
    #fifth row
    if y > 300 and y < 610:
        if x > 1000 and x <= 1200:
            return 1000, 310
    #sixth row
    if y >300 and y < 610:
        if x > 1250 and x <= 1450:
            return 1250,310
    #7th row
    if y > 300 and y < 610:
        if x > 1500 and x < 1700:
            return 1500, 310
    #ace slot 2
    

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
    RED = (255,0,0)
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
                c = get_cells(x,y) # (0,0)
                if(c in [(0,0), (570,0), (0,310), (250,310), (500,310), (750,310), (1000,310), (1250,310), (1500,310)]):
                    img = pygame.image.load(imgs[deck.pop()])
                    print(img)
                    print('1')
                    screen.blit(img, c)
               # if screen.blit(img, get_cells(x,y)):
                    
            #draw from deck lines
            pygame.draw.line(screen, BLACK, (200,0), (200,310))
            pygame.draw.line(screen, BLACK, (0, 310), (200,310))
            #Upper ace grid + ace slot 1
            pygame.draw.line(screen, BLACK, (570,310), (1920,310))
            pygame.draw.line(screen, BLACK, (570,310), (570, 0))
            pygame.draw.line(screen, BLACK, (770,310), (770, 0))
            #first left row
            pygame.draw.line(screen, BLACK, (200,310), (200, 610))
            pygame.draw.line(screen, BLACK, (0,610), (200,610))
            #second row
            pygame.draw.line(screen,BLACK, (250,310),(250, 610))
            pygame.draw.line(screen, BLACK, (450,310), (450,610))
            pygame.draw.line(screen, BLACK, (250, 310), (450,310))
            pygame.draw.line(screen, BLACK, (250,610), (450, 610))
            #third row
            pygame.draw.line(screen, BLACK, (500,610), (700, 610))
            pygame.draw.line(screen, RED, (500,310), (700, 310))
            pygame.draw.line(screen, BLACK, (500,310), (500,610))
            pygame.draw.line(screen, BLACK, (700,310), (700,610))
            #Fourth row
            pygame.draw.line(screen, BLACK, (750,310), (750,610))
            pygame.draw.line(screen, BLACK, (950,310), (950,610))
            pygame.draw.line(screen, BLACK, (750,610), (950,610))
            #fifth row
            pygame.draw.line(screen, BLACK, (1000,310), (1000,610))
            pygame.draw.line(screen, BLACK, (1200,310), (1200,610))
            pygame.draw.line(screen, BLACK, (1000,610), (1200,610))
            #sixth row
            pygame.draw.line(screen, BLACK, (1250,310), (1250,610))
            pygame.draw.line(screen, BLACK, (1450,310), (1450,610))
            pygame.draw.line(screen, BLACK, (1250,610), (1450,610))
            #last row
            pygame.draw.line(screen, BLACK, (1500,310), (1500,610))
            pygame.draw.line(screen, BLACK, (1700,310), (1700,610))
            pygame.draw.line(screen, BLACK, (1500,610), (1700,610))
            #Ace slot 2
            pygame.draw.line(screen, BLACK, (820, 0), (820,310))
            pygame.draw.line(screen, BLACK, (1020,310), (1020, 0))
            #Ace slot 3
            pygame.draw.line(screen, BLACK, (1070,310), (1070,0))
            pygame.draw.line(screen, BLACK, (1270,310), (1270,0))
            #ace slot 4
            pygame.draw.line(screen, BLACK, (1320,310), (1320,0))
            pygame.draw.line(screen, BLACK, (1520,310), (1520,0))
        pygame.display.flip()    
main()
