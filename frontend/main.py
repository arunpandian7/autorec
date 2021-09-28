import streamlit as st
import pandas as pd

st.write(""" # Retail Product Recommendation
 *A product recommendation is basically a filtering system that seeks to predict and show the items that a user would like to purchase*""")

df = pd.read_csv("./dataset/retail.csv")

filter_button = st.radio("Get recommendations by", ("User","Product")) 
display_count = st.slider(label='Select number of items to display', min_value=0, max_value=100, key=4)

if filter_button == "Product":
    st.write(df[["StockCode","Description","UnitPrice"]].sample(display_count))
elif filter_button == "User":
    first_column = df.pop('CustomerID')
    df.insert(0, 'CustomerID', first_column)
    st.write(df.sample(display_count))

form = st.form(key='input_form')
user_input = form.text_input(f'Enter {filter_button} ID')
submit = form.form_submit_button('Get Recommendations')
if submit:
    st.write(f'Fetching recommendations for {filter_button} ID : {user_input} ...')