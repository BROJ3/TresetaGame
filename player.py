class Player():
    def __init__ (self,name):
        self.name=name
        self.hand=[]
        self.stack=[]
        self.points=[]

    def play_card(self,card,deck):
        self.hand.remove(card)
        deck.add_to_stack((self,card))
        return card

    def get_name(self):
        #Return the id of the player
        return self.name
    
    def show_hand(self):
        cards_to_return=[]
        for card in self.hand:
            cards_to_return.append(card.get_name())
        return cards_to_return            

                

    
