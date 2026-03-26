import pandas as pd


def load_sample_data(path: str = "data/sample_pocs.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_kpis(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "total_pocs": 0,
            "avg_score": 0.0,
            "go_count": 0,
            "high_risk_count": 0,
        }

    return {
        "total_pocs": int(len(df)),
        "avg_score": round(float(df["final_score"].mean()), 2),
        "go_count": int((df["recommendation"] == "GO").sum()),
        "high_risk_count": int((df["risk_level"] >= 4).sum()),
    }
