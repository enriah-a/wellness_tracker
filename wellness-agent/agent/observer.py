# TODO: This is a placeholder. In a real agent, observer would monitor external data (e.g., files, APIs).
# For now, we'll simulate observing logged meals (passed from main.py or elsewhere).

def calculate_total_protein_intake(food_protein,flat_meal_log):
    """
    Calculate total protein intake based on observed food intake.
    Food_protein is a dict with food:protein structure
    Flat meal log is a tuple
    """
    total_protein = 0
    for meal_item, meal_qty in flat_meal_log.items():
            if meal_item in food_protein:
                total_protein = total_protein + (meal_qty*food_protein[meal_item])
            else:
                print(f"Warning: {meal_item} not found in food database.")
    return total_protein