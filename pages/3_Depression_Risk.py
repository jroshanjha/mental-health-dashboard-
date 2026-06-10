# 🚀 Step 4: Depression Risk Prediction
# pages/3_Depression_Risk.py

import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "models/Classification_Model/Classification-Model/depression_classifier.pkl"
)

# Input Features :- 
daily_social_media_hours = st.slider(
    "Daily Social Media Hours",
    0.0,
    15.0,
    5.0
)
screen_time_before_sleep = st.slider(
    "Screen Time Before Sleep (hours)",
    0.0,
    10.0,
    5.0
)
sleep_hours = st.slider(
    "Sleep Hours",
    0.0,
    10.0,
    5.0
)

academic_performance = st.slider(
    "Academic Performance",
    1,
    10,
    5
)

physical_activity = st.slider(
    "Physical Activity",
    0,
    10,
    5
)

stress_level = st.slider(
    "Stress Level",
    0,
    10,
    5
)

anxiety_level = st.slider(
    "Anxiety Level",
    0,
    10,
    5
)

# user_type = st.selectbox(
#     "User Type",
#     [0,1,2,3]
# )

mental_health_score = st.slider(
    "Mental Health Score",
    0,
    100,
    50
)

# mental_health_score = stress_level + anxiety_level 

sleep_efficiency = st.slider(
    "Sleep Efficiency",
    0.0,
    1.0,
    0.75
)

# addiction_score = st.slider(
#     "Addiction Score",
#     0,
#     100,
#     50
# )

addiction_score = ( daily_social_media_hours * screen_time_before_sleep)

wellness_score = st.slider(
    "Wellness Score",
    0,
    100,
    50
)

# wellness_score = (stress_level + anxiety_level + addiction_score) / 3
# wellness_score = (sleep_hours + physical_activity) - stress_level - anxiety_level + addiction_score
# n_df['sleep_hours'] +
#     n_df['physical_activity'] -
#     n_df['stress_level']

st.subheader("Depression Risk Prediction")

st.write("Input the features to predict depression risk")

# input_data = [[
#     daily_social_media_hours,
#     screen_time_before_sleep,
#     sleep_hours,
#     academic_performance,
#     physical_activity,
#     stress_level,
#     anxiety_level,
#     mental_health_score,
#     sleep_efficiency,
#     addiction_score,
#     wellness_score
# ]]


data = pd.DataFrame([{
        "daily_social_media_hours": daily_social_media_hours,
        "academic_performance": academic_performance,
        "physical_activity": physical_activity,
        "stress_level": stress_level,
        "anxiety_level": anxiety_level,
        # "user_type": user_type,
        'mental_health_score': mental_health_score,
        "sleep_efficiency": sleep_efficiency,
        "addiction_score": addiction_score,
        "wellness_score": wellness_score
    }])

if st.button("Predict Risk"):
    
    labels = {
        0: "Low",
        # 1: "Medium",
        1: "High"
    }
    prediction = model.predict(data)
    #risk_mapping = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    risk_mapping = {0: "Low Risk", 1: "High Risk"}
    st.write(f"Predicted Depression Risk: {risk_mapping[prediction[0]]}")
    
    st.success(
        f"Depression Risk: {labels[int(prediction[0])]}"
    )