import os
from langchain_openai import OpenAI  # Updated import based on latest LangChain changes
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_core.exceptions import LangChainException

# Import API key (Ensure secret_key.py exists)
try:
    from secret_key import openai_key
    os.environ['OPENAI_API_KEY'] = openai_key
except ImportError:
    raise ValueError("⚠️ API key missing! Ensure 'secret_key.py' contains 'openai_key'.")

# Initialize OpenAI LLM with error handling
def initialize_llm(temperature=0.7):
    """Initialize OpenAI LLM with a specified temperature."""
    try:
        return OpenAI(temperature=temperature)
    except Exception as e:
        raise ValueError(f"⚠️ Error initializing OpenAI: {e}")

llm = initialize_llm()

# Function to generate restaurant name and menu
def generate_restaurant_name_and_items(cuisine):
    """
    Generates a fancy restaurant name and a list of 10 menu items for a given cuisine.
    
    :param cuisine: Type of cuisine (e.g., Italian, Mexican)
    :return: Dictionary with 'restaurant_name' and 'menu_items'
    """
    try:
        # Chain 1: Restaurant Name Generation
        prompt_template_name = PromptTemplate(
            input_variables=['cuisine'],
            template="I want to open a restaurant for {cuisine} food. Please suggest a fancy name for this restaurant."
        )

        name_chain = LLMChain(
            llm=llm,
            prompt=prompt_template_name,
            output_key="restaurant_name",
        )

        # Chain 2: Menu Item Generation
        prompt_template_items = PromptTemplate(
            input_variables=['restaurant_name'],
            template="Suggest 10 food items for {restaurant_name}."
        )

        food_item_chain = LLMChain(
            llm=llm,
            prompt=prompt_template_items,
            output_key="menu_items",
        )

        # Sequential Chain for Combining Results
        chain = SequentialChain(
            chains=[name_chain, food_item_chain],
            input_variables=['cuisine'],
            output_variables=['restaurant_name', 'menu_items']
        )

        response = chain.invoke({'cuisine': cuisine})  # Updated to use `.invoke()`
        return response

    except LangChainException as e:
        return {"error": f"⚠️ LangChain error: {e}"}
    except Exception as e:
        return {"error": f"⚠️ Unexpected error: {e}"}

# Main execution
if __name__ == "__main__":
    cuisine_type = "Italian"
    result = generate_restaurant_name_and_items(cuisine_type)

    if "error" in result:
        print(result["error"])
    else:
        print(f"🏠 Restaurant Name: {result['restaurant_name'].strip()}")
        print("\n🍴 Menu Items:")
        for item in result["menu_items"].split(","):
            print(f"- {item.strip()}")
