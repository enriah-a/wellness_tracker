import json
# New code to provide a consistent API for loading food data instead of loading a heavy json each time
class FoodDatabase:
    def __init__(self, file_path='wellness-agent/data/food_protein.json'):
        with open(file_path, 'r') as f:
            self.raw_data = json.load(f)
        self.food_info = {}
        self.food_category = {}
        self._flatten_data()

    def _flatten_data(self):
        for category, foods in self.raw_data.items():
            for food, info in foods.items():
                self.food_category[food] = category
                self.food_info[food] = info

    def get_info(self, food_key):
        return self.food_info.get(food_key.lower())

    def get_all_keys(self):
        return list(self.food_info.keys())
