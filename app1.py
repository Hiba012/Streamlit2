import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# Charger le modèle et le scaler
model = joblib.load("ranfor.pkl")

st.title("🌦️ Prédiction de la pluie")

# Saisie utilisateur
temp = st.number_input("Température (°C)", step=0.1)
hum = st.number_input("Humidité (%)", step=0.1)
wind = st.number_input("Vitesse du vent", step=0.1)
cloud = st.number_input("Couverture nuageuse (%)", step=0.1)
press = st.number_input("Pression (hPa)", step=0.1)

if st.button("Prédire"):
    data = np.array([[temp, hum, wind, cloud, press]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("🌧️ Il va pleuvoir.")
    else:
        st.success("☀️ Pas de pluie.")
