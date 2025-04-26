import streamlit as st
import joblib
import numpy as np

model = joblib.load("weather_model.pkl")

st.title("Weather Prediction App")
st.header("Enter Weather Details")

temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0)
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0)
if st.button("Predict"):
    input_data = np.array([[temperature, humidity, wind_speed, pressure]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Weather Condition: {prediction[0]}")
