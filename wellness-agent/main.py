"""
Main entry point for the Wellness Agent.
Handles user input for meal logging and runs the agent loop.
"""

from agent.loader import load_food_data, log_meals
from agent.observer import calculate_total_protein_intake


def main():
    print("Welcome to the Personal Wellness Agent!")
    # Loading food DB
    food_category, food_protein = load_food_data()
    meal_log = log_meals() #returns foop_list i.e. Breakfast:  <tuples>
    #I want to flatten this for easy parsing, before passing to calculat_protein_intake
    flat_meal_log = {food: qty for meal_items in meal_log.values() for food, qty in meal_items}
    total_protein = calculate_total_protein_intake(food_protein,flat_meal_log)

    print(f"\nYou have eaten {total_protein}g of protein today.")
    # # TODO: Pass observations to reasoner and actor for advice
if __name__ == "__main__":
    main()