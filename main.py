#from secret_key import openapi_key
import os
#from langchain.llms import OPENAI
import streamlit as st
import langchain_helper 

#os.environ['OPENAI_API_KEY'] = openapi_key


st.title ("Restaurant Name Generator:")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].split(',')

    st.write("***Menu ITEMS ***")
    for item in menu_items:
        st.write ("-", item)