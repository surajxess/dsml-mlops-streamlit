import pandas as pd
import streamlit as st
import pickle
import datetime



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

st.bar_chart(data=df, x="Price", y="Driven (Kms)")

d = st.date_input("Enter the date", datetime.date(2023,1,2))
st.write ("Date is:" ,d)

model = pickle.load(open("car_pred","rb"))

# with open("car_pred","rb") as f:
    # model = pickle.load(f)

encode_dict = {
    {"fuel_type":{"Petrol":0, "Diesel":1, "CNG":2, "electric":3},
     transmission":{"automatic": 0, "manual": 1}
     }
}

def model_pred(Fuel, Gear, engine_power, seats):
    transmission_type = encode_dict["transmission"][Gear]
    fuel_type = decode_dict["fuel_type"][Fuel]

    #This is a new line