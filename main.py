import random
from card import Card
from deck import Deck
#from hand import Hand
from player import Player


moj_spil = Deck()

moj_spil.add_player() #adds player 1
moj_spil.add_player() #adds player 2
hands = moj_spil.deal_cards(num_cards=5)
for player in moj_spil.players:
	print(player.get_name())

print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")



while True:
	action= input("what would you like to do?")
    
	if action == 'play':
		played_cards=[]

		print("\nGAME HS BEGUN, THESE ARE YOUR CARDS\n")
		for player, hand in hands.items():
			print("===================")
			print(f"{player.get_name()}'s hand")
			print("======================")
			player.show_hand()

			#have a player choose a card to play	
			selected_card = input("Select a card to play\n")
			selected_suit=input("which suit?")
			print(selected_card," of ", selected_suit," chosen")

			for card in player.hand:
				if selected_card == card.get_name()[0] and selected_suit[0] == card.get_name()[2][0]:
							print("ima taj")
							
			#for card in player.hand:
			#        print(card.get_name())



		

	elif action == 'q':
		break
