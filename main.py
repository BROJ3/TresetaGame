import random
from card import Card
from deck import Deck
from player import Player
#import game_functions as gf

#gf.start_game() deleted because hands is not returned to be used

moj_spil = Deck()


moj_spil.add_player() #adds player 1
moj_spil.add_player() #adds player 2
hands = moj_spil.deal_cards(num_cards=5)

for player in moj_spil.players:
	print(player.get_name())

print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")
#hands = gf.start_game()
current_player_index = 0

while True:
	current_player = moj_spil.players[current_player_index]
	print(f"\nIt's {current_player.get_name()}'s turn.")
	action= input("what would you like to do?")
    
	if action == 'play':
		
		current_player_index = (current_player_index + 1) % len(moj_spil.players)

		print("\nGAME HS BEGUN, THESE ARE YOUR CARDS\n")
		for hand in hands.items():
			print("===================")
			print(f"{player.get_name()}'s hand")
			print("======================")
			player.show_hand()

			#have a player choose a card to play	
			selected_card = input("Select a card to play\npress q to quit\n")
			selected_suit=input("which suit?")
			print(selected_card," of ", selected_suit," chosen")

			for card in player.hand:
				if selected_card == card.get_name()[0] and selected_suit[0] == card.get_name()[2][0]:
							print("ima taj")
							played_card = player.play_card(card) #works but Do I want it like this

			
			#for card in player.hand:
			#        print(card.get_name())



		

	elif action == 'q':
		break
 