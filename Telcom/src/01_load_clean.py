import pandas as pd
from src.config import DATA_RAW, DATA_PROCESSED

def main():
    df = pd.read_csv(DATA_RAW)

    # Fix TotalCharges to be numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Convert Yes/No to 1/0 (only true binary columns)
    binary_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0})

    output_path = DATA_PROCESSED / "Telecom_churn_cleaned.csv"
    df.to_csv(output_path, index=False)

    print(f" Cleaned data saved to: {output_path}")
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()
