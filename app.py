import streamlit as st
import requests
import json
import os # Import the 'os' module to access environment variables

# --- App Title and Description ---
st.title("Customer Churn Prediction")
st.markdown("Enter customer details to predict whether they will churn.")

# --- API URL (Get from environment variable for deployment) ---
# In local development, if the environment variable 'FASTAPI_URL' is not set,
# it will default to "http://127.0.0.1:8000".
# On Render, you will set the 'FASTAPI_URL' environment variable for this Streamlit service
# to point to the public URL of your deployed FastAPI backend.
fastapi_base_url = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000")
api_url = f"{fastapi_base_url}/predict" # Construct the full API endpoint URL

# --- Create Input Fields for User ---
st.sidebar.header("Customer Input Features")

# Create input fields in the sidebar
gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
senior_citizen = st.sidebar.selectbox("Senior Citizen", (0, 1))
partner = st.sidebar.selectbox("Partner", ("Yes", "No"))
dependents = st.sidebar.selectbox("Dependents", ("Yes", "No"))
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
phone_service = st.sidebar.selectbox("Phone Service", ("Yes", "No"))
multiple_lines = st.sidebar.selectbox("Multiple Lines", ("Yes", "No", "No phone service"))
internet_service = st.sidebar.selectbox("Internet Service", ("DSL", "Fiber optic", "No"))
online_security = st.sidebar.selectbox("Online Security", ("Yes", "No", "No internet service"))
online_backup = st.sidebar.selectbox("Online Backup", ("Yes", "No", "No internet service"))
device_protection = st.sidebar.selectbox("Device Protection", ("Yes", "No", "No internet service"))
tech_support = st.sidebar.selectbox("Tech Support", ("Yes", "No", "No internet service"))
streaming_tv = st.sidebar.selectbox("Streaming TV", ("Yes", "No", "No internet service"))
streaming_movies = st.sidebar.selectbox("Streaming Movies", ("Yes", "No", "No internet service"))
contract = st.sidebar.selectbox("Contract", ("Month-to-month", "One year", "Two year"))
paperless_billing = st.sidebar.selectbox("Paperless Billing", ("Yes", "No"))
payment_method = st.sidebar.selectbox("Payment Method", ("Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"))
monthly_charges = st.sidebar.slider("Monthly Charges", 18.0, 120.0, 50.0)
total_charges = st.sidebar.slider("Total Charges", 18.0, 9000.0, 1000.0)

# --- Store User Inputs in a Dictionary ---
input_data = {
    "gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

# --- Prediction Button and Logic ---
if st.button("Predict Churn"):
    # Send a POST request to the API with the user's data
    try:
        response = requests.post(api_url, data=json.dumps(input_data))

        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            probability = result['churn_probability']

            st.subheader("Prediction Result")
            if prediction == "Churn":
                st.error(f"Prediction: Customer will CHURN (Probability: {probability:.2f})")
            else:
                st.success(f"Prediction: Customer will NOT CHURN (Probability: {1 - probability:.2f})")
        else:
            # Display more detailed error from the API if available
            st.error(f"Error from API: Status Code {response.status_code}. Response: {response.text}")
            st.error("Error: Could not get a prediction. Check the API server and its URL.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the prediction API. Ensure the backend is running and accessible.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")