class Player():
    def __init__ (self,name):
        self.name=name
        self.hand=[]
        self.stack=[]

    def play_card(self,card):
        #remove card from had and throw into played cards
        self.pop(card)

    def get_name(self):
        #Return the id of the player
        return self.name