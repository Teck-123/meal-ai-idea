from meal_logic import MealGenerator

def get_user_input():
    print(" Daily Meal Idea Generator")
    print("=" * 32)
    
    # Meal type selection
    print("\n1. What type of meal?")
    print("1 - Breakfast")
    print("2 - Lunch") 
    print("3 - Dinner")
    print("4 - Snack")
    
    while True:
        try:
            meal_choice = int(input("Enter choice (1-4): "))
            if 1 <= meal_choice <= 4:
                break
            print("Please enter 1, 2, 3, or 4")
        except ValueError:
            print("Please enter a valid number")
    
    meal_types = ["breakfast", "lunch", "dinner", "snack"]
    meal_type = meal_types[meal_choice - 1]
    
    # Time available
    print("\n2. How much time do you have?")
    print("1 - Less than 10 minutes")
    print("2 - 10-30 minutes")
    print("3 - More than 30 minutes")
    
    while True:
        try:
            time_choice = int(input("Enter choice (1-3): "))
            if 1 <= time_choice <= 3:
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")
    
    # Dietary preference
    print("\n3. Dietary preference?")
    print("1 - Vegetarian")
    print("2 - Vegan")
    print("3 - No restrictions")
    
    while True:
        try:
            diet_choice = int(input("Enter choice (1-3): "))
            if 1 <= diet_choice <= 3:
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")
    
    return meal_type, time_choice, diet_choice

def main():
    generator = MealGenerator()
    
    while True:
        meal_type, time_available, dietary_preference = get_user_input()
        
        suggestion = generator.get_meal_suggestion(meal_type, time_available, dietary_preference)
        
        print("\n" + "=" * 50)
        print("YOUR MEAL SUGGESTION:")
        print("=" * 50)
        print(f"{suggestion}")
        print("=" * 50)
        
        again = input("\nWould you like another suggestion? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for using Meal Generator! 👋")
            break
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()