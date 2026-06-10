# 🚀 Step 2: Home Page
# pages/1_Home.py

import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/mental_health_data_clean.csv')

# Data Cleaning :- 
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.fillna(data.median(), inplace=True)
data.drop(columns=['Unnamed: 0'], inplace=True)  # Example: dropping a non-essential column
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)


# EDA :-
# 1. Total Users 
total_users = len(data)
total_gender = data['gender'].nunique()

# 2. Average Sleep Hours
avg_sleep_hours = data['sleep_hours'].mean()
# 3. Average Wellness Score
avg_wellness_score = data['wellness_score'].mean()
# 4. Average Anxiety Level
avg_anxiety_level = data['anxiety_level'].mean()
avg_stress_level = data['stress_level'].mean()

# 5. social_interaction_level Distribution
social_interaction_counts = data['social_interaction_level'].value_counts()

# 6. Correlation Matrix
correlation_matrix = data.corr()

st.title("🏠 Dashboard Overview")

col1, col2, col3, col4 ,col5,col6= st.columns(6)

# col1.metric("Users", "5,000")
# col2.metric("Avg Sleep", "6.8 hrs")
# col3.metric("Avg Wellness", "62")
# col4.metric("Avg Anxiety", "5.4")
col1.metric("Total Users", f"{total_users}")
col2.metric("Total Gender", f"{total_gender}")
col3.metric("Avg Sleep Hours", f"{avg_sleep_hours:.1f} hrs")
col4.metric("Avg Wellness Score", f"{avg_wellness_score:.1f}")
col5.metric("Avg Anxiety Level", f"{avg_anxiety_level:.1f}")
col6.metric("Avg Stress Level", f"{avg_stress_level:.1f}")

st.subheader("Social Interaction Level Distribution")
st.bar_chart(social_interaction_counts)

st.subheader("Correlation Matrix")
# caption="Correlation Matrix of Mental Health Metrics"
st.write(correlation_matrix) # api="matplotlib",use_container_width=True,height=500,annotation="Correlation Matrix of Mental Health Metrics"

# Data Visualizations :-

# 1. Gender Distribution
st.subheader("Gender Distribution")
st.bar_chart(data['gender'].value_counts(),color='grey')
# st.pyplot(plt.figure(figsize=(10, 6)))

# 2. Age Distribution
st.subheader("Age Distribution")
st.bar_chart(data['new_age'].value_counts(),color='blue')
# st.pyplot(plt.figure(figsize=(10, 6)))


# 3. Depression Risk Distribution
st.subheader("Depression Risk Distribution")
st.bar_chart(data['depression_risk'].value_counts(),color='green')
# st.pyplot(plt.figure(figsize=(10, 6)))


# 4. Suicide Risk Distribution
# plt.figure(figsize=(10, 6))
# sns.countplot(x='suicide_risk', data=data)
# plt.title('Suicide Risk Distribution')
# plt.xlabel('Suicide Risk')
# plt.ylabel('Count')
# plt.show()

# 7. Sleep Hours vs Stress Level
st.subheader("Sleep Hours vs Stress Level")
#st.scatter_chart(x=data['sleep_hours'],y=data['stress_level'],color='red',size=10)
#st.scatter_chart(x='sleep_hours', y='stress_level', color='red', size=10)
st.scatter_chart(
    data=data, 
    x='sleep_hours', 
    y='stress_level', 
    color=None,  # 'color' doesn't take a standard color like red here, omit or use a categorical column
    size=10
)

# 8. Wellness Score vs Anxiety Level
st.subheader("Wellness Score vs Anxiety Level")
st.scatter_chart(data=data,x='wellness_score', y='anxiety_level', color='blue', size=10)



# 9. screen time before sleep vs sleep hours
st.subheader("Screen Time Before Sleep vs Sleep Hours")
st.scatter_chart(data=data,x='screen_time_before_sleep', y='sleep_hours', color='green', size=10)

# Screen time before sleep vs academic performance
st.subheader("Screen Time Before Sleep vs Academic Performance")
st.scatter_chart(data=data,x='screen_time_before_sleep', y='academic_performance', color='blue', size=10)

# 10. Depression Risk Distribution
st.subheader("Depression Risk Distribution")
st.bar_chart(data['depression_risk'].value_counts(),color='red')
# st.pyplot(plt.figure(figsize=(10, 6)))

# 12. Anxiety Level Distribution
st.subheader("Anxiety Level Distribution")
st.bar_chart(data['anxiety_level'].value_counts(),color='blue')
# st.pyplot(plt.figure(figsize=(10, 6)))

# 13. Stress Level Distribution
st.subheader("Stress Level Distribution")
st.bar_chart(data['stress_level'].value_counts(),color='orange')


# 14. Wellness Score Distribution
st.subheader("Wellness Score Distribution")
st.bar_chart(data['wellness_score'].value_counts(),color='green')
# st.pyplot(plt.figure(figsize=(10, 6)))


# 15. Social Interaction Level Distribution
st.subheader("Social Interaction Level Distribution")
st.bar_chart(data['social_interaction_level'].value_counts(),color='grey')


# 16. Social Media Hours Distribution
st.subheader("Social Media Hours Distribution")
st.bar_chart(data['daily_social_media_hours'].value_counts(),color='blue')
# plt.figure(figsize=(10, 6))
# sns.countplot(x='daily_social_media_hours', data=data)
# plt.title('Social Media Hours Distribution')
# plt.xlabel('Social Media Hours')
# plt.ylabel('Count')
# plt.show()  

# 17. Physical Activity Level Distribution
st.subheader("Physical Activity Level Distribution")
st.bar_chart(data['physical_activity'].value_counts(),color='green')
# plt.figure(figsize=(10, 6))
# sns.countplot(x='physical_activity', data=data)
# plt.title('Physical Activity Level Distribution')
# plt.xlabel('Physical Activity Level')
# plt.ylabel('Count')
# plt.show()

# 18. Physical Activity vs sleep Hours Distribution
st.subheader("Physical Activity Hours Distribution")
st.scatter_chart(data=data,x='physical_activity', y='sleep_hours', color='orange', size=10)

# 19. Sleep Hours Distribution
st.subheader("Sleep Hours Distribution")
st.bar_chart(data['sleep_hours'].value_counts(),color='red')

# 20. Sleep Quality Distribution
st.subheader("Sleep Quality Distribution")
st.bar_chart(data['sleep_efficiency'].value_counts(),color='yellow')


# Pie Chart for Gender 
# Data for the pie chart
st.subheader("Gender Distribution (Pie Chart)")
labels = data['gender'].unique()
sizes = data['gender'].value_counts().values

explode = [0.1 if label == 'female' else 0 for label in labels]  # Explode the female slice
# Create a pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
# Display the pie chart in Streamlit
st.pyplot(fig1)


# Pie Chart for Depression Risk
st.subheader("Depression Risk Distribution (Pie Chart)")
labels = data['depression_risk'].unique()
sizes = data['depression_risk'].value_counts().values
explode = [0.1 if label == 2 else 0 for label in labels]  # Explode the high risk slice
fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
ax2.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
st.pyplot(fig2)
