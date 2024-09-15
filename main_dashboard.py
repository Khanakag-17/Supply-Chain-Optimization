import streamlit as st

# Function to load and execute a Python script
def load_app(file_name):
    with open(file_name, 'r') as f:
        code = f.read()
        exec(code, globals())

# Sidebar for navigation
st.sidebar.image("logo.jpg", use_column_width=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Demand Forecasting", "Optimal Route & Cost", "Associative Prediction", "Intermediate Job Suggestions"])

# Load and execute the selected app
if page == "Demand Forecasting":
    load_app("new_app.py")  # Replace with the correct filename or path

elif page == "Optimal Route & Cost":
    load_app("app.py")  # Replace with the correct filename or path

elif page == "Associative Prediction":
    st.title("Associative Prediction")
    load_app("apriori.py")  # Replace with the correct filename or path
    
elif page == "Intermediate Job Suggestions":
    load_app("job_suggest.py")  # Path to the uploaded app_3.py file


