"""Synthetic manufacturing KPI analysis."""
import pandas as pd

DATA = "data/manufacturing_data.csv"
df = pd.read_csv(DATA)

df["Achievement_Pct"] = 100 * df["Units_Produced"] / df["Production_Target"]
df["Defect_Rate_Pct"] = 100 * df["Defects"] / df["Units_Produced"]
df["Good_Units"] = df["Units_Produced"] - df["Defects"]

summary = df.groupby("Machine").agg(
    Target=("Production_Target", "sum"),
    Produced=("Units_Produced", "sum"),
    Defects=("Defects", "sum"),
    Downtime_Minutes=("Downtime_Minutes", "sum"),
    Good_Units=("Good_Units", "sum"),
)
summary["Achievement_Pct"] = 100 * summary["Produced"] / summary["Target"]
summary["Defect_Rate_Pct"] = 100 * summary["Defects"] / summary["Produced"]

print(summary.round(2))
