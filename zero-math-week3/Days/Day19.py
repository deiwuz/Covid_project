import pandas as pd
from pathlib import Path

# Load the CSV files

population_path = Path('zero-math-week3/data/world_population.csv')
Covid_csv = Path('zero-math-week3/data/countries-aggregated.csv')

# create the Dataframes

population_df = pd.read_csv(population_path)
covid_df = pd.read_csv(Covid_csv)

print(covid_df)

# Rename the 'Country Name' column to 'Country' in population_df
population_df.rename(columns={'Country/Territory': 'Country'}, inplace=True)

# Create a dictionary for known discrepancies between country names
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

# Apply the corrections to the 'Country' column in covid_df
covid_df['Country'] = covid_df['Country'].map(corrections).fillna(covid_df['Country'])
population_df['Country'] = population_df['Country'].map(corrections).fillna(population_df['Country'])

# merge the DataFrames on the 'Country' column using an inner join
merged_df = pd.merge(covid_df, population_df[['Country', '2022 Population', '2000 Population']], on='Country', how='inner')


merged_df.to_csv('zero-math-week3/data/merged_covid_population.csv', index=False)