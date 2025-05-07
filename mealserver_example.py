import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Mealserver Example")


# Define the agent
@fast.agent(
    instruction="""You are a helpful cooking assistant that can provide meal information.
    Use the mealserver tools to find and suggest meals based on user requests.
    When providing meal suggestions, include:
    1. The meal name
    2. A brief description
    3. Key ingredients
    4. Basic preparation instructions
    """,
    servers=["mealserver"],  # Connect to the mealserver MCP server
)
async def main():
    async with fast.run() as agent:
        # Interactive mode allows the user to chat with the agent
        await agent.interactive()

        # Alternatively, you can send specific queries:
        # result = await agent("Find me a meal with chicken and pasta")
        # print(result)
        
        # Or search by category:
        # result = await agent("Suggest a seafood dish")
        # print(result)
        
        # Or get a random meal suggestion:
        # result = await agent("Suggest a random meal for dinner tonight")
        # print(result)


if __name__ == "__main__":
    asyncio.run(main())
