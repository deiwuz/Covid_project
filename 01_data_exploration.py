"""
COVID-19 and Population Data - Initial Exploration

This script loads and displays initial data from COVID-19 cases and world population datasets
to understand the structure and contents before merging.

Input:
    - zero-math-week3/data/world_population.csv: World population statistics by country
    - zero-math-week3/data/countries-aggregated.csv: Daily COVID-19 case data by country

Output:
    - Console display of first 5 rows of each dataset

Author: Zero Math Week 3 - Day 18
"""

import pandas as pd
from pathlib import Path

# Define paths to the CSV data files
population_path = Path('zero-math-week3/data/world_population.csv')
covid_csv = Path('zero-math-week3/data/countries-aggregated.csv')

# Load the CSV files into pandas DataFrames
population_df = pd.read_csv(population_path)
covid_df = pd.read_csv(covid_csv)

# Display the first few rows of each DataFrame to understand structure and content
print("=== World Population Data ===")
print(population_df.head())
print("\n=== COVID-19 Cases Data ===")
print(covid_df.head())
