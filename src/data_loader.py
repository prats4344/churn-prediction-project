import pandas as pd

def load_telco_data(path="data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"):
    """
    Loads the Telco churn data from a CSV file and performs
    a basic cleaning step on the 'TotalCharges' column.
    """
    df = pd.read_csv(path)

    # The 'TotalCharges' column has some empty spaces.
    # This line converts it to a number and puts 'NaN' for invalid values.
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # This line removes the few rows that had empty charges.
    df.dropna(inplace=True)

    return df