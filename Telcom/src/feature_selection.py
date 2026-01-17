import pandas as pd
from src.config import DATA_PROCESSED

def tenure_bucket(t: int) -> str:
    if t <= 6:
        return "0-6"
    elif t <= 12:
        return "7-12"
    elif t <= 24:
        return "1-2 years"
    return "2+ years"

def main():
    df = pd.read_csv(DATA_PROCESSED / "Telecom_churn_cleaned.csv")

    df["tenure_bucket"] = df["tenure"].apply(tenure_bucket)

    service_cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                    "TechSupport", "StreamingTV", "StreamingMovies"]
    
    df["services_count"] = df[service_cols].apply(lambda x: (x == "Yes").sum(), axis=1)

    # Create high_value_customer feature
    df["high_value_customer"] = (df["MonthlyCharges"] > df["MonthlyCharges"].median()).astype(int)

    #Risk flag
    df["contract_risk_flag"] = (df["Contract"] == "Month-to-month").astype(int)
    df["payment_risk_flag"] = (df["PaymentMethod"] == "Electronic check").astype(int)

    # Save the updated dataframe
    output_path = DATA_PROCESSED / "Telecom_churn_features.csv"
    df.to_csv(output_path, index=False)

    print(f" Feature engineered data saved to: {output_path}")
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()
