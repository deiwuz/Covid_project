import pandas as pd
from pathlib import Path

# Load the CSV files

population_path = Path('zero-math-week3/data/world_population.csv')
Covid_csv = Path('zero-math-week3/data/countries-aggregated.csv')

# create the Dataframes

population_df = pd.read_csv(population_path)
covid_df = pd.read_csv(Covid_csv)

# Display the first few rows of each DataFrame  
print(population_df.head())
print(covid_df.head())
