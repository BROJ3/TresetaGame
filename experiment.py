from card import Card
class Deck:
    def __init__(self):
        self.cards = []  # The deck of cards
        self.stack = []  # The played cards pile

    def add_to_stack(self, card):
        """
        Add a card to the played cards pile (stack).
        """
        self.stack.append(card)

    def show_stack(self):
        """
        Show all cards in the played cards pile.
        """
        return [card.get_name() for card in self.stack]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card, deck):
        """
        Removes the specified card from the player's hand and adds it to the deck's stack.
        If the card is not in the player's hand, raises a ValueError.
        """
        if card in self.hand:
            self.hand.remove(card)
            deck.add_to_stack(card)  # Add the played card to the deck's stack
            return card
        else:
            raise ValueError(f"Card {card.get_name()} is not in {self.name}'s hand.")

    def show_hand(self):
        """
        Return a list of card names in the player's hand.
        """
        return [card.get_name() for card in self.hand]


# Create a deck and a player
deck = Deck()
player = Player("Alice")

# Create some cards
card1 = Card("Hearts", 10, "10")
card2 = Card("Spades", 1, "Ace")

# Add cards to the player's hand
player.hand.extend([card1, card2])
# Player plays a card
try:
    played_card = player.play_card(card1, deck)  # Pass the deck instance
    print(f"Played card: {played_card.get_name()}")
except ValueError as e:
    print(e)

# Show the player's remaining hand
print("Remaining hand:", player.show_hand())

# Show the stack in the deck
print("Stack in the deck:", deck.show_stack())
