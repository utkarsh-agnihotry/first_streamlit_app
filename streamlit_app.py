import pandas
import streamlit
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Grapefruit'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

