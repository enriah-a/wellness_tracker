
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