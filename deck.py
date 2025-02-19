import random
from player import Player
from card import Card

class Deck():
	#defining numbers an suits of the deck
	SUIT_TUPLE = ('Kupe','Bate','Spade','Denari')
	STANDARD_DICT = {'4':1,'5':2,'6':3,'7':4,'Fanat':5,'Caval':6,'King':7,'Ace':8,'2':9,'3':10}

	def __init__(self,rank_value_dict=STANDARD_DICT):
		
		self.starting_deck_list=[] #pre-shuffled deck
		self.playing_deck_list=[] #shuffled deck

		#will be two until coded otherwise
		self.next_player_num = 0
		self.players=[]
		self.stack_in_play=[]
		self.current_suit = None 
		self.last_hand_winner = None 
		

		#create cards and append to deck
		for suit in Deck.SUIT_TUPLE:
			for value, rank in rank_value_dict.items():
				o_card = Card(suit,rank,value)
				self.starting_deck_list.append(o_card)

		
		self.shuffle()

	def shuffle(self):
		self.playing_deck_list = self.starting_deck_list.copy()
		random.shuffle(self.playing_deck_list)
		random.shuffle(self.playing_deck_list)
		random.shuffle(self.playing_deck_list)


	def add_player(self):
		self.next_player_num +=1
		player_name = f"Player_{self.next_player_num}"
		igrac = Player(player_name)
		self.players.append(igrac)
		

	def deal_cards(self, num_cards):
		for player in self.players:
			
			for i in range(num_cards):
				card = self.playing_deck_list.pop()
				player.hand.append(card)

		#return player.hand
	
	def add_to_stack(self,card):
		self.stack_in_play.append(card)

	def determine_winner(self):
		
		winning_tuple = max(self.stack_in_play, key=lambda item: item[1].get_value())
		winning_player, winning_card = winning_tuple
		self.last_hand_winner = winning_player

		winning_player.stack.extend(card for _, card in self.stack_in_play)
		print(f"{winning_player.get_name()} wins the round and collects these cards: {[card.get_name() for _, card in self.stack_in_play]}")

		self.stack_in_play.clear()
		self.current_suit=None

	# Deal cards to winner first
		self.deal_one_card(winning_player)
		for player in self.players:
			if player != winning_player:
				self.deal_one_card(player)

		return self.players.index(winning_player) if winning_player else 0
	
	def deal_one_card(self, player):
		if self.playing_deck_list:
			card = self.playing_deck_list.pop()
			player.hand.append(card)
			print(f"{player.get_name()} received {card.get_name()}.")


