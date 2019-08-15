from gethand import evaluate
from Player import Player 
import sys 

#compare two hands on given board and return winner(s) as a list

def compare(board, p1, p2):
	cards1 = board + p1.hand
	cards2 = board + p2.hand

	hand1 = evaluate(cards1)
	hand2 = evaluate(cards2)

	if hand1[0] > hand2[0]: 
		return [p1]
	if hand2[0] > hand1[0]:
		return [p2]

	if hand1 == hand2:
		return [p1, p2]

	#if index is same and not a split
	if hand1[1] > hand2[1]: return [p1]
	else: return [p2]

def main():
    
    board = ['6s', '2s', '2d', '2c', '6d']
    hero = Player("Hero")
    villain = Player("Vill")
    hero.hand = ["Jh", "Ac"]
    villain.hand = ["7s", "Jd"]
    print compare(board, hero, villain)

if __name__ == '__main__':
    sys.exit(main())