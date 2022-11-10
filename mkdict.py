f = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
s = ['S','H','D','C']

cards = []
for face in f:
    for suit in s:
        cards.append(str(face)+str(suit))
        
        
print(cards)

card_dict = {}

for card in cards:
    card_dict[card]="PNG/" + card +".png"
    
print(card_dict)


                     
            