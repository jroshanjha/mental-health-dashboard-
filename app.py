import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title="Mental Health AI Platform",
    page_icon="🧠",
    layout="wide"
    )

st.title("🧠 AI-Powered Mental Health Analytics Platform")


st.markdown("""
### Features

- Depression Risk Prediction
- Stress Score Prediction
- Anxiety Score Prediction
- Wellness Score Prediction
- Mental Health Score Prediction
- Addiction Risk Prediction
- Suicide Risk Prediction
- Explainable AI
""")

df = pd.read_csv("data/mental_health_data_clean.csv")
st.dataframe(df.head())

# Data Cleaning :- 
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.median(), inplace=True)
df.drop(columns=['Unnamed: 0'], inplace=True)  # Example: dropping a non-essential column
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# total users:- 
total_users = df.shape[0]

# average sleep hours :- 
avg_sleep_hours = df['sleep_hours'].mean()
# average wellness score :-
avg_wellness_score = df['wellness_score'].mean()
# average anxiety level :- 
avg_anxiety_level = df['anxiety_level'].mean()
# average mental health score :- 
avg_depression_risk = df['depression_risk'].mean()
# average stress level :- 
avg_stress_level = df['stress_level'].mean()
# average mental health score :- 
avg_mental_health_score = df['mental_health_score'].mean()
# average addiction risk :- 
avg_addiction_score = df['addiction_score'].mean()

# usage_per_sleep_hours :- 
avg_usage_per_sleep_hours = df['usage_per_sleep'].mean()

# Correlation Matrix
correlation_matrix = df.corr()

col1, col2, col3, col4 ,col5 = st.columns(5)

col6,col7,col8,col9= st.columns(4)

col1.metric("Total Users", f"{total_users}")
col2.metric("Avg Sleep Hours", f"{avg_sleep_hours:.1f} hrs")
col3.metric("Avg Wellness Score", f"{avg_wellness_score:.1f}")
col4.metric("Avg Anxiety Level", f"{avg_anxiety_level:.1f}")
col5.metric("Avg Depression Level", f"{avg_depression_risk:.1f}")
col6.metric("Avg Stress Level", f"{avg_stress_level:.1f}")
col7.metric("Avg Mental Health Score", f"{avg_mental_health_score:.1f}")
col8.metric("Avg Addiction Risk", f"{avg_addiction_score:.1f}")
col9.metric("Avg Usage per Sleep Hours", f"{avg_usage_per_sleep_hours:.1f}")

st.subheader("Correlation Matrix")
st.write(correlation_matrix) # api="matplotlib",use_container_width=True,height=500,annotation="Correlation Matrix of Mental Health Metrics"

# Dipression Risk Distribution :-
st.subheader("Depression Risk Distribution")
st.bar_chart(df['depression_risk'].value_counts(),color='blue')   

# Sleep Hours :- 
st.subheader("Sleep Hours Distribution")
#st.bar_chart(df['sleep_hours'].value_counts(),color='blue')
#st.histogram(df['sleep_hours'], bins=10, edgecolor='black', color='blue')

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))
# Plot the histogram with your specified arguments
ax.hist(df['sleep_hours'], bins=10, edgecolor='black', color='blue')
# Display the Matplotlib figure in Streamlit
st.pyplot(fig)


# Daily Sodial Media Hours Distribution :- 
fig, ax = plt.subplots(figsize=(10, 6))
st.subheader("Daily Social Media Hours Distribution")
ax.hist(df['daily_social_media_hours'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# Sleep Efficiency :-
st.subheader("Sleep Efficiency Distribution")
ax.hist(df['sleep_efficiency'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# screen_time_before_sleep :- 
st.subheader("Screen Time Before Sleep Distribution")
ax.hist(df['screen_time_before_sleep'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# academic_performance :-
st.subheader("Academic Performance Distribution")
ax.hist(df['academic_performance'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# physical_activity :- 
st.subheader("Physical Activity Distribution")
ax.hist(df['physical_activity'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# stress_level :-
st.subheader("Stress Level Distribution")
ax.hist(df['stress_level'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# anxiety_level :-
st.subheader("Anxiety Level Distribution")
st.bar_chart(df['anxiety_level'].value_counts(),color='blue')
# st.histogram(df['anxiety_level'], bins=10, edgecolor='black', color='blue')
