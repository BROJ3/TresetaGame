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
	
	def get_bella_value(self):
		if self.number == "Ace":
			return 1
		elif self.number in ("King", "Caval", "Fanat", "2", "3"):
			return 1/3
		else:
			return 0
