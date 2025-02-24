from card import Card
from deck import Deck
from player import Player

def setup_game():
    moj_spil = Deck()
    moj_spil.add_player()  # Player 1

    player_2_type = input("Do you want Player 2 to be a bot? (y/n): ").strip().lower()

    if player_2_type == 'y':
        moj_spil.add_player("Bot_2")  # Bot player
        print("Player 2 is now a bot!")
    else:
        moj_spil.add_player()  # Normal Player 2 (human)
        print("Player 2 is another human!")

    moj_spil.deal_cards(num_cards=10)
    return moj_spil

def take_turn(current_player, moj_spil): 
    
    if current_player.get_name() == "Bot_2":
        return bot_play_turn(current_player, moj_spil)

    print(current_player.show_hand())
    print(f"\nIt's {current_player.get_name()}'s turn.")
    suit_in_play = moj_spil.current_suit
    chosen_card = None

    while chosen_card is None:
        selected_number = input("Select a card number: ").capitalize()
        selected_suit = input("Select card suit: ").capitalize()

        matching_cards = [card for card in current_player.hand if card.get_suit() == suit_in_play]
        for card in current_player.hand:
            if selected_number == card.get_number() and selected_suit == card.get_suit():
                if suit_in_play is None:
                    moj_spil.current_suit = selected_suit
                    chosen_card = card
                    break
                elif selected_suit == suit_in_play or not matching_cards:
                    chosen_card = card
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

def bot_play_turn(bot_player, moj_spil):
    """Bot logic: Must follow suit if possible, otherwise plays lowest card and loses."""
    suit_in_play = moj_spil.current_suit
    valid_cards = [card for card in bot_player.hand if card.get_suit() == suit_in_play]

    if valid_cards:
        # Follow suit and decide strategy: Play high if aggressive, low if defensive
        chosen_card = max(valid_cards, key=lambda card: card.get_value())  # Play highest valid card
    else:
        # If the bot has no valid suit cards, play the lowest-value card and lose
        chosen_card = min(bot_player.hand, key=lambda card: card.get_value())

    print(f"{bot_player.get_name()} (Bot) played {chosen_card.get_name()}.")
    bot_player.play_card(chosen_card, moj_spil)
    moj_spil.current_suit = chosen_card.get_suit()
    suit_in_play = chosen_card.get_suit()

    return chosen_card

