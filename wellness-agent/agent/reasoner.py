
from rapidfuzz import process # pip install rapidfuzz
def interpret_item(user_input, db):
    """
    Agentic Skill: Maps '2 big eggs' to ('boiled_egg', 2)
    """
    parts = user_input.strip().split(' ')
    qty = int(parts[0]) if parts[0].isdigit() else 1
    name_query = "_".join(parts[1:] if parts[0].isdigit() else parts).lower()

    # Fuzzy match against database keys
    best_match = process.extractOne(name_query, db.get_all_keys(), score_cutoff=70)
    
    if best_match:
        return best_match[0], qty
    return None, qty

def suggest_protein_additions(food_info):
    choice = input("\nDo you want suggestions to add protein? (yes/no): ").lower().strip()
    
    if choice in ['yes', 'y']:
        suggestions = []
        
        for food_name, info in food_info.items():
            # Now we can access 'meal_type' directly from our dictionary
            if "snack" in info.get("meal_type", []):
                display_name = food_name.replace('_', ' ').title()
                suggestions.append((display_name, info["protein"]))
        
        # Sort and print
        suggestions.sort(key=lambda x: x[1], reverse=True)
        print("\n--- High Protein Snack Suggestions ---")
        for name, prot in suggestions:
            print(f"• {name}: {prot}g protein")