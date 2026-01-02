"""
COVID-19 Cases per 100k Population Analysis (Refactored)

This module calculates normalized COVID-19 infection rates to enable fair comparisons
between countries of different population sizes. It processes merged COVID-19 and
population data to compute cases per 100,000 inhabitants.

Key Metric:
    Cases_per_100k = (Confirmed cases / Population) * 100,000

This normalization allows for meaningful comparisons between countries. For example,
a small country with 1,000 cases and a population of 100,000 has the same infection
rate (1,000 per 100k) as a large country with 1,000,000 cases and 100,000,000 people.

Process:
    1. Load merged COVID-19 and population data
    2. Convert dates to datetime format for proper temporal handling
    3. Calculate cases per 100,000 inhabitants using the formula above
    4. Filter to keep only the latest date for each country (most recent data)
    5. Sort countries by infection rate in descending order
    6. Export results to CSV for visualization and reporting

Functions:
    calculate_per_capita: Main function to compute per capita infection rates

Output Files:
    data/covid_cases_per_100k.csv: Countries ranked by infection rate with full data
"""

import pandas as pd
from pathlib import Path


def calculate_per_capita(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate COVID-19 cases per 100,000 inhabitants for each country.

    This function normalizes COVID-19 case counts by population size, allowing for
    fair comparisons between countries. It processes time-series data and retains
    only the most recent statistics for each country.

    The calculation formula is:
        Cases_per_100k = (Confirmed / Population) * 100,000

    Args:
        merged_df (pd.DataFrame): DataFrame containing merged COVID-19 and population data.
            Required columns:
            - 'Date': Date of observation (will be converted to datetime)
            - 'Confirmed': Total confirmed COVID-19 cases
            - '2022 Population': Country population from 2022
            - 'Country': Country name

    Returns:
        pd.DataFrame: Processed DataFrame with:
            - All original columns
            - New 'Cases_per_100k' column (rounded to 2 decimal places)
            - One row per country (most recent date only)
            - Sorted by Cases_per_100k in descending order

    Output Files:
        Saves results to: data/covid_cases_per_100k.csv

    Example:
        >>> merged_df = pd.read_csv('data/merged_covid_population.csv')
        >>> result_df = calculate_per_capita(merged_df)
        >>> print(result_df[['Country', 'Cases_per_100k']].head())
    """
    # Create a copy to avoid modifying the original DataFrame
    covid_19_df = merged_df.copy()

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
    output_path = Path('data/covid_cases_per_100k.csv')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    covid_19_df.to_csv(output_path, index=False)

    print(f"\nAnalysis complete. Results saved to: {output_path}")
    print(f"Total countries analyzed: {len(covid_19_df)}")
    print(f"Top country: {covid_19_df.iloc[0]['Country']} with {covid_19_df.iloc[0]['Cases_per_100k']:.2f} cases per 100k")

    return covid_19_df


# Script mode: if run directly, load from CSV and execute calculation
if __name__ == "__main__":
    print("Running per capita calculation module in standalone mode...")

    # Define path to the merged COVID-19 and population dataset
    merged_covid_population_path = Path('../data/merged_covid_population.csv')

    # Read the CSV file into a DataFrame
    merged_df = pd.read_csv(merged_covid_population_path)

    # Calculate per capita statistics
    result_df = calculate_per_capita(merged_df)

    print(f"\nTop 5 countries by infection rate:")
    print(result_df[['Country', 'Cases_per_100k']].head())
