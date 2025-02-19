class Player():
    def __init__ (self,name):
        self.name=name
        self.hand=[]
        self.stack=[]
        self.points=[]

    def play_card(self,card,deck):
        self.hand.remove(card)
        deck.add_to_stack((self,card))
        self.sort_hand()
        return card

    def get_name(self):
        #Return the id of the player
        return self.name
    
    def show_hand(self):
        cards_to_return=[]
        for card in self.hand:
            cards_to_return.append(card.get_name())
        return cards_to_return            

                
    def calculate_points(self):
        total_points = 0
        for card in self.stack:
            total_points += card.get_bella_value()  # Assuming you have get_bella_value() in Card
        return total_points



    def receive_card(self, card):
        """Add a card to hand and immediately re-sort it."""
        self.hand.append(card)
        self.sort_hand()

    def sort_hand(self):
        """Sorts hand by suit first, then by value within each suit."""
        suit_order = {'Kupe': 0, 'Bate': 1, 'Spade': 2, 'Denari': 3}  # Define a fixed suit order
        self.hand.sort(key=lambda card: (suit_order[card.get_suit()], card.get_value()))