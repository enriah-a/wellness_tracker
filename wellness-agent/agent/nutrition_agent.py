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
        total_i = 0
        breakdown = []
        missing = []
        
        # Q2 Specific Trackers
        has_meat_or_shake = False
        has_ghee = False

        for item in raw_inputs:
            key, qty = self.interpret(item)
            if key:
                stats = self.food_info[key]
                p = stats["protein"] * qty
                i = stats["iron"] * qty
                total_p += p
                total_i += i
                
                # Check against Q2 Nourishment goals
                if stats.get("category") in ["meat", "supplement"]:
                    has_meat_or_shake = True
                if "ghee" in key:
                    has_ghee = True

                breakdown.append({
                    "Item": key.replace('_', ' ').title(),
                    "Protein": p,
                    "Iron": i
                })
            else:
                missing.append(item)
        
        return {
            "protein": total_p,
            "iron": total_i,
            "breakdown": breakdown,
            "missing": missing,
            "q2_checks": {
                "meat_or_shake": has_meat_or_shake,
                "daily_ghee": has_ghee
            }
        }
