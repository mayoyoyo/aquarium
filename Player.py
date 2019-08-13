import sys

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = ["", ""]
		self.value = 0 

def main():
   	p1 = Player("Hero")
   	print p1.hand

if __name__ == '__main__':
	sys.exit(main())