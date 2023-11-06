import random
from card import Card

class Deck():
	#defining numbers an suits of the deck
	SUIT_TUPLE = ('Kupe','Bate','Spade','Dinari')
	STANDARD_DICT = {
		'Ace':8,
		'2':9,
		'3':10,
		'4':1,
		'5':2,
		'6':3,
		'7':4,
		'Fanat':5,
		'Caval':6,
		'King':7}


	#we want the deck to
	#- make all cards	-DONE
	# shuffle itself	-DONE
	def __init__(self,rank_value_dict=STANDARD_DICT):
		#pre-shuffled deck
		self.starting_deck_list=[]
		#shuffled deck
		self.playing_deck_list=[]
		#will be two until coded otherwise
		self.next_player_num = 0
		self.players=[]

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

	def add_player(self,name):
		self.next_player_num +=1
		player_name = f"Player {self.next_player_num}"
		self.players.append(player_name)
		


	def deal_cards(self, num_cards=10):
		hands = {}
		for player in self.players:
			hand = []
			for i in range(num_cards):
				card = self.playing_deck_list.pop()
				hand.append(card)
			hands[player] = hand
		return hands
