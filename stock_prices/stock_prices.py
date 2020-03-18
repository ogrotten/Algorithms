#!/usr/bin/python

import argparse


def find_max_profit(prices):
	"""
	get 'origin' number from array.
	check it against the rest of the numbers in the array `comparison'
	store the result of the check (comparison - origin)
	return the greatest difference.
	"""
	pricelength = len(prices) - 1
	count = 0
	best = float("-inf")

	for i in range(pricelength):
		comparison = None
		origin = prices[i]
		for j in range(pricelength - i):
			# print(19, i,j)
			loc = pricelength - (pricelength - j - 1)

			if loc > pricelength:
				break

			comparison = prices[i + loc]

			# print(22, origin, comparison)
			if comparison - origin > best:
				best = comparison - origin
				# print(best)

	# print(best)
	return best


# find_max_profit([1050, 270, 1540, 3800, 2])
# find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])

if __name__ == "__main__":
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description="Find max profit from prices.")
	parser.add_argument(
		"integers", metavar="N", type=int, nargs="+", help="an integer price"
	)
	args = parser.parse_args()

	print(
		"A profit of ${profit} can be made from the stock prices {prices}.".format(
			profit=find_max_profit(args.integers), prices=args.integers
		)
	)

