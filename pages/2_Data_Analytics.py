# 🚀 Step 3: Data Analytics Page
# pages/2_Data_Analytics.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# df['user_type'] = kmeans.fit_predict(
#     df[['daily_social_media_hours', 'sleep_hours', 'stress_level']]
# )
# sns.scatterplot(
#     data=df,
#     x='daily_social_media_hours',
#     y='stress_level',
#     hue='#     df[['daily_social_media_hours', 'sleep_hours', 'stress_level']]
# '
# )
# plt.show()

# sns.scatterplot(
#     data=df,
#     x='sleep_hours',
#     y='stress_level',
#     hue='user_type'
# )
# plt.show()

# Physical Activity vs Stress
# plt.figure(figsize=(12, 8))
# sns.barplot(x='physical_activity',y='stress_level',data=df)
# plt.show()

# sns.boxplot(
#     x='physical_activity',
#     y='stress_level',
#     data=df
# )
# plt.show()

# Insight:
# Active people may have lower stress levels, but we need to control for other factors like sleep and social media use to confirm this.

# Multivariate Analysis
# Pairplot
# sns.pairplot(new_df[
#     ['daily_social_media_hours',
#      'sleep_hours',
#      'stress_level',
#      'anxiety_level']
# ])
# plt.show()

# 3D Relationship Understanding
# sns.scatterplot(
#     x='daily_social_media_hours',
#     y='sleep_hours',
#     hue='depression_risk',
#     size='anxiety_level',
#     data=new_df
# )
# plt.show()

# sns.clustermap(new_df.select_dtypes(include=np.number), cmap='coolwarm')
# plt.show()

#new_df['new_age'] = new_df['age'].map(lambda x: 0 if x >=16 else  1) # age >=16 ( 0 Young ) and <=16 ( 1 Child )

# new_df['gender'] = new_df['gender'].map(lambda x: 0 if x == 'male' else  1) # Male ( 0 ) and Female ( 1 )

# social_interaction_level => low ( 0 ), medium ( 1 ) and high ( 2 )
# new_df['social_interaction_level'] = new_df['social_interaction_level'].map(lambda x: 0 if x == 'low' else (1 if x == 'medium' else 2))

# depression_risk => low ( 0 ), medium ( 1 ) and high ( 2 )
# new_df['depression_risk'] = new_df['depression_risk'].map

df = pd.read_csv("data/mental_health_data.csv")
df['wellness_score'] = (df['stress_level'] + df['anxiety_level'] + df['depression_risk']) / 3
# df['mental_health_score'] = 100 - df['wellness_score'] * 100
st.title("📊 Data Analytics")

st.dataframe(df.head())

# Distribution Plot for Sleep Hours
st.subheader("Sleep Hours Distribution")
st.bar_chart(df['sleep_hours'].value_counts(),color='blue')


# Metrics for Average Levels
avg_depression_score = df['depression_risk'].mean()
avg_sleep_hours = df['sleep_hours'].mean()
avg_wellness_score = df['wellness_score'].mean()
avg_anxiety_level = df['anxiety_level'].mean()
avg_stress_level = df['stress_level'].mean()

# Distribution for social media hours
st.subheader("Daily Social Media Hours Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['daily_social_media_hours'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# Distribution for physical activity
st.subheader("Physical Activity Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['physical_activity'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)

# Correlation Heatmap 
correlation_matrix = df.corr()

st.subheader("Correlation Heatmap")
st.write(correlation_matrix)

# Distribution for academic performance
st.subheader("Academic Performance Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['academic_performance'], bins=10, edgecolor='black', color='blue')
st.pyplot(fig)