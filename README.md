# FastAgent with Mealserver MCP

This repository contains examples of using the FastAgent framework with the Mealserver MCP server.

## Setup

1. Make sure you have the mealserver running at `C:\mcp\mealserver`
2. The configuration in `fastagent.config.yaml` is already set up to use the mealserver

## Examples

This repository includes two example scripts that demonstrate how to use the mealserver:

### Basic Example (mealserver_example.py)

This example creates a simple interactive agent that can use the mealserver to provide meal information based on user requests.

```bash
python mealserver_example.py
```

### Advanced Example (mealserver_advanced.py)

This example demonstrates how to use specific mealserver tools to:
- Get random meal suggestions
- Find meals by category
- Find meals by area/cuisine
- Find meals by ingredient
- Find meals with multiple ingredients
- Save ingredients to a shopping list file

```bash
python mealserver_advanced.py
```

## Available Mealserver Tools

The mealserver provides the following tools:

- `get_meal_by_letter`: Get meal by letter (e.g., "A", "B")
- `get_meal_by_name`: Get meal by name (e.g., "Arrabiata", "Spicy")
- `get_random_meal`: Get a random meal suggestion
- `get_meal_by_category`: Get meal by category (e.g., "Seafood")
- `get_meal_by_area`: Get meal by area/cuisine (e.g., "Canadian")
- `get_meal_by_ingredient`: Get meal by ingredient (e.g., "chicken_breast")
- `get_meal_by_multiple_ingredients`: Get meals containing multiple ingredients (e.g., ["beef", "potatoes"])
- `save_ingredients_to_file`: Save ingredients of a meal to a file (shopping list)

## Resources

The mealserver also provides these resources:
- `http://localhost/meal_categories`: List of available meal categories
- `http://localhost/cuisine_areas`: List of available cuisine areas
- `http://localhost/common_ingredients`: List of common ingredients
