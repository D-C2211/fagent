import streamlit as st
import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create FastAgent instance
fast = FastAgent("Mealserver Example")

# Define the agent
def register_agent():
    @fast.agent(
        instruction="""You are a helpful cooking assistant that can provide meal information.
        Use the mealserver tools to find and suggest meals based on user requests.
        When providing meal suggestions, include:
        1. The meal name
        2. A brief description
        3. Key ingredients
        4. Basic preparation instructions
        """,
        servers=["mealserver"],
    )
    async def agent_func():
        pass

register_agent()

# Initialize Streamlit app
st.set_page_config(page_title="🍽️ Meal Assistant", layout="wide")
st.title("🍽️ Meal Assistant")

# Initialize chat history if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form("chat_form"):
    user_input = st.text_input("Ask for a meal suggestion or recipe:", key="input")
    submitted = st.form_submit_button("Send")

# Process input
if submitted and user_input:
    async def query_agent(message):
        async with fast.run() as agent:
            return await agent(message)

    result = asyncio.run(query_agent(user_input))

    # Store and display
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": result.text, "image": getattr(result, "image", None)})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Assistant:** {chat['content']}")
        if chat.get("image"):
            st.image(chat["image"], caption="Meal Image")
