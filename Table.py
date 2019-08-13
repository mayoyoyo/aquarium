import sys
from Deck import Deck
from Player import Player
from comparehands import compare

class Table:

	def __init__(self):
		self.players = []
		self.board = [""] * 5

	def add(self, player):
		self.players.append(player)

	def newhand(self):
		deck = Deck()
		deck.shuffle()
		self.dealplayers(deck)
		self.dealflop(deck)
		self.dealturn(deck)
		self.dealriver(deck)

	#deal to players, where players is a list of players
	def dealplayers(self, deck):
		n = len(self.players)
		if n < 2:
			return None
		
		for i in range(n):
			self.players[i].hand = [deck.cards[i*2 + 5], deck.cards[i*2 + 6]]
			
	def dealflop(self, deck):
		self.board[0] = deck.cards[0]
		self.board[1] = deck.cards[1]
		self.board[2] = deck.cards[2]

	def dealturn(self, deck):
		self.board[3] = deck.cards[3]
		
	def dealriver(self, deck):
		self.board[4] = deck.cards[4]

def main():
	p1 = Player("Hero")
	p2 = Player("Villain")
   	table = Table()
   	table.add(p1)
   	table.add(p2)
   	table.newhand()
   	print table.board
   	print table.players[0].hand
   	print table.players[1].hand
   	print compare(table.board, table.players[0].hand, table.players[1].hand)

if __name__ == '__main__':
	sys.exit(main())