import pandas as pd

# Load data
df = pd.read_csv("data/raw/hdfc_top100_nav.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Sort by date
df = df.sort_values("date")

# Remove duplicates
df = df.drop_duplicates()

# Ensure nav is numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Forward-fill missing NAV values
df["nav"] = df["nav"].ffill()

# Save cleaned file
df.to_csv("data/processed/hdfc_top100_nav_clean.csv", index=False)

print("Cleaning completed successfully!")
print("Total rows:", len(df))