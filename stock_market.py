import streamlit as st 
import pandas as pd 
import yfinance as yf

st.title("Stock Market App")
# streamlit run stock_market.py


st.write("This is my hope of getting hike")

ticker_symbol = st.text_input("Ticker Symbol", "AAPL")

# Date Input
starting_date = st.date_input("Enter Starting Date",value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter Ending Date",value=pd.to_datetime("today"))

ticker_data = yf.Ticker(ticker_symbol)
history = ticker_data.history(start= starting_date, end= ending_date)



st.write("I am going to show you Microsoft Data")
st.write(history)

col1, col2 = st.columns(2)
with col1:
    st.write("Volume chart")
    st.line_chart(history.Volume)

with col2:
    st.write("Close chart")
    st.line_chart(history.Close)
