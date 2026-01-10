from agent.loader import load_food_data, log_meals
from agent.reasoner import suggest_protein_additions
from agent.observer import calculate_total_protein_intake

def main():
    print("Welcome to the Personal Wellness Agent!")
    
    # 1. Load the food database
    # food_info now contains the full dictionary for each item
    food_category, food_info = load_food_data()

    # 2. Log meals
    # log_meals returns (raw_text_dict, parsed_food_list_dict)
    _, food_list = log_meals() 

    # 3. Flatten the meal log
    # This prevents 'breakfast' from being treated as a food
    flat_meal_log = {}
    for meal_name, items in food_list.items():
        for food, qty in items:
            # Sum quantities if same food is eaten in different meals
            flat_meal_log[food] = flat_meal_log.get(food, 0) + qty
    
    # 4. Calculate total protein
    total_protein = calculate_total_protein_intake(food_info, flat_meal_log)

    print(f"\nTotal Protein Intake: {total_protein}g")

    # 5. Provide suggestions if goal isn't met (e.g., goal of 50g)
    if total_protein < 80:
        print(f"You are {50 - total_protein}g short of your 50g goal.")
        suggest_protein_additions(food_info)
    else:
        print("Great job! You've hit your protein target for the day.")

if __name__ == "__main__":
    main()