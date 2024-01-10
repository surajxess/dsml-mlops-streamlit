import pandas as pd
import streamlit as st
import pickle



st.title("Car Price Prediction App")

col1, col2 = st.columns(2)
with col1:
    fuel_type = st.radio('fuel_type',["Petrol", "Diesel", "CNG", "Electric"])

with col2:
    transmission_type = st.selectbox('transmission_type',["Automatic", "Manual"])

col3, col4 = st.columns(2)

with col3:
    engine_power = st.slider('engine_power',100,1500, step=50)

with col4:
    seats = st.selectbox('seats',[2,4,6,7,8])

df = pd.read_csv("C:\\Users\suraj\OneDrive\Desktop\Scaler\MlOps\Dataset\Cars24.csv")
st.dataframe(df)

st.bar_chart(data=df, x="Price", y="Kms Driven)