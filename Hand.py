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
			deck = Deck()
			deck.shuffle()
			self.deck = deck
			self.board = [""] * 5
			self.pot = rollover
			self.sb = sb
			self.bet = 0

	#deal to players, where players is a list of players
	def dealplayers(self):
		if len(self.playersleft) > 1:
			
			#test formatting 
			print

			for i in range(len(self.playersleft)):
				self.playersleft[i].hand = [self.deck.cards[i*2 + 5], self.deck.cards[i*2 + 6]]

				#testing
				print(self.playersleft[i].name + ": \t" + ''.join(self.playersleft[i].hand))

	#need to add case in which player doesn't have enough for a bb
	def post(self):
		#post big
		if self.playersleft[2 % len(self.playersleft)].chips >= self.sb * 2: 
			self.playersleft[2 % len(self.playersleft)].chips -= self.sb * 2
			self.pot += self.sb * 2
		#post small
		if self.playersleft[1].chips >= self.sb:
			self.playersleft[1].chips -= self.sb
			self.pot += self.sb

		#testing
		print("\n" + self.playersleft[0].name + " is button \t% d" %(self.playersleft[0].chips))
		print(self.playersleft[1].name + " posts sb \t% d" %(self.playersleft[1].chips))
		print(self.playersleft[2 % len(self.playersleft)].name + " posts bb \t% d" %(self.playersleft[2 % len(self.playersleft)].chips))
				
	def dealflop(self):
		self.board[0] = self.deck.cards[0]
		self.board[1] = self.deck.cards[1]
		self.board[2] = self.deck.cards[2]

	def dealturn(self):
		self.board[3] = self.deck.cards[3]
		
	def dealriver(self):
		self.board[4] = self.deck.cards[4]

	def preflop_action(self):
		pass
		

	def postflop_action(self):
		self.bet = 0
		for player in self.playersleft:
			player.invested = 0
		pass
	
	#def endhand(self, winner):
		#winner.chips += self.pot
		#cover split case and side pot

	# deals with showdown -- returns rollover in pot
	#use only when river is already dealt (if self.board[4])
	def showdown(self):
		
		rollover = 0
		
		winners = compare(self.board, self.playersleft[0], self.playersleft[1])
		for i in range(len(self.playersleft) - 2):
			temp = compare(self.board, winners[0], self.playersleft[i + 2])
			if len(temp) == 2:
				winners.append(self.playersleft[i + 2])

		prize = self.pot / len(winners)
		rollover = self.pot % len(winners)
		for player in winners:
			player.chips += prize
			#testing 
			print(player.name)
		return rollover


def main():
	p1 = Player("Hero")
	p2 = Player("Vill")
	p3 = Player("Fish")
	p1.getchips(20)
	p2.getchips(20)
	p3.getchips(20)
	table = Table()
	table.sit(p1, 0)
	table.sit(p2, 1)
	table.sit(p3, 2)
	hand = Hand(table.players, 0, 1, 0) 
	hand.post()
	hand.board = ['Qh', '3h', 'Tc', '9c', 'Qc']
	p1.hand = ['6h', '9s']
	p2.hand = ['8d', '9d']
	p3.hand = ['5s', 'Ac']
	hand.showdown()
	   	
if __name__ == '__main__':
	sys.exit(main())