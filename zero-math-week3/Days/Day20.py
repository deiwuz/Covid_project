import pandas as pd
from pathlib import Path
from datetime import datetime

# Load the CSV files

merged_covid_population_path = Path('zero-math-week3/data/merged_covid_population.csv')

# create the Dataframe
covid_19_df = pd.read_csv(merged_covid_population_path)

# Convert the 'Date' column to datetime format and then to 'YYYY-MM' format
covid_19_df['Date'] = pd.to_datetime(covid_19_df['Date'], format='%Y-%m-%d').dt.strftime('%Y-%m')

# Group by 'Date' and 'Country', erasing the daily data to have monthly data
covid_19_df = covid_19_df.groupby(['Country', 'Date']).sum().reset_index()

print(covid_19_df.head(1000).to_string())

