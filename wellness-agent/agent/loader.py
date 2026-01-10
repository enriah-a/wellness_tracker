import json

# Load the JSON data from the file
with open('wellness-agent/data/food_protein.json', 'r') as f:
    data = json.load(f)

def load_food_data():
    #Initialize dicts: food_category maps food to category, food_protein maps food to protein value"""
    food_category = {}
    food_protein = {}

    for category, foods in data.items():
        for food, protein in foods.items():
            food_category[food] = category
            food_protein[food] = protein

    return food_category, food_protein


def log_meals():
    """Prompt user to log meals for breakfast, lunch, and dinner."""
    meals = {}       # store raw meal text if needed
    food_list = {}   # store parsed (food, qty) tuples
    
    for meal_name in ['breakfast', 'lunch', 'dinner']:
        meal = input(f"Enter your {meal_name} (e.g., '2 idli + sambar'): ")
        meals[meal_name] = meal.lower()  # keep raw input
        food_list[meal_name] = parse_meal(meal)  # parse into tuples eg breakfast: idli,2 / greek_yoghurt,1

     # Display logged meals
    print("\nYou have logged the following meals:")
    for meal_name, items in food_list.items():
        print(f"{meal_name.capitalize()}: {items}")

    return meals, food_list

def parse_meal(meal_text):
    # Split by '+' to get individual food items
    items = meal_text.split('+')
    meal_items = []
    
    for item in items:
        item = item.strip()
        parts = item.split(' ')
        
        # Check if the first word is a number (the quantity)
        if parts[0].isdigit():
            qty = int(parts[0])
            # Join the remaining words with underscores (e.g., "greek yoghurt" -> "greek_yoghurt")
            food = "_".join(parts[1:]).strip()
        else:
            # No number provided, assume quantity is 1
            qty = 1
            # Join all words with underscores
            food = "_".join(parts).strip()
            
        meal_items.append((food, qty))
    return meal_items
