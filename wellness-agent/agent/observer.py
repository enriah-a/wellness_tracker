# TODO: This is a placeholder. In a real agent, observer would monitor external data (e.g., files, APIs).
# For now, we'll simulate observing logged meals (passed from main.py or elsewhere).

def calculate_total_protein_intake(food_info, flat_meal_log):
    total_protein = 0
    for meal_item, meal_qty in flat_meal_log.items():
        if meal_item in food_info:
            # Access the nested protein value
            protein_value = food_info[meal_item]["protein"] 
            total_protein += (meal_qty * protein_value)
    return total_protein