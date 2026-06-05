import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

df = pd.read_csv("data/processed/hdfc_top100_nav_clean.csv")

df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")