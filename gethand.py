# returns the hand and its valuation based on an input of a list of 7 cards
# high: 0, p: 1, 2p: 2, 3x: 3, str: 4, fl: 5, fh: 6, q: 7, strfl: 8, rf: 9

import sys

def evaluate(cards):

	res = check_flush(cards)
	if res:
		#check for royal flush
		if res[-5:] == [10, 11, 12, 13, 14]:
				return [9, [14, 13, 12, 11, 10]]

		#check for straight flush
		res.reverse()
		for i in range(len(res) - 4):
			if res[i] - res[i+4] == 4:
				res = res[i:i+5]
				return [8, res]
		if res[-4:] == [5, 4, 3, 2] and res[0] == 14:
			res = [5, 4, 3, 2, 14]
			return [8, res]

		#if flush, no quads/fh can exist
		return [5, res[:5]]

	res = check_quads(cards)
	if res:
		return [7, res]

	res = check_fh(cards)
	if res:
		return [6, res]
	
	res = check_str(cards)
	if res:
		return [4, res]

	res = check_3x(cards)
	if res:
		return [3, res]

	res = check_2p(cards)
	if res:
		return [2, res]

	res = check_p(cards)
	if res:
		return [1, res]

	#return high hand
	for n in range(len(cards)):
		if cards[n][0] == "A": cards[n] = 14
		elif cards[n][0] == "K": cards[n] = 13
		elif cards[n][0] == "Q": cards[n] = 12
		elif cards[n][0] == "J": cards[n] = 11
		elif cards[n][0] == "T": cards[n] = 10
		else: cards[n] = int(cards[n][0])
	return [0, sorted(cards, reverse=True)[:-2]]

def check_flush(cards):
	# h, d, c, s
	count = [""] * 4
	for c in cards:
		if c[1] == "h": count[0] += c[0]
		if c[1] == "d": count[1] += c[0]
		if c[1] == "c": count[2] += c[0]
		if c[1] == "s": count[3] += c[0]

	for i in count:
		if len(i) >= 5:
			i = list(i)
			for n in range(len(i)):
				if i[n] == "A": i[n] = 14
				elif i[n] == "K": i[n] = 13
				elif i[n] == "Q": i[n] = 12
				elif i[n] == "J": i[n] = 11
				elif i[n] == "T": i[n] = 10
				else: i[n] = int(i[n])
			i.sort()
			return i

def check_quads(cards):
	clone = cards[:]
	count = [0] * 13
	a = set()
	for n in range(len(clone)):
		if clone[n][0] == "A": clone[n] = 14
		elif clone[n][0] == "K": clone[n] = 13
		elif clone[n][0] == "Q": clone[n] = 12
		elif clone[n][0] == "J": clone[n] = 11
		elif clone[n][0] == "T": clone[n] = 10
		else: clone[n] = int(clone[n][0])

	for c in clone:
		count[c-2] += 1
		if count[c-2] == 4:
			a = set(clone)
			a.remove(c)
			high = max(a)
			return [c, c, c, c, high] 

def check_fh(cards):
	clone = cards[:]
	count = [0] * 13
	pairs = []
	trips = []
	pair = 0
	trip = 0
	a= set()
	for n in range(len(clone)):
		if clone[n][0] == "A": clone[n] = 14
		elif clone[n][0] == "K": clone[n] = 13
		elif clone[n][0] == "Q": clone[n] = 12
		elif clone[n][0] == "J": clone[n] = 11
		elif clone[n][0] == "T": clone[n] = 10
		else: clone[n] = int(clone[n][0])

	for c in clone:
		count[c-2] += 1
		if count[c-2] == 2:
			pairs.append(c)
		elif count[c-2] == 3:
			trips.append(c)

	if trips:
		if len(pairs) > 1:
			trip = max(trips)
			pairs.remove(trip)
			pair = max(pairs)
			return [trip, trip, trip, pair, pair]

def check_str(cards):
	vals = [c[0] for c in cards]
	for n in range(7):
		if vals[n] == "A": vals[n] = 14
		elif vals[n] == "K": vals[n] = 13
		elif vals[n] == "Q": vals[n] = 12
		elif vals[n] == "J": vals[n] = 11
		elif vals[n] == "T": vals[n] = 10
		else: vals[n] = int(vals[n])
	vals = sorted(list(dict.fromkeys(vals)), reverse=True)

	if len(vals) < 5: return None
	for i in range(len(vals) - 4):
		if vals[i] - vals[i+4] == 4:
			vals = vals[i:i+5]
			return vals
	if vals[-4:] == [5, 4, 3, 2] and vals[0] == 14:
		return [5, 4, 3, 2, 14]

def check_3x(cards):
	clone = cards[:]
	count = [0] * 13
	a = set()
	for n in range(len(clone)):
		if clone[n][0] == "A": clone[n] = 14
		elif clone[n][0] == "K": clone[n] = 13
		elif clone[n][0] == "Q": clone[n] = 12
		elif clone[n][0] == "J": clone[n] = 11
		elif clone[n][0] == "T": clone[n] = 10
		else: clone[n] = int(clone[n][0])

	for c in clone:
		count[c-2] += 1
		if count[c-2] == 3:
			a = set(clone)
			a.remove(c)
			high1 = max(a)
			a.remove(high1)
			high2 = max(a)
			return [c, c, c, high1, high2]

def check_2p(cards):
	clone = cards[:]
	count = [0] * 13
	pairs = []
	a= set()
	for n in range(len(clone)):
		if clone[n][0] == "A": clone[n] = 14
		elif clone[n][0] == "K": clone[n] = 13
		elif clone[n][0] == "Q": clone[n] = 12
		elif clone[n][0] == "J": clone[n] = 11
		elif clone[n][0] == "T": clone[n] = 10
		else: clone[n] = int(clone[n][0])

	for c in clone:
		count[c-2] += 1
		if count[c-2] == 2:
			pairs.append(c)

	if len(pairs) > 1:
		pairs.sort()
		a = set(clone)
		a.remove(pairs[-1])
		a.remove(pairs[-2])
		return [pairs[-1], pairs[-1], pairs[-2], pairs[-2], max(a)]

def check_p(cards):
	clone = cards[:]
	count = [0] * 13
	for n in range(len(clone)):
		if clone[n][0] == "A": clone[n] = 14
		elif clone[n][0] == "K": clone[n] = 13
		elif clone[n][0] == "Q": clone[n] = 12
		elif clone[n][0] == "J": clone[n] = 11
		elif clone[n][0] == "T": clone[n] = 10
		else: clone[n] = int(clone[n][0])

	for c in clone:
		count[c-2] += 1
		if count[c-2] == 2:
			clone.remove(c)
			clone.sort()
			return [c, c, clone[-2], clone[-3], clone[-4]]

def main():
    
    a = ["2s", "8s", "2d", "4c", "5s", "3d", "7s"]
    print evaluate(a)

if __name__ == '__main__':
    sys.exit(main())