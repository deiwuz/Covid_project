"""
COVID-19 and Population Data - Initial Exploration (Refactored)

This module provides functions to load and explore COVID-19 and population data.
Unlike the script version (01_data_exploration.py), this version exports reusable functions.
"""

import pandas as pd
from pathlib import Path
from typing import Tuple


def load_data(data_dir: Path = Path('../data')) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load COVID-19 and population datasets.

    Args:
         data_dir: Path to the directory containing data files


    Returns:
        Tuple of (population_df, covid_df)

    Raises:
        FileNotFoundError: If data files don't exist
    """
    if data_dir is None:
        # Get the project root (parent of the covid_etl directory)
        script_dir = Path(__file__).parent
        data_dir = script_dir.parent / 'data'

    population_path = data_dir / 'world_population.csv'
    covid_path = data_dir / 'countries-aggregated.csv'

    if not population_path.exists():
        raise FileNotFoundError(f"Population data not found: {population_path}")
    if not covid_path.exists():
        raise FileNotFoundError(f"COVID data not found: {covid_path}")

    population_df = pd.read_csv(population_path)
    covid_df = pd.read_csv(covid_path)

    return population_df, covid_df


def display_data_summary(population_df: pd.DataFrame, covid_df: pd.DataFrame) -> None:
    """
    Display summary information about the datasets.

    Args:
        population_df: World population DataFrame
        covid_df: COVID-19 cases DataFrame
    """
    print("=== World Population Data ===")
    print(f"Shape: {population_df.shape}")
    print(population_df.head())

    print("\n=== COVID-19 Cases Data ===")
    print(f"Shape: {covid_df.shape}")
    print(covid_df.head())

    print("\n=== Data Info ===")
    print(f"Countries in population data: {population_df['Country/Territory'].nunique()}")
    print(f"Countries in COVID data: {covid_df['Country'].nunique()}")


def explore_data(data_dir: Path = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Complete exploration workflow: load and display data.

    Args:
        data_dir: Path to the directory containing data files.
                  If None, uses the 'data' directory relative to the project root.

    Returns:
        Tuple of (population_df, covid_df)
    """
    population_df, covid_df = load_data(data_dir)
    display_data_summary(population_df, covid_df)
    return population_df, covid_df


# Script mode: if run directly, execute exploration
if __name__ == "__main__":
    explore_data()
