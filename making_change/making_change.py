#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]


def making_change(amount, coins):
	cache = [1] + ([0] * (amount))
	# print(11, cache)
	for eachcoin in coins:
		for i in range(eachcoin, amount + 1):
			cache[i] = cache[i] + cache[i - eachcoin]
			# print(i, cache[i], end=", ")
		# print("\n", 16, cache, "\n\n")
	return cache[amount]

# print(making_change(14, denominations))

if __name__ == "__main__":
	# Test our your implementation from the command line
	# with `python making_change.py [amount]` with different amounts
	if len(sys.argv) > 1:
		denominations = [1, 5, 10, 25, 50]
		amount = int(sys.argv[1])
		print(
			"There are {ways} ways to make {amount} cents.".format(
				ways=making_change(amount, denominations), amount=amount
			)
		)
	else:
		print("Usage: making_change.py [amount]")
