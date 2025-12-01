"""
COVID-19 and Population Data Merging with Country Name Standardization

This script merges COVID-19 case data with world population statistics by standardizing
country names across both datasets to ensure proper matching.

Process:
    1. Load COVID-19 cases and population data
    2. Standardize column names
    3. Apply country name corrections for consistency
    4. Merge datasets using inner join on 'Country'
    5. Export merged dataset

Input:
    - data/world_population.csv: World population statistics
    - data/countries-aggregated.csv: Daily COVID-19 cases

Output:
    - data/merged_covid_population.csv: Merged dataset with COVID-19 and population data

"""

import pandas as pd
from pathlib import Path

# Define paths to the input CSV data files
population_path = Path('../data/world_population.csv')
covid_csv = Path('../data/countries-aggregated.csv')

# Load the CSV files into pandas DataFrames
population_df = pd.read_csv(population_path)
covid_df = pd.read_csv(covid_csv)

# Rename the 'Country/Territory' column to 'Country' for consistency
population_df.rename(columns={'Country/Territory': 'Country'}, inplace=True)

# Create a dictionary mapping country name variations to standardized names
# This ensures proper matching between datasets that use different naming conventions
corrections = {
    'US': 'United States',
    'Korea, South': 'South Korea',
    'Burma': 'Myanmar',
    'Czechia': 'Czech Republic',
    'Taiwan*': 'Taiwan',
    "Cote d'Ivoire": 'Ivory Coast',
    'Congo (Brazzaville)': 'Republic of the Congo',
    'Congo (Kinshasa)': 'DR Congo',
    'West Bank and Gaza': 'Palestine',
    'Cape Verde': 'Cabo Verde'
}

# Apply country name corrections to both DataFrames
# .map() replaces matching values, .fillna() keeps original values for non-matches
covid_df['Country'] = covid_df['Country'].map(corrections).fillna(covid_df['Country'])
population_df['Country'] = population_df['Country'].map(corrections).fillna(population_df['Country'])

# Merge the DataFrames on the 'Country' column using an inner join
# Inner join keeps only countries present in both datasets
# Only select 'Country' and '2022 Population' columns from population_df to avoid redundant data
merged_df = pd.merge(covid_df, population_df[['Country', '2022 Population']], on='Country', how='inner')

# Export the merged DataFrame to a CSV file for further analysis
# index=False prevents pandas from writing row numbers to the CSV
output_path = Path('../data/merged_covid_population.csv')
output_path.parent.mkdir(parents=True, exist_ok=True)
merged_df.to_csv(output_path, index=False)