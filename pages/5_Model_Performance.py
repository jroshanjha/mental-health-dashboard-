# 🚀 Step 6: Model Performance Page
# pages/5_Model_Performance.py
import streamlit as st
import pandas as pd
# Show:

# Accuracy
# Precision
# Recall
# F1 Score
# ROC-AUC

#st.metric(A)

st.metric(
    "XGBoost Train Accuracy",
    "89.3%"
)
st.metric(
    "XGBoost Test Accuracy",
    "88.4%"
)

st.metric(
    "XgBoost Accuracy",
    "88.3%"
)
st.metric(
    "XGBoost Precision",
    "80.45%"
)
st.metric(
    "XGBoost Recall",
    "100.0%"
)

st.metric(
    "XGBoost F1 Score",
    '89.16%'
)

# Confusion Matrix :- [[193  60]
#  [  0 247]]

st.metric(
    "XGBoost ROC-AUC",
    "100.0%"
)

st.metric("Confusion Matrix", "\n[[193  60]\n [  0 247]]"
          )
# Actual True vs Predicted True :- 247
# Actual True vs Predicted False :- 0
# Actual False vs Predicted True :- 60
# Actual False vs Predicted False :- 193

# Table Format :-
# Confusion Matrix Details
st.metric(
    "Confusion Matrix Details",
    "Actual True vs Predicted True: 247\nActual True vs Predicted False:\n0\nActual False vs Predicted True: 60\nActual False vs Predicted False: 193"
)

# st.metric(
#     "Confusion Matrix Details",
#     "Actual True vs Predicted True: 247\nActual True vs Predicted False:\
#     0\nActual False vs Predicted True: 60\nActual False vs Predicted False: 193"
# )

# Classification Report :-               
#                   precision    recall  f1-score   support
  
#            0       1.00      0.76      0.87       253
#            1       0.80      1.00      0.89       247

#       accuracy                         0.88       500
#       macro avg       0.90      0.88      0.88       500
#    weighted avg       0.88      0.88      0.88       500

st.metric(
    "Classification Report",
    "Precision: 1.00 (Class 0), 0.80 (Class 1)\nRecall: 0.76 (Class 0), 1.00 (Class 1)\nF1-Score: 0.87 (Class 0), 0.89 (Class 1)"
)


# Regression :- 

# R2 Score :- 
st.metric(
    "R2 Score",
    "91.98"
)

# MAE :- 
st.metric(
    "MAE",
    "83.88"
)

# MSE :- 
st.metric(
    "MSE",
    "130.64"
)

# RMSE :- 
st.metric(
    "RMSE",
    "11.42"
)

# # MAPE :- 
# st.metric(
#     "MAPE",
#     "0.01"
# )

# Adjusted R2 Score :- 
st.metric(
    "Adjusted R2 Score",
    "91.82"
)

# Training Score :- 
st.metric(
    "Train R2 Score",
    "93.25"
)

# Training Standard Error :- 
st.metric(
    "Train RMSE",
    "6.75"
)

# Test Standard Error :- 
st.metric(
    "Test RMSE",
    "8.2"
)

# Test Score :- 
st.metric(
    "Test R2 Score",
    "91.98"
)