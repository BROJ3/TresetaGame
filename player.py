class Player():
    def __init__ (self,name):
        self.name=name
        self.hand=[]
        self.stack=[]

    def play_card(self,card):
        #remove card from had and throw into played cards
        self.hand.remove(card)
        return card

    def get_name(self):
        #Return the id of the player
        return self.name
    
    def show_hand(self):
        cards_to_return=[]
        for card in self.hand:
            cards_to_return.append(card.get_name())
        return cards_to_return            

                

    
