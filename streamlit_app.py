import streamlit as st
import pandas as pd
import snowflake.connector

st.title ("My Mom's New Healthy Dinner")
st.header("Breakfast Favourites")
st.text('>> 🥣Omega 3 & Blueberry Oatmeal')
st.text('>> 🥗kale, Spinach, & Rocket Smoothie ')
st.text('>> 🐔Hot-Boiled Free-Range egg')
st.text('>> 🥑Avacado Toast🍞')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:",  list(my_fruit_list.index),["Apple", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)
