def get_recipe_price(prices, optionals=None, **ingredients):
    recipe_price = 0
    if optionals is None:
        optionals = []

    for ingredient, amount in ingredients.items():
        if ingredient not in optionals:
            recipe_price += (amount/100) * prices[ingredient]
    return recipe_price


def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))


if __name__ == '__main__':
    main()