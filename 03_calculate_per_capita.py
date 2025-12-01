"""
COVID-19 Cases per 100k Population Analysis

This script analyzes merged COVID-19 and population data to calculate infection rates
per 100,000 inhabitants for each country, using only the most recent data available.

Process:
    1. Load merged COVID-19 and population data
    2. Convert dates to datetime format
    3. Calculate cases per 100,000 inhabitants
    4. Filter to keep only the latest date for each country
    5. Sort by infection rate (descending)
    6. Export results

Input:
    - zero-math-week3/data/merged_covid_population.csv: Merged COVID-19 and population data

Output:
    - zero-math-week3/data/covid_cases_per_100k.csv: Countries ranked by infection rate

Key Metric:
    - Cases_per_100k: (Confirmed cases / Population) * 100,000
    - This normalizes infection data by population size for fair comparison

Author: Zero Math Week 3 - Day 20
"""

import pandas as pd
from pathlib import Path

# Define path to the merged COVID-19 and population dataset
merged_covid_population_path = Path('zero-math-week3/data/merged_covid_population.csv')

# Read the CSV file into a DataFrame
covid_19_df = pd.read_csv(merged_covid_population_path)

# Convert the 'Date' column to datetime format for proper date handling and filtering
covid_19_df['Date'] = pd.to_datetime(covid_19_df['Date'], format='%Y-%m-%d')

# Calculate confirmed cases per 100,000 inhabitants for each row
# Formula: (Confirmed cases / Total population) * 100,000
# This normalizes case counts by population size, enabling fair comparison between countries
# Round to 2 decimal places for readability
covid_19_df['Cases_per_100k'] = ((covid_19_df['Confirmed'] / covid_19_df['2022 Population']) * 100000).round(2)

# Filter to keep only the most recent date for each country
# groupby('Country')['Date'].idxmax() returns the index of the row with the maximum date for each country
# .loc[] then selects those specific rows
# This ensures we're comparing the latest available data for all countries
covid_19_df = covid_19_df.loc[
    covid_19_df.groupby('Country')['Date'].idxmax()
]

# Sort countries in descending order by cases per 100k population
# Countries with highest infection rates relative to population appear first
covid_19_df = covid_19_df.sort_values(by='Cases_per_100k', ascending=False)

# Save the resulting DataFrame to a new CSV file for visualization and reporting
output_path = Path('zero-math-week3/data/covid_cases_per_100k.csv')
covid_19_df.to_csv(output_path, index=False)

print(f"Analysis complete. Results saved to {output_path}")
print(f"Total countries analyzed: {len(covid_19_df)}")
