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
        if ingredients[key] // recipe[key] <= 0:
            return 0
        if ingredients[key] // recipe[key] < batches:
            batches = ingredients[key] // recipe[key]
    return batches


# recipe_batches(
# 	{"milk": 2, "sugar": 40, "butter": 20},
# 	{"milk": 5, "sugar": 120, "butter": 500},
# )


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
