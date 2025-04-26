import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("weather_model.pkl")

st.title("🌦️ Weather Prediction App")

# User input fields (update if your model uses different features)
TAVG = st.number_input("Average Temperature (°C)", value=20.0)
TMAX = st.number_input("Max Temperature (°C)", value=25.0)
TMIN = st.number_input("Min Temperature (°C)", value=15.0)
AWND = st.number_input("Average Wind Speed (m/s)", value=3.5)
PRCP = st.number_input("Precipitation (mm)", value=0.0)
SNOW = st.number_input("Snowfall (mm)", value=0.0)
WSF1 = st.number_input("Fastest 2-minute Wind Speed (m/s)", value=5.0)

# Predict button
if st.button("Predict Weather Condition"):
    input_data = np.array([[TAVG, TMAX, TMIN, AWND, PRCP, SNOW, WSF1]])
    prediction = model.predict(input_data)
    st.success(f"✅ Prediction: {prediction[0]}")
