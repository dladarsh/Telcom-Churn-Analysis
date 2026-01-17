from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = PROJECT_ROOT / "data" / "raw" / "Telco_Cusomer_Churn.csv"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS = PROJECT_ROOT / "outputs"
for p in [DATA_PROCESSED, OUTPUTS]:
    p.mkdir(parents=True, exist_ok=True)