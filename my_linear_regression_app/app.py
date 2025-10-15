# app.py
import streamlit as st
import pickle
import numpy as np
import os

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="🏡 California House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Load model
# ---------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "house_price_prediction.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Model file not found! Place house_price_prediction.pkl in this folder.")
    st.stop()

# ---------------------------
# App title
# ---------------------------
st.markdown("<h1 style='text-align:center;color:#4B0082;'>🏡 California House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#6A5ACD;'>Adjust the features and see the predicted price instantly!</p>", unsafe_allow_html=True)
st.write("---")

# ---------------------------
# Input sliders in columns
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    MedInc = st.slider("Median Income (10k USD)", 0.0, 20.0, 5.0, 0.1)
    HouseAge = st.slider("House Age (years)", 1, 52, 20)

with col2:
    AveRooms = st.slider("Average Rooms", 1.0, 15.0, 5.0, 0.1)
    AveBedrms = st.slider("Average Bedrooms", 0.5, 5.0, 1.0, 0.1)

with col3:
    Population = st.slider("Population", 1, 5000, 1000)
    AveOccup = st.slider("Average Occupancy", 0.5, 10.0, 3.0, 0.1)

with col4:
    Latitude = st.slider("Latitude", 32.0, 42.0, 35.0, 0.01)
    Longitude = st.slider("Longitude", -124.0, -114.0, -120.0, 0.01)

# ---------------------------
# Predict price
# ---------------------------
input_array = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
prediction = model.predict(input_array)[0]

st.markdown(
    f"""
    <div style="background: linear-gradient(90deg, #FF7F50, #FF4500); padding:25px; border-radius:15px; text-align:center;">
        <h2 style='color:white;'>💰 Predicted Median House Price: ${prediction*100000:.2f}</h2>
    </div>
    """,
    unsafe_allow_html=True
)
