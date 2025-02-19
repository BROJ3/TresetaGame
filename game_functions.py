from card import Card
from deck import Deck
from player import Player

def setup_game():
    """Initialize the game, add players, and deal cards."""
    moj_spil = Deck()
    moj_spil.add_player()  # Player 1
    moj_spil.add_player()  # Player 2
    moj_spil.deal_cards(num_cards=10)
    return moj_spil

def take_turn(current_player, moj_spil):
    print(current_player.show_hand())
    """Handle a single player's turn."""
    print(f"\nIt's {current_player.get_name()}'s turn.")
    suit_in_play = moj_spil.current_suit
    chosen_card = None
    
    while chosen_card is None:
        selected_number = input("Select a card number: ").capitalize()
        selected_suit = input("Select card suit: ").capitalize()

        matching_cards = [card for card in current_player.hand if card.get_suit() == suit_in_play]

        for card in current_player.hand:
            if selected_number == card.get_number() and selected_suit == card.get_suit():
                if suit_in_play is None or selected_suit == suit_in_play or not matching_cards:
                    chosen_card = card
                    moj_spil.current_suit = selected_suit
                    break
                else:
                    print(f"You must play a card from the suit in play: {suit_in_play}")
        
        if chosen_card is None:
            print("Invalid selection or wrong suit. Try again.")

    played_card = current_player.play_card(chosen_card, moj_spil)
    print(f"Played card: {played_card.get_name()}")
    return played_card

def check_winner(moj_spil):
    """Check if the game is over and calculate points."""
    if not moj_spil.playing_deck_list and all(len(player.hand) == 0 for player in moj_spil.players):
        if moj_spil.last_hand_winner:
            print(f"{moj_spil.last_hand_winner.get_name()} gets an extra point for winning the last hand!")
            moj_spil.last_hand_winner.points.append(1)

        for player in moj_spil.players:
            player_points = player.calculate_points() + len(player.points)
            print(f"{player.get_name()} scored {player_points:.2f} points.")
        print("Game over!")
        return True
    return False
