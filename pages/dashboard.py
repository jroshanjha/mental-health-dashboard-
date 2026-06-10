import streamlit as st
import pandas as pd
import joblib

# classifier = joblib.load(
#     "models/depression_classifier.pkl"
# )

# regressor = joblib.load(
#     "models/regressor.pkl"
# )

classifier = joblib.load(
    "models/Classification_Model/Classification-Model/depression_classifier.pkl"
)

regressor = joblib.load(
    "models/Regression-Model/R-model/final_model.pkl"
)

st.title("🧠 Mental Health AI Dashboard")


# Load the dataset
# 🔴 Classification UI

st.header("Depression Risk Prediction")

daily_hours = st.slider(
    "Daily Social Media Hours", 0.0, 15.0
)

stress = st.slider(
    "Stress Level", 0, 10
)

anxiety = st.slider(
    "Anxiety Level", 0, 10
)

if st.button("Predict Risk"):

    input_df = pd.DataFrame([{
        "daily_social_media_hours": daily_hours,
        "stress_level": stress,
        "anxiety_level": anxiety
    }])

    pred = classifier.predict(input_df)

    st.success(f"Risk Level: {pred[0]}")
    
    
# 🔴 Regression UI

st.header("Mental Health Score Prediction")

sleep_efficiency = st.slider(
    "Sleep Efficiency", 0.0, 1.0
)

if st.button("Predict Scores"):

    input_df = pd.DataFrame([{
        "sleep_efficiency": sleep_efficiency
    }])

    pred = regressor.predict(input_df)

    st.write(pred)
    
    
    
# ADVANCED DASHBOARD FEATURES

# Add:

# ✔ KPI Cards
# ✔ Real-time Charts
# ✔ Correlation Heatmap
# ✔ User Segmentation
# ✔ Download Prediction Report
# ✔ SHAP Explainability
# ✔ Risk Gauge Meter
# ✔ Trend Analysis