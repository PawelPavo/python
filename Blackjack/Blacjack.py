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

        # track aces
        if card.rank == "Ace":
            self.aces+=1

    def adjust_for_ace(self):
        
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        # SEE README.md
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

        # using TRUTHY value 0
        '''
        while self.value > 21 and self.aces: # truthy value no need for >0
            self.value -= 10
            self.aces -= 1
        '''

class Chips:
    def __init__(self,total=100):
        self.total=total # this can be adjusted to supplied value by user input
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet



# Asking player how many chips they want to bet and checking if they have enough
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet? '))
        except:
            print('Sorry please provide an integer.')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {} chips left.'.format(chips.total))
            else:
                break

# function to hit
def hit(deck,hand):

    # adding card from the hand and adjusting for Ace
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# function to see if player wants to hit or stand
def hit_or_stand(deck,hand):
    global playing # controls a while loop
    while True:
        x = input('Hit or Stanb? Enter h or s ')
        if x[0].lower() == 'h':  # x[0] is to check if someone may write "hit" or "hh" for example
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing=False
        else:
            print('Sorry, I did not understand that, please eneter h or s only! ')
            continue
        break

# Functions to display cards

def show_some(player, dealer):
    # Show only ONE of dealers hand/cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    # Show all (2 cards) of the players hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    # Show all the dealers cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # One line to for for loop
    '''
    print(f"Dealer's hand: ",*dealer.cards,sep='\n')
    '''
    
        
    # calculare and display value ex. (J+K = 20)
    print("Value of Dealer's Hand is: {}".format(dealer.value))

    # Show all the players cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    
    print("Value of Players's Hand is: {}".format(player.value))

# End of game scenarios

def player_busts(player,dealer,chips):
    print('BUST PLAYER')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and Player tie! PUSH')



# GAME

while True:
    # Print an opening statement
    print('Welcome to Blackjack')

    # Create and shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()

    # Deal to Player
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Deal to Dealer
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips=Chips()

    # Prompt the Player for Bet
    take_bet(player_chips)

    # Show Card (but keep the dealer's card hidden)
    show_some(player_hand,dealer_hand)

    while playing: # playing comes from hit_or_stand function

        # Prompt player to Hit or Stnad
        hit_or_stand(deck,player_hand)

        # Show cards (but keep dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_bust() and break the loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand, player_chips)
            break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all Cards
        show_all(player_hand,dealer_hand)
        
        # Run diffrent winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))

    # Ask to play again
    new_game=input("Would you like to play another hand? y/n: ")

    if new_game[0]=='y':
        playing=True
    else:
        print('Thank you for playing!')
        break
        


