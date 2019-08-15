import sys
from Player import Player
from Table import Table
from Hand import Hand

class Game:

	def __init__(self, table, sb):
		self.hand_no = 0
		self.table = table
		self.players = []
		self.button = 0 
		self.sb = sb

	#check how many players have enough chips to play and updates players in game
	#returns number of players with chips remaining
	def update(self):
		n = 0
		self.players = self.table.players[:]
		for i in range(len(self.players)):
			if self.players[i].chips == 0:
				self.players[i] = None
			else: n += 1
		return n

	#begin the game
	def start(self):
		rollover = 0
		#if there are enough players with chips keep running hands
		while self.update() > 1:

			self.hand_no += 1
			print("\nHand %d" %(self.hand_no))
			# in the beginning button is lowest indexed player to have enough chips
			if self.hand_no == 1:
				for i in range(len(self.players)):
					if self.players[i].chips > 0:
						self.button = i
						break
			else:
				#consider patching when bb and/or sb leaves, but for now just move once
				for i in range(len(self.players)):
					self.button += 1
					if self.players[(self.button) % len(self.players)].chips > 0:
						self.button = (self.button) % len(self.players)
						break

			hand = Hand(self.players, self.button, self.sb, rollover)
			rollover = 0
			hand.dealplayers()
			hand.post()
			
			#testing
			print("Pot:% d" %(hand.pot))

			hand.dealflop()
	   		hand.dealturn()
	   		hand.dealriver()
	   		print 
	   		print hand.board
	   		print 
	   		print("Winners: ")
	   		rollover = hand.showdown()

			#testing
			prompt = raw_input("\n" + "Next hand? (Y/N) ")
   			if prompt == "y": 
   				continue
   			else: break




def main():
	p1 = Player("Hero")
	p2 = Player("Vill")
	p3 = Player("Fish")
   	table = Table()
   	table.sit(p1, 0)
   	table.sit(p2, 1)

   	game = Game(table, 1)
   	
	table.sit(p3, 2)
	p1.getchips(200)
   	p2.getchips(200)
   	p3.getchips(200)
   	prompt = raw_input("Start? (Y/N) ")
   	if prompt == "y": 
   		game.start()
   	
	#print game.table.players[1].hand
	

if __name__ == '__main__':
	sys.exit(main())