from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

classifier = joblib.load(
    "models/Classification_Model/Classification-Model/depression_classifier.pkl"
)

regressor = joblib.load(
    "models/Regression-Model/R-model/final_model.pkl"
)

# Load the dataset
# 📌 Convert target labels
# mapping = {
#     "Low": 0,
#     "Medium": 1,
#     "High": 2
# }

# df['depression_risk_level'] = (
#     df['depression_risk_level'].map(mapping)
# )

# 📌 train_classifier.py
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# import joblib

# X = df[features]
# y = df['depression_risk_level']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2
# )

# model = RandomForestClassifier()

# model.fit(X_train, y_train)

# preds = model.predict(X_test)

# print(classification_report(y_test, preds))

# joblib.dump(model, "models/depression_classifier.pkl")


# 📈 Evaluation Metrics

# Use:

# Accuracy
# Precision
# Recall
# F1-score
# Confusion Matrix
# ROC-AUC


# Multi-Output Regression

# Predict multiple scores together:

# addiction_score
# mental_health_score
# anxiety_score
# stress_score
# wellness_score



# 🧩 STEP 1: Define Features
# features = [
#     'sleep_efficiency',
#     'daily_social_media_hours',
#     'sleep_hours',
#     'usage_per_sleep',
#     'screen_time_before_sleep',
#     'academic_performance',
#     'physical_activity',
#     'social_interaction_level'
# ]
# 🧩 STEP 2: Train Multi-Output Regressor
# 📌 train_regressor.py
# from sklearn.multioutput import MultiOutputRegressor
# from sklearn.ensemble import RandomForestRegressor

# targets = [
#     'addiction_score',
#     'mental_health_score',
#     'anxiety_score',
#     'stress_score',
#     'wellness_score'
# ]

# X = df[features]
# y = df[targets]

# model = MultiOutputRegressor(
#     RandomForestRegressor()
# )

# model.fit(X, y)

# joblib.dump(model, "models/regressor.pkl")
# 📊


# 📊 Regression Metrics

# Use:

# MAE
# MSE
# RMSE
# R² Score
# Adjusted R² Score



# 🔴 Classification Endpoint
@app.post("/predict-risk")

def predict_risk(data: dict):

    df = pd.DataFrame([data])

    pred = classifier.predict(df)

    return {
        "depression_risk_level": int(pred[0])
    }
    
    
# 🔵 Regression Endpoint

@app.post("/predict-scores")

def predict_scores(data: dict):

    df = pd.DataFrame([data])

    pred = regressor.predict(df)

    return {
        "predictions": pred.tolist()
    }