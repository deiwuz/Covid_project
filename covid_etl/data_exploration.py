"""
COVID-19 and Population Data - Initial Exploration (Refactored)

This module provides functions to interactively load and explore COVID-19 and population datasets.
It allows users to select CSV files from the data directory and displays summary statistics
for validation before further processing.

Functions:
    data_selection: Interactive CSV file selection interface
    load_data: Load selected CSV files into pandas DataFrames
    display_data_summary: Display dataset statistics and preview
    explore_data: Main orchestration function combining all steps

Module Design:
    - Reusable function-based design for integration into larger pipelines
    - Interactive user input for flexible file selection
    - Built-in validation and error handling
    - Can be run standalone or imported as a module
"""

import pandas as pd
from pathlib import Path
from typing import Tuple

working_dir = Path(__file__).parent.parent / 'data'

def data_selection(user: str) -> str:
    """
    Allows the user to select population and COVID data CSV files from the working directory.

    Args:
        user (str): The name of the user.

    Returns:
        Tuple[str, str]: Paths to the selected population data and COVID data CSV files.
    """

    # Generate dictionary of CSV files in the working directory
    possible_csvs = {}
    
    # List all CSV files in the working directory
    csvs_list = [ i for i in list(working_dir.iterdir()) if i.suffix == '.csv' ]
    for i in range(len(csvs_list)):
        csvs_list[i] = str(csvs_list[i])
        possible_csvs.update({i:csvs_list[i]})
    
    
    while True:
        for i in possible_csvs:
            print(f"{i}: {possible_csvs[i]}")
        
        try:
            population_data = input(f"\nHi {user}, please select the population data by entering the corresponding number: ")
            print(f"\n You have selected: {possible_csvs[int(population_data)]}")

            covid_data = input(f"\nHi {user}, please select the covid data by entering the corresponding number: ")
            print(f"\n You have selected: {possible_csvs[int(covid_data)]}")
            # Assign selected file paths
            population_data_dir = possible_csvs[int(population_data)]
            covid_data_dir = possible_csvs[int(covid_data)]
            
            break
        except (ValueError, KeyError):
            print("\n Invalid selection. Please enter a valid number from the list.")
            continue

    return population_data_dir, covid_data_dir

def load_data(population_data_dir: str = None, covid_data_dir: str = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load population and COVID-19 data from CSV files into pandas DataFrames.

    Args:
        population_data_dir (str): File path to population data CSV
        covid_data_dir (str): File path to COVID-19 data CSV

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Population DataFrame and COVID-19 DataFrame

    Raises:
        FileNotFoundError: If either specified file does not exist
    """
    population_data = Path(population_data_dir)
    covid_data = Path(covid_data_dir)

    if not population_data.exists():
        raise FileNotFoundError(f"Population data not found: {population_data}")
    if not covid_data.exists():
        raise FileNotFoundError(f"COVID data not found: {covid_data}")

    population_df = pd.read_csv(population_data)
    covid_df = pd.read_csv(covid_data)

    return population_df, covid_df


def display_data_summary(population_data: pd.DataFrame, covid_data: pd.DataFrame) -> None:
    """
    Display summary information about the datasets.

    Args:
        population_data (pd.DataFrame): DataFrame containing population data.
        covid_data (pd.DataFrame): DataFrame containing COVID-19 data.
    """
    print("=== Population Data ===")
    print(f"Shape: {population_data.shape}")
    print(population_data.head())

    print("\n=== COVID Data ===")
    print(f"Shape: {covid_data.shape}")
    print(covid_data.head())

    print("\n=== Data Info ===")
    print(f"Countries in population data: {population_data['Country/Territory'].nunique()}")
    print(f"Countries in COVID data: {covid_data['Country'].nunique()}")


def explore_data(user: str = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Main function to explore COVID-19 and population data.

    Orchestrates the complete data exploration workflow by calling data_selection,
    load_data, and display_data_summary in sequence. This function provides an
    interactive interface for users to select and preview datasets.

    Args:
        user (str, optional): Name of the user for personalized prompts.
                Defaults to None.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Tuple containing:
            - population_df: DataFrame with population data
            - covid_df: DataFrame with COVID-19 case data

    Raises:
        FileNotFoundError: If selected data files do not exist
        ValueError: If invalid file selection is made
    """
    population_data, covid_data = data_selection(user)
    population_data, covid_data = load_data(population_data, covid_data)
    display_data_summary(population_data, covid_data)

    return population_data, covid_data


# Script mode: if run directly, execute exploration
if __name__ == "__main__":
    print("Running data exploration module in standalone mode...")
    explore_data()