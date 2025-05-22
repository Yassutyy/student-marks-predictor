import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('study_model.pkl')

# UI
st.title("📚 Student Marks Predictor")
st.write("Enter study hours to predict the marks!")

# Input
hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, step=0.5)

# Predict
if st.button("Predict"):
    prediction = model.predict(np.array([[hours]]))
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
