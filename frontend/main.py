import streamlit as st
import pandas as pd

st.write(""" # Retail Product Recommendation
 *A product recommendation is basically a filtering system that seeks to predict and show the items that a user would like to purchase*""")

df = pd.read_csv("./dataset/retail.csv")

filter_button = st.radio("Get recommendations by", ("User","Product")) 

if filter_button == "Product":
    st.write(df[["StockCode","Description","UnitPrice"]].sample(10))
elif filter_button == "User":
    st.write(df.sample(10))

form = st.form(key='input_form')
user_input = form.text_input(f'Enter {filter_button} ID')
submit = form.form_submit_button('Get Recommendations')
if submit:
    st.write(f'Fetching recommendations for {filter_button} ID : {user_input} ...')