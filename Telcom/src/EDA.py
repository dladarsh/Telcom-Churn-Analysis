import pandas as pd

from src.config import DATA_PROCESSED, OUTPUTS

TABLES_DIR = OUTPUTS / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)

def save_table(df, name):
    path=TABLES_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    print(f"Saved -> {path}")


def main():
    df = pd.read_csv(DATA_PROCESSED / "Telecom_churn_features.csv")

    # 1) Overall KPIs
    kpis = pd.DataFrame([{
        "total_customers": len(df),
        "churn_rate": round(df["Churn"].mean(), 3),
        "avg_monthly_charges": round(df["MonthlyCharges"].mean(), 2),
        "avg_tenure_months": round(df["tenure"].mean(), 1)
    }])
    save_table(kpis, "overall_kpis")

    # 2) Churn by Contract Type
    churn_by_contract = (
        df.groupby("Contract", as_index=False).agg(customers=("customerID", "count"), churn_rate=("Churn", "mean")).sort_values("churn_rate", ascending=False)
    )

    save_table(churn_by_contract, "churn_by_contract")

    # 3) Churn by Payment Method
    churn_by_payment = (
        df.groupby("PaymentMethod", as_index=False).agg(customers=("customerID", "count"), churn_rate=("Churn", "mean")).sort_values("churn_rate", ascending=False)
    )

    save_table(churn_by_payment, "churn_by_payment")

    # 4) Churn by Tenure Bucket
    churn_by_tenure = (
        df.groupby("tenure_bucket", as_index=False).agg(customers=("customerID", "count"), churn_rate=("Churn", "mean")).sort_values("churn_rate", ascending=False)
    )

    save_table(churn_by_tenure, "churn_by_tenure")

    # 5) Service count vs churn
    churn_by_service_count = (
        df.groupby("services_count", as_index=False).agg(customers=("customerID", "count"), churn_rate=("Churn", "mean")).sort_values("services_count")
    )
    save_table(churn_by_service_count, "churn_by_service_count")

    # 6) High Value Customers at risk
    high_value_churn = (
        df[df["high_value_customer"] == 1].groupby("contract_risk_flag", as_index=False).agg(customers=("customerID", "count"), churn_rate=("Churn", "mean"))
    )

    save_table(high_value_churn, "high_value_customer_risk")

if __name__ == "__main__":
    main()