# Gender -> Female=1 , Male=0
# Churn  -> Yes=1 , No=0
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the X is ['Age', 'Gender', 'Tenure', 'MonthlyCharges']

import streamlit as st
import joblib
import numpy as np
import pandas as pd

scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please Enter the values and hit the prediction button to get prediction")

st.divider()

age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)

monthlyCharges = st.number_input("Enter Monthly Charges", min_value=30, max_value=150)

gender = st.selectbox("Enter the Gender",["Male","Female"])

st.divider()

predictbutton = st.button("Predict")

st.divider()

if predictbutton:
    gender = 1 if gender == "Female" else 0

    X = pd.DataFrame([[age, gender, tenure, monthlyCharges]], columns=['Age', 'Gender', 'Tenure', 'MonthlyCharges'])

    X_array = scaler.transform(X)

    prediction = model.predict(X_array)[0]

    predicated = "Continue" if prediction == 1 else "No Continue"

    st.balloons()

    st.write(f"The model predicts that the customer will {predicated} with the service.")

else:
    st.write("Please enter the values and click on the predict button to get the prediction.")