"""Sales EDA portfolio project.
Run with: python sales_eda.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path("../excel-sales-analysis/data/sales_data.csv")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])
df["Sales"] = df["Quantity"] * df["Unit_Price"]
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("=== Sales EDA ===")
print(f"Rows: {len(df)}")
print(f"Total sales: {df['Sales'].sum():,.2f}")
print(f"Orders: {df['Order_ID'].nunique():,}")
print(f"Quantity: {df['Quantity'].sum():,}")
print(f"Average order value: {df['Sales'].mean():,.2f}")
print("\nMissing values:\n", df.isna().sum())
print("\nSales by region:\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\nSales by category:\n", df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

monthly = df.groupby("Month", as_index=False)["Sales"].sum()
monthly.plot(x="Month", y="Sales", kind="line", marker="o", legend=False)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "monthly_sales.png", dpi=160)
plt.close()

region = df.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
region.plot(x="Region", y="Sales", kind="bar", legend=False)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "sales_by_region.png", dpi=160)
plt.close()

print(f"\nCharts saved to {OUT}/")
