# main.py

# 1. Import necessary libraries
import pickle
import json
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb # We need this to load the model

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

# 4. Load the trained model, scaler, and columns
with open('final_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('model_columns.json', 'r') as f:
    model_columns = json.load(f)

# 5. Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert the input data into a pandas DataFrame
    input_df = pd.DataFrame([data.dict()])

    # One-hot encode the categorical features
    input_df_encoded = pd.get_dummies(input_df)

    # Align the columns of the input data with the columns the model was trained on
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