class Player():
    def __init__ (self,name):
        self.name=name
        self.hand=[]
        self.stack=[]

    def play_card(self,card):
        #remove card from had and throw into played cards
        self.hand.pop(card)

    def get_name(self):
        #Return the id of the player
        return self.name
    
    def show_hand(self):
        for card in self.hand:
		        print(card.get_name())
                    
    
    
