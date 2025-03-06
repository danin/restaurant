import os
import streamlit as st
import langchain_helper

# Uncomment if using an API key from a separate file
# from secret_key import openapi_key
# os.environ['OPENAI_API_KEY'] = openapi_key

# Streamlit App Title
st.title("🍽️ AI-Powered Restaurant Name & Menu Generator")

# Sidebar for cuisine selection
st.sidebar.header("Customize Your Restaurant")
cuisine = st.sidebar.radio("Pick a Cuisine:", ("Indian", "Italian", "Mexican", "American"))

# Function to generate restaurant details
def fetch_restaurant_details(cuisine):
    try:
        with st.spinner("🤖 Generating restaurant details..."):
            response = langchain_helper.generate_restaurant_name_and_items(cuisine)

        # Extract data safely
        restaurant_name = response.get("restaurant_name", "Unknown Restaurant").strip()
        menu_items = response.get("menu_items", "No menu items available").split(",")

        return restaurant_name, menu_items

    except Exception as e:
        st.error(f"⚠️ Error fetching restaurant details: {e}")
        return None, None

# Display results only if cuisine is selected
if cuisine:
    restaurant_name, menu_items = fetch_restaurant_details(cuisine)

    if restaurant_name:
        st.header(f"🏠 Restaurant Name: {restaurant_name}")

        # Display menu
        st.subheader("🍴 Menu Items")
        st.write("Here are some recommended dishes for your restaurant:")

        for item in menu_items:
            st.markdown(f"- {item.strip()}")  # Using Markdown for cleaner list format
