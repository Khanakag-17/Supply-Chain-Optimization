import streamlit as st
import joblib
import pandas as pd
from datetime import datetime

# Load the pre-trained model
model = joblib.load('best_model.pkl')

# Load the dataset
data = pd.read_csv('Integrated_Dataset - Inventory.csv')  # Replace with your actual dataset path

# Function to predict based on input features
def predict_sales(features):
    prediction = model.predict(features)
    return prediction

# Streamlit App UI
st.title("Sales Prediction App")

# Instructions for the user
st.write("""
#### Instructions:
- Select a city, category, and date from the options above.
- The app will auto-fill other features based on the selected city, category, and date.
- Click "Predict" to see the predicted sales value.
""")

# User input for City, Category, and Date
city_name = st.selectbox('City', data['City'].unique())
category = st.selectbox('Category', data['Category'].unique())
date_input = st.date_input('Select Date')

# Parse the date input and extract the corresponding month and year
selected_month = date_input.strftime('01-%m-2023')

# Filter the dataset based on the selected city and category
filtered_data = data[(data['City'] == city_name) & (data['Category'] == category)]

# Auto-fill the other fields based on the selected city and category
if not filtered_data.empty:
    state = filtered_data['State'].values[0]
    gender_ratio = filtered_data['Gender_Ratio'].values[0]
    literacy_rate = filtered_data['Literacy_Rate'].values[0]
    population = filtered_data['Population'].values[0]
    tier = filtered_data['Tier'].values[0]

    # Extract relevant sales features based on the selected month
    assurance_sales = filtered_data['Assurance_Sales'].values[0]
    holiday_sales = filtered_data['Holiday_Sales'].values[0]
    discount = filtered_data['Discount'].values[0]
    summer_sales = filtered_data['Summer_Sales'].values[0]
    winter_sales = filtered_data['Winter_Sales'].values[0]
    rain_sales = filtered_data['Rain_Sales'].values[0]

    # Initialize all monthly sales columns as 0
    month_sales_features = {col: 0 for col in filtered_data.columns if col.startswith('01-')}

    # Check and extract the sales data for the selected month
    if selected_month in month_sales_features:
        month_sales_features[selected_month] = filtered_data[selected_month].values[0]
    else:
        st.write(f"No sales data available for the selected month: {selected_month}")

else:
    st.error("No data available for the selected city and category.")
    st.stop()

# Prepare the input features as a DataFrame with other features set to 0
input_features = pd.DataFrame({
    'Population': [population],
    'Gender_Ratio': [gender_ratio],
    'Tier': [tier],
    'Literacy_Rate': [literacy_rate],
    'Assurance_Sales': [assurance_sales],
    'Holiday_Sales': [holiday_sales],
    'Discount': [discount],
    'Summer_Sales': [summer_sales],
    'Winter_Sales': [winter_sales],
    'Rain_Sales': [rain_sales],
    **month_sales_features,
    'feature_1': [0],  # Add the monthly sales data with one non-zero value
    # Set all other features to 0 as insignificant
    'Total_Sales': [0],
    # Add other features as needed
})

# Predict button
if st.button('Predict'):
    try:
        prediction = predict_sales(input_features)
        st.write(f"Predicted Sales for {city_name} for {category} category: {prediction[0]:.0f} units")
    except ValueError as e:
        st.error(f"Error in prediction: {e}")
