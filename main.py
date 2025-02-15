import random
from card import Card
from deck import Deck
from player import Player

moj_spil = Deck()

moj_spil.add_player() #adds player 1
moj_spil.add_player() #adds player 2

hands = moj_spil.deal_cards(num_cards=10)

for player in moj_spil.players:
	print(player.get_name())
	print(player.show_hand())
	print("===")

#hands = gf.start_game()
current_player_index = 0

while True:

	current_player = moj_spil.players[current_player_index]
	print(f"\nIt's {current_player.get_name()}'s turn.")
	action= input("what would you like to do? (play/q)")
    
	if action == 'play':
		suit_in_play = None
		print(current_player.show_hand())


		chosen_card = None
		while chosen_card is None:
			selected_number = input("Select a card number: ").capitalize()
			selected_suit = input("Select card suit: ").capitalize()

			# Check if player has cards that match the suit in play
			matching_cards = [card for card in current_player.hand if card.get_suit() == moj_spil.current_suit]

			#it is same as this:
			#matching_cards = []
			#for card in current_player.hand:
				#if card.get_suit() == moj_spil.current_suit:
					#matching_cards.append(card)

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

			
		if chosen_card:
			played_card = current_player.play_card(chosen_card, moj_spil)  # Pass the deck instance
			print(f"Played card: {played_card.get_name()}")
			suit_in_play = card.get_suit()
		else:
			print(f"Invalid card: {selected_number} of {selected_suit} is not in your hand.")

		current_player_index = (current_player_index + 1) % len(moj_spil.players)
		
		#mechanics for "hand"
		if len(moj_spil.stack_in_play) == 2:
			current_player_index = moj_spil.determine_winner() 
			while moj_spil.stack_in_play:
				moj_spil.stack_in_play.pop()
				suit_in_play=None
		
		#print points once game is "done"
		if len(player.show_hand()) == 0:
			for player in moj_spil.players:
				print(player.get_name())
				print(len(player.stack))
				print("===")

		#count point
		if not moj_spil.playing_deck_list and all(len(player.hand) == 0 for player in moj_spil.players):

			if moj_spil.last_hand_winner:
				print(f"{moj_spil.last_hand_winner.get_name()} gets an extra point for winning the last hand!")
				moj_spil.last_hand_winner.points.append(1)

			for player in moj_spil.players:
				player_points = player.calculate_points() + len(player.points)
				print(f"{player.get_name()} scored {player_points:.2f} points.")
				print("Game over!")

			break
			#for player in moj_spil.players:
			#	player_points = player.calculate_points()
			#	print(f"{player.get_name()} scored {player_points:.2f} points.")
			#break



        			
	elif action == 'q':
		break

 