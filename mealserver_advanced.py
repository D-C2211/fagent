import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Mealserver Advanced Example")


# Define the agent with direct access to mealserver tools
@fast.agent(
    instruction="""You are a cooking assistant that can directly use mealserver tools.
    When asked about meals, use the appropriate tool to find the information.
    Present the information in a clear, organized format.
    """,
    servers=["mealserver"],
)
async def main():
    async with fast.run() as agent:
        print("\n=== Mealserver Advanced Example ===\n")
        
        # Example 1: Get a random meal
        print("Example 1: Getting a random meal...")
        random_meal = await agent("Use the get_random_meal tool to find a random meal suggestion")
        print(f"Random Meal Result: {random_meal}\n")
        
        # Example 2: Get a meal by category
        print("Example 2: Getting a meal by category...")
        seafood_meal = await agent("Use the get_meal_by_category tool to find a Seafood dish")
        print(f"Seafood Meal Result: {seafood_meal}\n")
        
        # Example 3: Get a meal by area
        print("Example 3: Getting a meal by area...")
        italian_meal = await agent("Use the get_meal_by_area tool to find an Italian dish")
        print(f"Italian Meal Result: {italian_meal}\n")
        
        # Example 4: Get a meal by ingredient
        print("Example 4: Getting a meal by ingredient...")
        chicken_meal = await agent("Use the get_meal_by_ingredient tool to find a meal with chicken")
        print(f"Chicken Meal Result: {chicken_meal}\n")
        
        # Example 5: Get a meal by multiple ingredients
        print("Example 5: Getting a meal with multiple ingredients...")
        multi_ingredient = await agent(
            "Use the get_meal_by_multiple_ingredients tool to find a meal with beef and potatoes"
        )
        print(f"Multi-Ingredient Meal Result: {multi_ingredient}\n")
        
        # Example 6: Save ingredients to a file
        print("Example 6: Saving ingredients to a file...")
        save_result = await agent(
            "First, get a random meal using get_random_meal. "
            "Then use the save_ingredients_to_file tool to save its ingredients to 'shopping_list.txt'"
        )
        print(f"Save Ingredients Result: {save_result}\n")


if __name__ == "__main__":
    asyncio.run(main())
