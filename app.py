import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor

# Load the pre-trained CatBoost model
cat_model = CatBoostRegressor()
cat_model.load_model("cat_model.cbm")

# Define the feature columns
feature_columns = [str(year) for year in range(1980, 2024)]

# Streamlit app
st.title("Inflation Prediction Web App")
st.write("This app predicts the inflation rate for the year 2024 based on historical data.")

# Input form for user data
st.sidebar.header("Input Features")
user_input = {}
for year in feature_columns:
    user_input[year] = st.sidebar.number_input(f"Inflation Rate for {year}", value=0.0)

# Convert user input to DataFrame
input_data = pd.DataFrame([user_input])

# Predict button
if st.button("Predict"):
    # Make prediction
    prediction = cat_model.predict(input_data)
    st.success(f"Predicted Inflation Rate for 2024: {prediction[0]:.2f}%")