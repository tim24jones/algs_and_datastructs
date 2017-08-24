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
            if self.v> othercard.v:
                return True
            elif self.v<othercard.v:
                return False
            elif self.v==othercard.v and self.s==othercard.s and best_suit==None:
                if play_order.play==0:
                    if play_order.first_play.s==self.s and play_order.first_play.s!=othercard.s:
                        return True
                    else:
                        return False
                elif play_order.play==None:
                    if (self.s==s and other_card.s!=s) or (self.s==h and other_card.s!=(s or h)) or (self.s==d and other_card.s!=(s or h or d)) or (self.s==c and other_card.s!=(s or h or d or c):
                        return True
                    else:
                        return False

class Dealer:
    def __init__(self,cards_available,players,number_to_deal)
    def full_deck(self)                                                                                                                                                    
        deck=[]
        for char in 'shdc':
            for value in [2,3,4,5,6,7,8,9,10,J,Q,K,A]:
                deck=deck+card(char,value)
        deck.append(card(joker,none)*2)
        self.deck=deck

    def __str__(self):
        self.cards_available=cards_available

    def shuffle_deck(cards_available): 
        for i in range(1000): #good when cards_available<<1000 (most of the time). If not, increase this number
            x=deck.append(deck.pop(random.randint(0,len(deck))))
        self.cards_available=x
#next section to be reworked
#    def deal_deck(self,players,cards,k):
#        players={}
#        for n in range(players):
#            players[n]=None #create players as keys of dictionary (probably a bad idea, rework with 'players' class)
#            for i in range(cards*players): #loop for number of cards to be dealt as a list into dictionary value
#                players[n]=deck.pop[(cards*players)%n]
#        return players[k] #show kth players hand from the dictionary
     
class player:
    def __init__(self,hand,playorder)
        self.hand=hand
        self.playorder=playorder
    def playcard:
        #remove card from hand list usually to play_area
    def recievecard:
        #add card to hand list, usually from dealer
    def trickpile
        #add cards to tricks from play_area
    def card_pile(self,face_up_or_down,fanned_or_stacked)
        #have a card pile to work with, depending on game
class play_area:
    def __init__(self,hand)
        self.cards=hand
    def card_pile(self,face_up_or_down,fanned_or_stacked)
        #have a card pile to work with, depending on game

