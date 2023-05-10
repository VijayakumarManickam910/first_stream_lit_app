import streamlit as st

st.title ("My Mom's New Healthy Dinner")

st.header('Breakfast Favourites')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗kale, Spinach, & Rocket Smoothie ')
st.text('🐔Hot-Boiled Free-Range egg')
st.text('🥑🍞Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),["Apple", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(my_fruit_list)

# New section to display fruityvice api response
st.header('Fruityvice Fruit Advice')
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

pip install --upgrade snowflake-connector-python
pip install --upgrade charset-normalizer==2.0.0
pip install --upgrade urllib3==1.26.7
python -m venv myenv
myenv\Scripts\activate
python -m pip install --upgrade pip

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
