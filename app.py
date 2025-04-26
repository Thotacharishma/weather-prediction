import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("weather_model.pkl")

st.title("🌦️ Weather Prediction App")

st.markdown("Enter the following weather-related inputs to predict the weather condition:")

# Input fields (23 total)
prcp = st.number_input("Precipitation (prcp)", value=0.0)
snow = st.number_input("Snowfall (snow)", value=0.0)
snwd = st.number_input("Snow Depth (snwd)", value=0.0)
tmax = st.number_input("Max Temperature (tmax)", value=25.0)
tmin = st.number_input("Min Temperature (tmin)", value=15.0)
rolling_3_tmax = st.number_input("3-Day Rolling Max Temp")
rolling_3_tmax_pct = st.number_input("3-Day Max Temp % Change")
rolling_3_tmin = st.number_input("3-Day Rolling Min Temp")
rolling_3_tmin_pct = st.number_input("3-Day Min Temp % Change")
rolling_3_prcp = st.number_input("3-Day Rolling Precip")
rolling_3_prcp_pct = st.number_input("3-Day Precip % Change")
rolling_14_tmax = st.number_input("14-Day Rolling Max Temp")
rolling_14_tmax_pct = st.number_input("14-Day Max Temp % Change")
rolling_14_tmin = st.number_input("14-Day Rolling Min Temp")
rolling_14_tmin_pct = st.number_input("14-Day Min Temp % Change")
rolling_14_prcp = st.number_input("14-Day Rolling Precip")
rolling_14_prcp_pct = st.number_input("14-Day Precip % Change")
month_avg_tmax = st.number_input("Monthly Avg Max Temp")
day_avg_tmax = st.number_input("Daily Avg Max Temp")
month_avg_tmin = st.number_input("Monthly Avg Min Temp")
day_avg_tmin = st.number_input("Daily Avg Min Temp")
month_avg_prcp = st.number_input("Monthly Avg Precip")
day_avg_prcp = st.number_input("Daily Avg Precip")

# Input array
input_data = np.array([[prcp, snow, snwd, tmax, tmin,
                        rolling_3_tmax, rolling_3_tmax_pct,
                        rolling_3_tmin, rolling_3_tmin_pct,
                        rolling_3_prcp, rolling_3_prcp_pct,
                        rolling_14_tmax, rolling_14_tmax_pct,
                        rolling_14_tmin, rolling_14_tmin_pct,
                        rolling_14_prcp, rolling_14_prcp_pct,
                        month_avg_tmax, day_avg_tmax,
                        month_avg_tmin, day_avg_tmin,
                        month_avg_prcp, day_avg_prcp]])

# Human-readable weather labels (adjust this to your actual labels)
weather_labels = {
    0: "Sunny",
    1: "Rainy",
    2: "Snowy",
    3: "Cloudy",
    4: "Stormy"
}

# Predict and show result
if st.button("Predict Weather Condition"):
    prediction = model.predict(input_data)[0]
    readable_output = weather_labels.get(prediction, f"Unknown ({prediction})")
    st.success(f"✅ Predicted Weather: {readable_output}")
