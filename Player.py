import sys

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = ["", ""]
		self.chips = 0 
		self.buyin = 0
		self.seat = None

	def getchips(self, chips):
		self.chips += chips
		self.buyin += chips

	def profit(self):
		return self.chips - self.buyin

def main():
   	p1 = Player("Hero")
   	print p1.hand

if __name__ == '__main__':
	sys.exit(main())