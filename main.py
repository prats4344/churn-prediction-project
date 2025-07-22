# main.py

# 1. Import necessary libraries
import pickle
import json
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb # We need this to load the model
from fastapi.middleware.cors import CORSMiddleware # NEW: Import CORSMiddleware

# 2. Create a class for the input data
# This ensures that the API receives data in the correct format
class InputData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# 3. Create a FastAPI app instance
app = FastAPI()

# NEW: Configure CORS middleware
# This allows your Streamlit frontend (on a different domain) to access this API
origins = [
    "http://localhost:8501",  # Allows local Streamlit development to access
    "https://customer-churn-frontend.onrender.com", # THIS IS YOUR ACTUAL STREAMLIT APP URL ON RENDER!
    # You can add other origins if your app will be accessed from other domains
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# END NEW CORS CONFIGURATION

# --- THIS IS THE NEW PART WE ARE ADDING ---
# This creates a "welcome" message at the base URL (the "/")
@app.get("/")
def read_root():
    return {"message": "Churn Prediction API is running!"}
# --- END OF NEW PART ---


# 4. Load the trained model, scaler, and columns
# Ensure these files (final_model.pkl, scaler.pkl, model_columns.json)
# are in the correct path relative to where main.py runs on Render.
# If they are in a 'src/' folder, you might need 'src/final_model.pkl' etc.
try:
    with open('final_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('model_columns.json', 'r') as f:
        model_columns = json.load(f)
except FileNotFoundError as e:
    print(f"Error loading model artifacts: {e}. Make sure 'final_model.pkl', 'scaler.pkl', and 'model_columns.json' are in the correct directory.")
    # You might want to raise an exception or handle this more gracefully in a production app
    # For now, we'll let it fail if files are missing, which Render logs will show.


# 5. Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert the input data into a pandas DataFrame
    input_df = pd.DataFrame([data.dict()])

    # One-hot encode the categorical features
    # Ensure all original categories are handled or that your preprocessing pipeline
    # during training also uses pd.get_dummies consistently.
    input_df_encoded = pd.get_dummies(input_df)

    # Align the columns of the input data with the columns the model was trained on
    # This is crucial to ensure the order and presence of all features
    input_df_aligned = input_df_encoded.reindex(columns=model_columns, fill_value=0)

    # Scale the aligned data using the loaded scaler
    input_scaled = scaler.transform(input_df_aligned)

    # Make a prediction
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    # Return the result
    return {
        "prediction": "Churn" if prediction[0] == 1 else "No Churn",
        "churn_probability": float(probability[0][1])
    }