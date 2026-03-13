import json, os

class FoodDatabase:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_path = os.path.join(base_dir, "..", "data", "food_protein.json")
        
        # Initialize the storage dictionaries first
        self.food_info = {}
        self.food_category = {}
        
        # 1. Load the raw nested data into a temporary variable
        raw_data = self.load_data()
        
        # 2. Flatten that temporary variable into our permanent dictionaries
        self._flatten_data(raw_data)

    def load_data(self):
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Could not find JSON at: {self.json_path}")
            
        with open(self.json_path, 'r') as f:
            return json.load(f)

    def _flatten_data(self, data):
        # We loop through the 'raw_data' passed in
        for category, foods in data.items():
            for food_name, nutrients in foods.items():
                # Save the category for reference
                self.food_category[food_name] = category
                # Save the flat food info (protein, iron, etc.)
                self.food_info[food_name] = nutrients

    def get_info(self, food_key):
        # Case-insensitive lookup
        return self.food_info.get(food_key.lower())

    def get_all_keys(self):
        return list(self.food_info.keys())