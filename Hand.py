import sys
from Deck import Deck
from Player import Player
from Table import Table
from comparehands import compare

class Hand:

	def __init__(self, players, button):
		if players[button]:
			self.playersleft = [] #players in hand starting from button at index 0
			for i in range(len(players)):
				if players[(button + i) % len(players)]:
					self.playersleft.append(players[(button + i) % len(players)])
			self.n = len(self.playersleft)
			deck = Deck()
			deck.shuffle()
			self.deck = deck
			self.board = [""] * 5
			self.pot = 0

	#deal to players, where players is a list of players
	def dealplayers(self):
		if self.n > 1:
			for i in range(self.n):
				self.playersleft[i].hand = [self.deck.cards[i*2 + 5], self.deck.cards[i*2 + 6]]
				
	def dealflop(self):
		self.board[0] = self.deck.cards[0]
		self.board[1] = self.deck.cards[1]
		self.board[2] = self.deck.cards[2]

	def dealturn(self):
		self.board[3] = self.deck.cards[3]
		
	def dealriver(self):
		self.board[4] = self.deck.cards[4]

def main():
	p1 = Player("Hero")
	p2 = Player("Villain")
	p3 = Player("button")
   	table = Table()
   	table.sit(p1, 0)
   	table.sit(p2, 1)
   	hand1 = Hand(table.players, 0)
   	hand1.dealplayers()
   	hand1.dealflop()
   	hand1.dealturn()
   	hand1.dealriver()
   	print hand1.board
   	print hand1.playersleft[0].hand
   	print hand1.playersleft[1].hand
   	print compare(hand1.board, hand1.playersleft[0].hand, hand1.playersleft[1].hand)
   	
if __name__ == '__main__':
	sys.exit(main())