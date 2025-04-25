import streamlit as st
import joblib
import numpy as np

model = joblib.load('weather_model.pkl')

st.title("Weather Forecast Prediction")
day = st.number_input("Day", min_value=1, max_value=31, value=15)
month = st.number_input("Month", min_value=1, max_value=12, value=4)

input_data = np.array([[day, month]])
prediction = model.predict(input_data)

st.write(f"Predicted Temperature: {prediction[0]:.2f}°C")
