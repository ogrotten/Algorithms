#!/usr/bin/python

import math

"""
Compare ingredients by name
find batch count using // 
Return the minimum amount

set the minimum based on the loop, 
IF a 0 is discovered THEN break
ELSE compare minimum to the "next key"
IF new-minimum < current minimum THEN set new minimum
"""

def recipe_batches(recipe, ingredients):
	batches = float("inf")
	if len(ingredients) < len(recipe):
		return 0

	for key in recipe:
		recipeamt = recipe[key]
		ingamt = ingredients[key]
		
		potential = ingamt // recipeamt
		if potential <= 0:
			return 0
		if potential < batches:
			batches = potential
	print(batches)
		


# one for loop with if
# if you don't try catch it'll key error

recipe_batches(
	{"milk": 2, "sugar": 40, "butter": 20},
	{"milk": 5, "sugar": 120, "butter": 500},
)


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

