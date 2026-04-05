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
        total_c = 0 # Track calories
        breakdown = []
        
        for item in raw_inputs:
            key, qty = self.interpret(item)
            if key:
                stats = self.food_info[key]
                p = stats["protein"] * qty
                c = stats.get("calories", 0) * qty # Get calories
                total_p += p
                total_c += c
                
                breakdown.append({
                    "Item": key.replace('_', ' ').title(),
                    "Protein": p,
                    "Calories": c
                })
        return {"protein": total_p, "calories": total_c, "breakdown": breakdown}
