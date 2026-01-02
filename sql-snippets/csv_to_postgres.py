"""
Script to load CSV data into a local PostgreSQL database.
 Reads 'country_summary.csv' from the data directory and loads it into
 a Postgres table named 'country_summary'.
 Ensure your local Postgres credentials match the `db_url` configuration.
"""
from sqlalchemy import create_engine
from pathlib import Path
import pandas as pd

db_url = 'postgresql+psycopg2://postgres:pass@localhost:5432/postgres'

engine = create_engine(db_url)

data_path = Path('../data/country_summary.csv')

df = pd.read_csv(data_path)

df.to_sql('country_summary', engine, if_exists='append', index=False)