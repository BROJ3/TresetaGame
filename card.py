#the card class

class Card():
	def __init__(self,suit,value,number):
		self.suit = suit
		self. number = number
		self.card_name =  number , 'of' , suit
		self.value = value

	def get_name(self):
		return self.card_name
	
	def get_rank(self):
		return self.rank

	def get_value(self):
		return self.value