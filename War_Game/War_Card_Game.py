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
