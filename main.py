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
		print("\nGAME HAS BEGUN, THESE ARE YOUR CARDS\n")
		suit_in_play = None
		print(current_player.show_hand())

		#have a player choose a card to play	
		selected_number = input("Select a card to play\n")
		selected_suit=input("which suit?")

		chosen_card = None

		for card in current_player.hand:
			if selected_number.capitalize() == card.get_number() and selected_suit.capitalize() == card.get_suit():
				chosen_card=card
				suit_in_play = card.get_suit()
				break

		if chosen_card:
			played_card = current_player.play_card(chosen_card, moj_spil)  # Pass the deck instance
			print(f"Played card: {played_card.get_name()}")
			

		else:
			print(f"Invalid card: {selected_number} of {selected_suit} is not in your hand.")

		current_player_index = (current_player_index + 1) % len(moj_spil.players)
		


		print(moj_spil.stack_in_play)

		if len(moj_spil.stack_in_play) == 2:
			moj_spil.determine_winner()
			suit_in_play = None
			while moj_spil.stack_in_play:
				moj_spil.stack_in_play.pop()

		
		if len(player.show_hand()) == 0:
			for player in moj_spil.players:
				print(player.get_name())
				print(player.show_hand())
				print(player.stack)
				print("===")

        			

	elif action == 'q':
		break

 