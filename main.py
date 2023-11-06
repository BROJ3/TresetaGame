import random
from card import Card
from deck import Deck
from hand import Hand


moj_spil = Deck()

moj_spil.add_player("Player 1")
#moj_spil.add_player("Player 2")

hands = moj_spil.deal_cards(num_cards=4)

for player, hand in hands.items():
    print("===================")
    print(f"{player}'s hand")
    print("======================")
    for card in hand:
        print(card.get_name())
        #print(card.get_value())

print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")

while True:
	action= input("what would you like to do?")
    
	if action == 'play':

		print("\nGAME HS BEGUN, THESE ARE YOUR CARDS\n")
		for player, hand in hands.items():

			if player == 'Player 1':
				#print the player's cards
				for card in hand:
					print(card.get_name())

				#select a card to play
				print("Which card do you want to play?")	
				selected_card = input("Select a card to play\n")
				selected_suit=input("which suit?")
				print(selected_card," of ", selected_suit," chosen")
				
				for card in hand:
					print(card.get_name())
					if selected_card == card.get_name()[0] and selected_suit[0] == card.get_name()[2][0]:
						print("ima taj")
					else:
						print("nema taj")
					
					
						
					


	if action =='help':
		print("no help yet, but press q to exit")

	elif action == 'q':
    		break

		