import random
from card import Card
from deck import Deck
from player import Player

moj_spil = Deck()

moj_spil.add_player() #adds player 1
moj_spil.add_player() #adds player 2

hands = moj_spil.deal_cards(num_cards=5)

for player in moj_spil.players:
	print(player.get_name())
	print(player.show_hand())
	print("===")

print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")
#hands = gf.start_game()
current_player_index = 0

while True:

	current_player = moj_spil.players[current_player_index]
	print(f"\nIt's {current_player.get_name()}'s turn.")
	action= input("what would you like to do? (play/q)")
    
	if action == 'play':
		suit_in_play = None
		print(current_player.show_hand())

		#have a player choose a card to play	


		chosen_card = None
		while chosen_card is None:
			selected_number = input("Select a card number: ").capitalize()
			selected_suit = input("Select card suit: ").capitalize()

			# Check if player has cards that match the suit in play
			matching_cards = [card for card in current_player.hand if card.get_suit() == moj_spil.current_suit]

			for card in current_player.hand:
				if selected_number == card.get_number() and selected_suit == card.get_suit():
					if moj_spil.current_suit is None:  # First card of the round
						moj_spil.current_suit = selected_suit
						print(f"Suit in play is now: {moj_spil.current_suit}")
						chosen_card = card
						break
					elif selected_suit != moj_spil.current_suit and matching_cards:
						print(f"You must play a card from the suit in play: {moj_spil.current_suit}")
						chosen_card = None
						break
					else:  # Either the suit matches, or there are no matching cards
						chosen_card = card
						break

			if chosen_card is None:
				print("Invalid selection or wrong suit. Try again.")

			

		############

		##########################
		if chosen_card:
			played_card = current_player.play_card(chosen_card, moj_spil)  # Pass the deck instance
			print(f"Played card: {played_card.get_name()}")
			suit_in_play = card.get_suit()
		else:
			print(f"Invalid card: {selected_number} of {selected_suit} is not in your hand.")

		current_player_index = (current_player_index + 1) % len(moj_spil.players)
		


		print(moj_spil.stack_in_play)

		if len(moj_spil.stack_in_play) == 2:
			moj_spil.determine_winner()
			#suit_in_play = None
			while moj_spil.stack_in_play:
				moj_spil.stack_in_play.pop()
				suit_in_play=None

		
		if len(player.show_hand()) == 0:
			for player in moj_spil.players:
				print(player.get_name())
				print(player.stack)
				print("===")

        			

	elif action == 'q':
		break

 