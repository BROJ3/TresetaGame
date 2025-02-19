import random
from game_functions import setup_game, take_turn, check_winner
from card import Card
from deck import Deck
from player import Player

moj_spil = setup_game()

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
		take_turn(current_player, moj_spil)
		current_player_index = (current_player_index + 1) % len(moj_spil.players)
		
		#mechanics for "hand"
		if len(moj_spil.stack_in_play) == 2:
			current_player_index = moj_spil.determine_winner() 
			while moj_spil.stack_in_play:
				moj_spil.stack_in_play.pop()
				suit_in_play=None
				moj_spil.current_suit=None
		
		#print points once game is "done"
		if check_winner(moj_spil):
			break
       			
	elif action == 'q':
		break

 