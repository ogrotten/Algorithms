#!/usr/bin/python

import argparse


def find_max_profit(prices):
	"""
	get 'origin' number from array.
	check it against the rest of the numbers in the array `comparison'
	store the result of the check (comparison - origin)
	return the greatest difference.
	"""
	plen = len(prices)-1
	count = 0
	best = 0

	for i in range(plen):
		comparison = None
		origin = prices[i]
		for j in range(plen - i):
			# print(19, i,j)
			loc = plen-(plen-j-1)

			if loc > plen:
				break

			comparison = prices[i+loc]

			if comparison - origin > best:
				best = comparison - origin

			print(22, origin, comparison)

	print(best)

find_max_profit([1050, 270, 1540, 3800, 2])


# if __name__ == "__main__":
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(description="Find max profit from prices.")
#     parser.add_argument(
#         "integers", metavar="N", type=int, nargs="+", help="an integer price"
#     )
#     args = parser.parse_args()

#     print(
#         "A profit of ${profit} can be made from the stock prices {prices}.".format(
#             profit=find_max_profit(args.integers), prices=args.integers
#         )
#     )
