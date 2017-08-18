import random

class card:
    def __init__(self,suit,value):
        self.s=suit
        self.v=value

    def __str__(self):
        return self.s,'of'readable_suit(self.v)

    def readable_suit(self):
        if self.s==s:
            return 'spades'
        elif self.s==h:
            return 'hearts'
        elif self.s==d:
            return 'diamonds'
        elif self.s==c:
            return 'clubs'
        elif self.s==j:
            return 'joker'
        else:
            return 'invalid suit'

    def card_value(self):
        values=[1,2,3,4,5,6,7,8,9,10,J,Q,K,A]
        for i in range(len(values)):
            if self.v==values[i]:
                return i
        else:
            return 'invalid value'

    def __gt__ (self,other_card,best_suit)
        if self.s==best_suit and other_card.s!=best_suit:
            return True
        if self.s!=best_suit and other_card.s==best_suit:
            return False
        if (self.s==best_suit and other_card.s==best_suit) or (self.s!=best_suit and othercard.s!=best_suit):
            if self.v

class Deck_of_cards:
    def __init__(self)
        deck=[]
        for char in 'shdc':
            for value in [2,3,4,5,6,7,8,9,10,J,Q,K,A]:
                deck=deck+card(char,value)
        deck.append(card(joker,none)*2)
        self.deck=deck

    def __str__(self):
        return deck

    def shuffle_deck(self):
        for i in range(1000):
            deck.append(deck.pop(random.randint(0,len(deck))))
        return deck

    def deal_deck(self,players,cards,k):
        players={}
        for n in range(players):
            players[n]=None #create players as keys of dictionary
            for i in range(cards*players): #loop for number of cards to be dealt as a list into dictionary value
                players[n]=deck.pop[(cards*players)%n]
        return players[k] #show kth players hand from the dictionary
