import sys

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = ["", ""]
		self.chips = 0 
		self.buyin = 0
		self.seat = None
		self.invested = 0

	#probably a good idea to add sit/leave functions
	# that will mirror the same functions in Table.py


	def getchips(self, chips):
		self.chips += chips
		self.buyin += chips

	def profit(self):
		return self.chips - self.buyin


	def call(self, bet):
		if self.chips > bet - self.invested:
			self.chips -= bet - self.invested
			self.invested = bet
		#all in corner case

	def bet(self, bet):
		if self.chips >= bet:
			self.chips -= bet


	#def raise(self, bet):
		
	def fold(self):
		pass

	def check(self):
		pass

def main():
   	p1 = Player("Hero")
   	print(p1.hand)

if __name__ == '__main__':
	sys.exit(main())