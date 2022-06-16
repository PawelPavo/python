# CARD CLASS
# SUIT, RANK, VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

# TESTING Card CLASS and value compare
'''
two_hearts= Card("Hearts","Two")
three_clubs=Card("Clubs", "Three")
print(three_clubs.value < two_hearts.value)
'''

# DECK CLASS
# Created a deck with an object of 52 cards

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
                
    # Shuffles the deck
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    #
    def deal_one(self):
        return self.all_cards.pop()

# TESTING shuffle_deck METHOD of DECK CLASS
'''
new_deck=Deck()
bottom_card=new_deck.all_cards[-1]
print(bottom_card)
new_deck.shuffle_deck()
print(new_deck.all_cards[-1])
'''

# TESTING deal_one METHOD of DECK CLASS
'''
new_deck=Deck()
new_deck.shuffle_deck()
myCard=new_deck.deal_one()
print(myCard)
print(len(new_deck.all_cards))
'''

# PLAYER CLASS
# Creating a class for Players

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    #removes the card from the top of the players deck - from the start of the list
    def remove_one(self):
        return self.all_cards.pop(0) 

     # adds cards to the bottom of the players deck - to the end of the list
    def add_cards(self, new_cards):
        # 'if' statement that compares the TYPE of the args 'if list'
        # if it is a list, that means there are more than 1 cards to add to the deck

        if type(new_cards)==type([]):
            # adding a LIST of Card objects - list of cards
            self.all_cards.extend(new_cards) # use of 'extend()'
        else:
            # adding a SINGLE  Card object
            self.all_cards.append(new_cards) # use of 'append()'

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# TESTING Player CLASS and METHODS
'''
new_deck=Deck() # Create a new deck
new_player=Player("Pawel")  # Create a player   
myCard=new_deck.deal_one() # deal one card
print(myCard) # check what card was delt
new_player.add_cards(myCard) # player 1 gets the delt card
print(new_player) # check if the player has the card
print(new_player.all_cards[0]) # check if its the card matched

# checking to see if list of cards adds correctly (same card is added for example)
new_player.add_cards([myCard,myCard,myCard]) 
print(new_player)

# checking remove method
new_player.remove_one()
print(new_player)
'''


