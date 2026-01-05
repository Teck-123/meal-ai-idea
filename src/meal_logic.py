import json
import random
import os

class MealGenerator:
    def __init__(self):
        self.meals = self._load_meals()
    
    def _load_meals(self):
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'meals.json')
        with open(data_path, 'r') as f:
            return json.load(f)
    
    def get_meal_suggestion(self, meal_type, time_available, dietary_preference):
        time_key = self._map_time(time_available)
        diet_key = self._map_diet(dietary_preference)
        
        try:
            meal_options = self.meals[meal_type][time_key][diet_key]
            return random.choice(meal_options)
        except KeyError:
            return "Sorry, no meal found for your preferences. Try different options."
    
    def _map_time(self, time):
        if time == 1:
            return "quick"
        elif time == 2:
            return "medium"
        else:
            return "long"
    
    def _map_diet(self, diet):
        if diet == 1:
            return "vegetarian"
        elif diet == 2:
            return "vegan"
        else:
            return "no_restrictions"