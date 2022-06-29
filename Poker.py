#2022 William Kephart

import numpy as np
import mysql.connector

#Defines a card class
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit



#Defines a player class
class Player:
    def __init__(self, username, cashAmount):
        self.username = username
        self.cashAmount = cashAmount
        playerID = None
        inp1 = input('What is your password?')
        inp2 = input('Please type your password again to confirm.')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="TestPassword!",
            database="Poker"
        )

        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO Users (name, cash) VALUES(%s, %s)", (username, cashAmount))
        mydb.commit()

#Defines a poker table class
class Table:
    def __init__(self, cardorder, Seats = [False, False, False, False, False, False, False, False, False], 
                 seatcount = 0, full = False, dealerID = 0):
        self.cardorder = shuffle(cardorder, len(cardorder))
        self.Seats = Seats
        self.seatcount = seatcount
        self.dealerID = dealerID
        self.full = full
        Tables.append(self)

def newPokerDB():
    Tables = []
    Cardnum = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    Cards = np.empty(52, dtype = object)
    OGcardorder = []

#instantiates an array of cards to be shuffled at each table
for i in range(52):
    OGcardorder.append(i)
for i in range(13):
    Cards[i] = Card(Cardnum[i], 'Spade')
    Cards[i+13] = Card(Cardnum[i], 'Club')
    Cards[i+26] = Card(Cardnum[i], 'Heart')
    Cards[i+39] = Card(Cardnum[i], 'Diamond')

def newUser():
    inp = input('What is your username?\n')
    mynewUser = Player(inp, 25)
    return mynewUser

#randomizes order of cards via Fisher-Yates Algorithm
def shuffle(cardorder, numCards):
    for i in range(numCards-1,0,-1):
        rng = np.random.default_rng()
        j = rng.integers(0, numCards)
        cardorder[i],cardorder[j] = cardorder[j],cardorder[i]
    return cardorder


def joinTable(player, cardorder):
    if (len(Tables) == 0):
        Table(cardorder)
        player.playerID = '00'
        Tables[0].Seats[0] = True
        Tables[0].seatcount += 1
    for i in range(len(Tables)):
        if (Tables[i].full == False):
            for j in range(len(Tables[i].Seats)):
                if (Tables[i].Seats[j] == False):
                    player.playerID = str(i)+str(j)
                    Tables[i].Seats[j] = True
                    Tables[i].seatcount += 1
                    if (Tables[i].seatcount == 9):
                        Tables[i].full = True
                        return
                    return
        else:
            Table(cardorder)
            player.playerID = str(i+1)+'0'
            return

def dealholecards(seatcount, Table):
    tableID = []
    for i in range(playerNum):
        tableID.append(playerNum)

for i in range(52):
    print(Cards[cardorder[i])

joinTable(newUser(), OGcardorder)











