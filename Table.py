import sys
from Player import Player

class Table:

	def __init__(self):
		self.seats = 3
		self.players = [None] * self.seats
		self.nplayers = 0

	def sit(self, player, seat):
		if seat < self.seats and self.nplayers < self.seats and self.players[seat] == None:
			self.players[seat] = player
			player.seat = seat
			self.nplayers += 1
		#else: raise error

	def leave(self, player):
		if self.nplayers > 0 and self.players[player.seat] == player:
			self.players[player.seat] = None
			self.nplayers -= 1
		#else: raise error

def main():
	p1 = Player("Hero")
	p2 = Player("Villain")
	p3 = Player("Villain")
   	table = Table()
   	table.sit(p1, 0)
   	table.sit(p2, 1)
   	table.sit(p3, 2)
   	print table.nplayers
   	
if __name__ == '__main__':
	sys.exit(main())