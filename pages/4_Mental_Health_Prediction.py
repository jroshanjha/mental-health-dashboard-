# 🚀 Step 5: Mental Health Prediction
# pages/4_Mental_Health_Prediction.py


import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "models/Regression-Model/R-model/final_model.pkl"
    #regression_model.pkl"
)

# st.title("🧠 Mental Health Score Prediction")

# Input Features :-
daily_social_media_hours = st.number_input(
    "Daily Social Media Hours",
    value=5.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    value=7.0
)

screen_time_before_sleep = st.number_input(
    "Screen Time Before Sleep",
    value=2.0
)

academic_performance = st.number_input(
    "Academic Performance",
    value=5
)

physical_activity = st.number_input(
    "Physical Activity",
    value=5
)

social_interaction_level = st.number_input(
    "Social Interaction Level",
    value=5
)

# sleep_efficiency = st.slider(
#     "Sleep Efficiency",
#     0.0,
#     1.0,
#     0.75
# )

# depression_risk = st.number_input(
#     "Depression Risk",
#     value=0.5
# )
sleep_efficiency = st.number_input(
    "Sleep Efficiency",
    value=0.75
)
# addiction_score = st.number_input(
#     "Addiction Score",
#     value=50
# )

addiction_score = ( daily_social_media_hours * screen_time_before_sleep)

# usage_per_sleep = st.number_input(
#     "Usage Per Sleep",
#     value=1.0
# )

usage_per_sleep = daily_social_media_hours / sleep_hours

# input_data = pd.DataFrame(
#     {
#         "daily_social_media_hours": [daily_social_media_hours],
#         "sleep_hours": [sleep_hours],
#         "screen_time_before_sleep": [screen_time_before_sleep],
#         "academic_performance": [academic_performance],
#         "physical_activity": [physical_activity],
#         "social_interaction_level": [social_interaction_level],
#         "sleep_efficiency": [sleep_efficiency],
#         "depression_risk": [depression_risk],
#         # "addiction_score": [addiction_score],
#         "usage_per_sleep": [usage_per_sleep]
#     }
# )

# Predict Mental Health Score
st.subheader("Mental Health Score Prediction")
if st.button("Predict Mental Health Score"): 
    # if st.button("Predict Scores"):

    X = pd.DataFrame([{
        "daily_social_media_hours": daily_social_media_hours,
        "sleep_hours": sleep_hours,
        "screen_time_before_sleep": screen_time_before_sleep,
        "academic_performance": academic_performance,
        "physical_activity": physical_activity,
        "social_interaction_level": social_interaction_level,
        #"depression_risk": depression_risk,
        "sleep_efficiency": sleep_efficiency,
        "addiction_score": addiction_score,
        "usage_per_sleep": usage_per_sleep
    }])

    pred = model.predict(X)
    # st.write(f"Predicted Mental Health Score: {pred[0]:.2f}")
    # prediction = model.predict(input_data)
    # st.write(f"Predicted Mental Health Score: {prediction[0]:.2f}")
    
    # KPI :- 
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Stress Score",
        round(pred[0][0],2)
    )

    col2.metric(
        "Anxiety Score",
        round(pred[0][1],2)
    )

    col3.metric(
        "Wellness Score",
        round(pred[0][2],2)
    )

    col4.metric(
        "Mental Health Score",
        round(pred[0][3],2)
    )