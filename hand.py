from deck import Deck

class Hand(Deck):
    def __init__ (self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)  
        
