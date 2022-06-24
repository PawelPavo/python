# BLACKJACK
import random


# Creating a Deck of 52 Cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing=True


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    def __init__(self):
        # start with an empty list
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                # build Card objects and add them to the list
                self.deck.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        # start with an empty string
        deck_comp = ''
        for card in self.deck:
            # add each Card object's print string
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        # the card passed in is from the Deck.deal() --> it gives us Card(suit,rank)
        self.cards.append(card)
        # adjusting the value of self.value to see if its 21 or more
        self.value+=values[card.rank]

    def adjust_for_ace(self):
        pass
'''
# TEST
test_deck=Deck()
test_deck.shuffle()

# Player
test_player=Hand()

# Deal 1 card from the deck CARD(suit,rank)
deal_card=test_deck.deal()
print(deal_card)
test_player.add_card(deal_card)
print(test_player.value)

# add card other way
test_player.add_card(test_deck.deal())
print(test_player.value)
'''
