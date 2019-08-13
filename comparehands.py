from gethand import evaluate
import sys 

#compare two hands on given board and return winner(s) as a list

def compare(board, hole1, hole2):
	cards1 = board + hole1
	cards2 = board + hole2

	hand1 = evaluate(cards1)
	hand2 = evaluate(cards2)

	if hand1[0] > hand2[0]: 
		return [hole1]
	if hand2[0] > hand1[0]:
		return [hole2]

	if hand1 == hand2:
		return [hole1, hole2]

	#if index is same and not a split
	if hand1[1] > hand2[1]: return [hole1]
	else: return [hole2]

def main():
    
    board = ["Kd", "Ks", "Ad", "4c", "7s"]
    hero = ["Kh", "As"]
    villain = ["Ah", "Ac"]
    print compare(board, hero, villain)

if __name__ == '__main__':
    sys.exit(main())