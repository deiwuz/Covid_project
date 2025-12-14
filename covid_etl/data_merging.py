"""
COVID-19 and Population Data - Dataset Merging

This module handles the merging of COVID-19 case data with population statistics.
It includes country name standardization to ensure successful joins between datasets
that may use different naming conventions.

Functions:
    column_standardization: Interactive column renaming to 'Country'
    data_standarization: Apply country name corrections for consistent naming
    merging_datasets: Main function to merge COVID-19 and population datasets

Country Name Mapping:
    The module includes a predefined mapping dictionary to standardize country names
    between different data sources (e.g., 'US' -> 'United States').

Output:
    Merged dataset saved to: data/merged_covid_population.csv
"""

import pandas as pd
from pathlib import Path
from typing import Tuple

# Country name corrections to standardize naming across different data sources
# Maps variant country names to their standardized equivalents
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

def column_standardization(population_df: pd.DataFrame, covid_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Interactively rename a column to 'Country' in one of the DataFrames.

    This function is called when the 'Country' column is not found in one or both
    DataFrames. It allows the user to select which DataFrame to modify and which
    column to rename to 'Country'.

    Args:
        population_df (pd.DataFrame): DataFrame containing population data
        covid_df (pd.DataFrame): DataFrame containing COVID-19 data

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames with standardized column names

    Note:
        After column renaming, this function calls data_standarization to apply
        country name corrections.
    """
    working_dataframes = {1: population_df, 2: covid_df}
    while True:

        for key, df in working_dataframes.items():
            print(f"Dataframe {key}, {df.head(1)}")
        
        try:
            dataframe_choice = int(input("Select the number of the dataframe to standardize columns: "))
            if dataframe_choice not in working_dataframes:
                print("Invalid choice. Please select a valid dataframe number.")
                continue

            print(working_dataframes[dataframe_choice].columns)

            column_name = input("Enter the column name to standardize: ")
            if column_name not in working_dataframes[dataframe_choice].columns:
                print("Column not found. Please enter a valid column name.")
                continue

            working_dataframes[dataframe_choice].rename(columns={column_name: 'Country'}, inplace=True)
            print(f"Column '{column_name}' standardized to 'Country' in dataframe {dataframe_choice}.")

            return data_standarization(working_dataframes[1], working_dataframes[2])
        
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the dataframe.")


def data_standarization(population_df: pd.DataFrame, covid_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Standardize country names across both DataFrames using predefined corrections.

    This function applies the corrections dictionary to map variant country names
    to their standardized equivalents in both the population and COVID-19 DataFrames.
    If the 'Country' column is missing from either DataFrame, it triggers interactive
    column standardization.

    Args:
        population_df (pd.DataFrame): DataFrame containing population data
        covid_df (pd.DataFrame): DataFrame containing COVID-19 data

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames with standardized country names

    Note:
        The corrections dictionary is defined at module level and contains mappings
        such as 'US' -> 'United States', 'Czechia' -> 'Czech Republic', etc.
    """
    print('-' * 20)
    print("Standardizing country names across datasets...")
    print('-' * 20)

    # Auto-detect and rename country columns
    common_aliases = ['Country/Territory', 'Country Name', 'Region', 'Nation']
    
    for df in [population_df, covid_df]:
        if 'Country' not in df.columns:
            for alias in common_aliases:
                if alias in df.columns:
                    df.rename(columns={alias: 'Country'}, inplace=True)
                    print(f"Automatically standardized column '{alias}' to 'Country'")
                    break

    if 'Country' not in population_df.columns or 'Country' not in covid_df.columns:
        print("DataFrames must contain 'Country' column for standardization.\n\ninitializing column standardization...")
        column_standardization(population_df, covid_df)

    population_df['Country'] = population_df['Country'].map(corrections).fillna(population_df['Country'])
    covid_df['Country'] = covid_df['Country'].map(corrections).fillna(covid_df['Country'])

    return population_df, covid_df

def merging_datasets(population_df: pd.DataFrame, covid_df: pd.DataFrame, estandarized: bool = False) -> pd.DataFrame:
    """
    Merge COVID-19 case data with world population statistics.

    This function performs country name standardization (unless already done) and then
    merges the two datasets on the 'Country' column. The merged result is saved to a
    CSV file for further analysis. Only the '2022 Population' column from the population
    data is included in the merge.

    Args:
        population_df (pd.DataFrame): DataFrame containing population data.
            Must have 'Country' and '2022 Population' columns.
        covid_df (pd.DataFrame): DataFrame containing COVID-19 data.
            Must have 'Country' column.
        estandarized (bool, optional): If True, skips country name standardization.
            Defaults to False.

    Returns:
        pd.DataFrame: Merged DataFrame containing COVID-19 data with population information

    Output Files:
        data/merged_covid_population.csv: The merged dataset

    Note:
        The merge is an inner join, so only countries present in both datasets
        will appear in the final result.
    """
    if not estandarized:
        population_df, covid_df = data_standarization(population_df, covid_df) 

    # Merge datasets on 'Country' column
    merged_df = pd.merge(covid_df, population_df[['Country', '2022 Population']], on='Country', how='inner')

    # Save to CSV with correct path
    output_path = Path('data/merged_covid_population.csv')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    merged_df.to_csv(output_path, index=False)

    print(f"Merged dataset saved to: {output_path}")
    print(f"Total rows merged: {len(merged_df)}")

    return merged_df