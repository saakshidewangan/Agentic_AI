import os
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Recipe Agent
recipe_agent = Agent(
    name="Recipe Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Provide recipes in a structured format with ingredients and steps."],
    markdown=True,
    debug_mode=True
)

# Get user input for the dish
dish_name = input("Enter the dish name: ")

# Fetch and print the recipe
recipe_agent.print_response(f"Give me a detailed recipe for {dish_name} including ingredients and cooking steps.", stream=True)
