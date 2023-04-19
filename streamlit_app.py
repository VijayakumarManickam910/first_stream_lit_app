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
st.dataframe(my_fruit_list)
