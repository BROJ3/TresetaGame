import random
from player import Player
from card import Card

#let me know if you have questions or something is unclear

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
		self.played_cards=[]

		

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

	def add_player(self, name=None):
		"""Adds a player to the game, allowing for a bot name."""
		if name is None:
			player_name = f"Player_{len(self.players) + 1}"
		else:
			player_name = name  # Use the provided name for the bot

		player = Player(player_name)
		self.players.append(player)
		

	def deal_cards(self, num_cards):
		for player in self.players:
			
			for i in range(num_cards):
				card = self.playing_deck_list.pop()
				player.hand.append(card)

	
	def add_to_stack(self,card):
		self.stack_in_play.append(card)
		self.played_cards.append(card)

	def determine_winner(self):
		"""Determine the winner based on Tressette rules: must follow suit or lose if they don't have it."""
		
		first_player, first_card = self.stack_in_play[0]
		second_player, second_card = self.stack_in_play[1]

		# Check if the second player HAD the required suit BEFORE they played
		had_suit_before_playing = any(card.get_suit() == first_card.get_suit() for card in second_player.hand + [second_card])

		if not had_suit_before_playing:
			# Second player had no matching suit before playing → Auto-lose
			winning_player, winning_card = first_player, first_card
			print(f"{second_player.get_name()} had no {first_card.get_suit()} cards before playing. {first_player.get_name()} wins automatically!")
		else:
			# Both players followed suit, determine winner based on card value
			winning_tuple = max(self.stack_in_play, key=lambda item: item[1].get_value())
			winning_player, winning_card = winning_tuple  # ✅ This will always be assigned

		self.last_hand_winner = winning_player  # Track last hand winner

		# Winner takes the stack
		winning_player.stack.extend(card for _, card in self.stack_in_play)
		print(f"{winning_player.get_name()} wins the round and collects these cards: {[card.get_name() for _, card in self.stack_in_play]}")

		# Reset the playing stack
		self.stack_in_play.clear()
		self.current_suit = None

		# Deal cards for the next round
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


