import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("don_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Corn Mycotoxin Prediction App 🌽")
st.write("Upload spectral reflectance data to predict vomitoxin levels.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "vomitoxin_ppb" in df.columns:
        df = df.drop(columns=["vomitoxin_ppb"])  # Remove target column if exists

    # Normalize features
    X_scaled = scaler.transform(df)

    # Predict
    predictions = model.predict(X_scaled)
    predictions = np.expm1(predictions)  # Reverse log transformation

    # Show results
    df["Predicted Vomitoxin"] = predictions
    st.dataframe(df)

    # Download results
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Predictions", data=csv, file_name="predictions.csv", mime="text/csv")
