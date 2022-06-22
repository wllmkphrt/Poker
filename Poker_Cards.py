#2022 William Kephart

import numpy as np

#Defines a card class
class Card:
    def __init__(self, number, suit, position):
        self.number = number
        self.suit = suit

#randomizes order of cards via Fisher-Yates Algorithm
def shuffle(cardorder, numCards):
    for i in range(numCards-1,0,-1):
        rng = np.random.default_rng()
        j = rng.integers(0, numCards)
        cardorder[i],cardorder[j] = cardorder[j],cardorder[i]
    return cardorder

cardorder = []
for i in range(52):
    cardorder.append(i)
n = len(cardorder)

Cards = np.empty(52, dtype = object)
Cardnum = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for i in range(13):
        Cards[i] = Card(Cardnum[i], 'Spade', i)
        Cards[i+13] = Card(Cardnum[i], 'Club', i+13)
        Cards[i+26] = Card(Cardnum[i], 'Heart', i+26)
        Cards[i+39] = Card(Cardnum[i], 'Diamond', i+39)

cardorder = shuffle(cardorder, n)

for i in range(52):
    print(Cards[cardorder[i]].number, Cards[cardorder[i]].suit)
