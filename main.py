import random
from card import Card
from deck import Deck
from hand import Hand


moj_spil = Deck()

moj_spil.add_player("Player 1")
moj_spil.add_player("Player 2")

hands = moj_spil.deal_cards(num_cards=10)

for player, hand in hands.items():
    print("===================")
    print(f"{player}'s hand")
    print("======================")
    for card in hand:
        print(card.get_name())
        print(card.get_value())

print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")

while True:
	action= input("what would you like to do?")
    
	if action == 'play':

		#print("GAME HS BEGUN, THESE ARE YOUR CARDS")

		for player, hand in hands.items():
			if player == 'Player 1':
				for card in hand:
					print(card.get_name())
				selected_card = input("Select a card to play\n")
				selected_suit = input("Select a suit to play\n")
				for card in hand:
					if selected_card == card.get_name()[0]:
						print("idemo")
						hand.pop(int(selected_card))
					#print(len(hand))
					

				#print('===========================') 
				#card_played_number = input("What card do you want to play\n")
				#card_played_suit = input("Of which suit?\n")
				#if card_played_number == card.get_name()[0]:
					#Hand.cards.pop(card)
					#	print("ima majstore")
					#else: 
					#	print("Otkud??????")
		#	elif player == 'Player 2':
		#		print("DRUGE KARTE")
		#		for card in hand:
		#			print(card.get_name())
		#print("IT WOULD BE HELPFUL TO BE ABLE TO POP ONE CARD INTO THE POT TO PLAY AND TAKE TURNS DOING IT WHILST D")

	if action == 'q':
    		break