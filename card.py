#the card class
#has number, suit, point value
#and strength? - do I code that in main?

class Card():
	def __init__(self,suit,value,number):
		self.suit = suit
		self. number = number
		self.card_name =  str(number) + ' of ' + str(suit)
		self.value = value

	def get_name(self):
		return self.card_name

	def get_number(self):
		return self.number

	def get_suit(self):
		return self.suit

	def get_value(self):
		return self.value
	
