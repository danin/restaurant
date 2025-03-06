from langchain.llms import OpenAI  
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain  
from secret_key import openai_key

import os

os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Please suggest a fancy name for this restaurant."
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name",
    )

    # Chain 2: Restaurant Menu Suggestion
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 10 food items for {restaurant_name}."
    )

    food_item_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key="menu_items",
    )

    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})  
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
