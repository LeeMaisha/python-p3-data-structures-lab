spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(foods):
    """Return a list of names from the spicy_foods list."""
    return [food["name"] for food in foods]


def get_spiciest_foods(foods):
    """Return foods with heat_level greater than 5."""
    return [food for food in foods if food["heat_level"] > 5]


def print_spicy_foods(foods):
    """Print each food in format: Name (Cuisine) | Heat Level: 🌶*heat_level."""
    for food in foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(foods, cuisine):
    """Return the food dictionary matching the given cuisine."""
    for food in foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(foods):
    """Print only foods with heat_level greater than 5."""
    spiciest = get_spiciest_foods(foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(foods):
    total = sum(food["heat_level"] for food in foods)
    return total // len(foods)



def create_spicy_food(foods, new_food):
    """Return list with new_food added."""
    foods.append(new_food)
    return foods