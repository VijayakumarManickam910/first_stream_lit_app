import streamlit as st

st.title ("My Mom's New Healthy Dinner")
st.header("Breakfast Favourites")
st.text('>> Omega 3 & Blueberry Oatmeal 🥗')
st.text('>> kale, Spinach, & Rocket Smoothie 🥣')
st.text('>> Hot-Boiled Free-Range egg 🐔')
st.text('>> Avacado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index))


st.dataframe(my_fruit_list)
