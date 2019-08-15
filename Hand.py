import sys
from Deck import Deck
from Player import Player
from Table import Table
from comparehands import compare

class Hand:

	def __init__(self, players, button, sb, rollover):
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
			self.pot = rollover
			self.small = self.playersleft[1]
			self.big = self.playersleft[2 % self.n]
			self.sb = sb

	#deal to players, where players is a list of players
	def dealplayers(self):
		if self.n > 1:
			
			#test formatting 
			print

			for i in range(self.n):
				self.playersleft[i].hand = [self.deck.cards[i*2 + 5], self.deck.cards[i*2 + 6]]

				#testing
				print(self.playersleft[i].name + ": \t" + ''.join(self.playersleft[i].hand))

	def post(self):
		if self.big.chips >= self.sb * 2: 
			self.big.chips -= self.sb * 2
			self.pot += self.sb * 2
		if self.small.chips >= self.sb:
			self.small.chips -= self.sb
			self.pot += self.sb

		#testing
		print("\n" + self.playersleft[0].name + " is button \t% d" %(self.playersleft[0].chips))
		print(self.small.name + " posts sb \t% d" %(self.small.chips))
		print(self.big.name + " posts bb \t% d" %(self.big.chips))
				
	def dealflop(self):
		self.board[0] = self.deck.cards[0]
		self.board[1] = self.deck.cards[1]
		self.board[2] = self.deck.cards[2]

	def dealturn(self):
		self.board[3] = self.deck.cards[3]
		
	def dealriver(self):
		self.board[4] = self.deck.cards[4]

	#def endhand(self, winner):
		#winner.chips += self.pot
		#cover split case and side pot

	# deals with showdown -- returns rollover in pot
	#use only when river is already dealt (if self.board[4])
	def showdown(self):
		
		rollover = 0
		
		winners = compare(self.board, self.playersleft[0], self.playersleft[1])
		for i in range(self.n - 2):
			temp = compare(self.board, winners[0], self.playersleft[i + 2])
			if len(temp) == 2:
				winners.append(self.playersleft[i + 2])
			else: winners = temp

		prize = self.pot / len(winners)
		rollover = self.pot % len(winners)
		for player in winners:
			player.chips += prize
			#testing 
			print player.name
		return rollover


def main():
	p1 = Player("Hero")
	p2 = Player("Villain")
   	table = Table()
   	table.sit(p1, 0)
   	table.sit(p2, 1)
   	hand1 = Hand(table.players, 0, 1)
   	prompt = raw_input("Start? (Y/N) ")
   	if prompt == "y": 
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