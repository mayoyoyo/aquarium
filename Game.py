import sys
from Deck import Deck
from Player import Player
from Table import Table
from Hand import Hand
from comparehands import compare

class Game:

	def __init__(self, table):
		self.hand_no = 0
		self.table = table
		self.players = []
		self.button = 0

	#check how many players have enough chips to play
	def update(self):
		n = 0
		self.players = self.table.players[:]
		for i in range(len(self.players)):
			if self.players[i].chips == 0:
				self.players[i] = None
			else: n += 1
		return n


	def start(self):
		#if there are enough players with chips
		if self.update() > 1:
			self.hand_no += 1
			hand = Hand(self.players, self.button)




def main():
	p1 = Player("Hero")
	p2 = Player("Villain")
	p3 = Player("button")
   	table = Table()
   	table.sit(p1, 0)
   	table.sit(p2, 1)

   	game = Game(table)
   	
	table.sit(p3, 2)
	p1.getchips(20)
   	p2.getchips(20)
   	game.start()
   	
	#print game.table.players[1].hand
	

if __name__ == '__main__':
	sys.exit(main())