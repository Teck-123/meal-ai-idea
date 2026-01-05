# Daily Meal Idea Generator

A simple application that helps users decide what to eat by taking basic inputs and suggesting suitable meal ideas with preparation tips.

## Features

- **Multi-factor decision system**: Considers meal type, available time, and dietary preferences
- **Rule-based logic**: Uses structured decision trees for personalized suggestions
- **Beginner-friendly**: Clean, readable code with no complex algorithms
- **Practical utility**: Addresses the universal daily challenge of meal planning

## How It Works

The application uses a decision tree approach:
1. **Meal Type**: Breakfast, Lunch, Dinner, or Snack
2. **Time Available**: <10 min, 10-30 min, or >30 min
3. **Dietary Preference**: Vegetarian, Vegan, or No restrictions

Based on these inputs, it selects from a curated database of meal suggestions with simple preparation instructions.

## Usage

Run the application:
```bash
python run.py
```

Follow the prompts to get your personalized meal suggestion!

## Project Structure

```
meal-ai-idea/
├── src/
│   ├── data/
│   │   └── meals.json          # Meal database
│   ├── meal_logic.py           # Core decision logic
│   └── main.py                 # User interface
├── run.py                      # Application runner
├── requirements.txt            # Dependencies (none needed)
└── README.md                   # This file
```

## Learning Objectives Achieved

- Multi-input decision trees and rule-based matching
- Assistance for practical daily decision-making
- Clean program flow with structured inputs/outputs
- Modular code design with separation of concerns

## Example Output

```
Daily Meal Idea Generator
================================

1. What type of meal?
1 - Breakfast
2 - Lunch
3 - Dinner
4 - Snack
Enter choice (1-4): 1

2. How much time do you have?
1 - Less than 10 minutes
2 - 10-30 minutes
3 - More than 30 minutes
Enter choice (1-3): 1

3. Dietary preference?
1 - Vegetarian
2 - Vegan
3 - No restrictions
Enter choice (1-3): 1

==================================================
YOUR MEAL SUGGESTION:
==================================================
Oatmeal with fruits - Mix oats with milk, add banana and berries
==================================================
```

This project demonstrates how straightforward decision-based logic can solve everyday practical problems in a helpful, transparent way.