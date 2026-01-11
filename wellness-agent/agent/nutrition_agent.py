# agent/nutrition_agent.py

from rapidfuzz import process

class NutritionAgent:
    def __init__(self, food_info):
        self.food_info = food_info
        self.keys = list(food_info.keys())

    def interpret(self, raw_text):
        if not raw_text.strip(): return None, 0
        parts = raw_text.strip().split(' ')
        qty = int(parts[0]) if parts[0].isdigit() else 1
        query = "_".join(parts[1:] if parts[0].isdigit() else parts).lower()
        match = process.extractOne(query, self.keys, score_cutoff=70)
        return (match[0], qty) if match else (None, qty)

    def observe_intake(self, raw_inputs):
        total_p = 0
        breakdown = []
        missing = []  # <--- Initialize this list

        for item in raw_inputs:
            key, qty = self.interpret(item)
            if key:
                p = self.food_info[key]["protein"] * qty
                total_p += p
                breakdown.append({
                    "Item": key.replace('_', ' ').title(),
                    "Protein": p
                })
            else:
                missing.append(item) # <--- Add unmatched items here
        
        # Ensure you are returning all THREE values here:
        return total_p, breakdown, missing