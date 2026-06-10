# 🚀 SHAP Explainability
# pages/6_Explainability.py


import joblib
import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import shap

model = joblib.load(
    "models/Classification_Model/Classification-Model/depression_classifier.pkl"
)

# Remove shap.initjs()

# # Generate your explainer and force plot
# explainer = shap.TreeExplainer(model)
# shap_values = explainer(X)

# # Save the plot as HTML and pass it to Streamlit
# plot_html = shap.plots.force(explainer.expected_value, shap_values[0], matplotlib=False)
# components.html(f"<script>{shap.getjs()}</script>{plot_html.data}", height=400)


# # Generate plot using matplotlib
# fig, ax = plt.subplots()
# shap.images.waterfall(shap_values[0], show=False) # or shap.summary_plot
# st.pyplot(fig)



# explainer = shap.TreeExplainer(model)

# # Display SHAP summary plot and feature impacts for the current prediction.
# shap.initjs()
# shap.summary_plot(
#     explainer.expected_value,
#     model.predict_proba,
#     plot_type="bar"
# )

# explainer = shap.Explainer(model)

# 1. Create explainer
explainer = shap.TreeExplainer(model)

# 2. Calculate SHAP values (use the instances/features you want to explain)
# For example: shap_values = explainer.shap_values(X_test)

# 3. Create a matplotlib figure
fig, ax = plt.subplots()

# 4. Generate the summary plot into the axis
shap.summary_plot(
    explainer.expected_value, # or shap_values depending on your SHAP version
    features=model.predict_proba, 
    plot_type="bar"
)

# 5. Display in Streamlit
st.pyplot(fig)