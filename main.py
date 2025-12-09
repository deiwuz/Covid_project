"""
COVID-19 ETL Pipeline - Main Entry Point

This script orchestrates the complete COVID-19 data analysis pipeline, from data loading
through visualization. It processes COVID-19 case data and population statistics to calculate
and visualize infection rates per capita across countries.

Pipeline Steps:
    1. Data Exploration: Load and validate COVID-19 and population datasets
    2. Data Merging: Standardize country names and merge datasets
    3. Per Capita Calculation: Calculate cases per 100,000 inhabitants
    4. Visualization: Generate bar chart of top countries by infection rate

Usage:
    python main.py

    or with uv:
    uv run python main.py

Dependencies:
    - pandas: Data manipulation and analysis
    - matplotlib: Plotting and visualization
    - seaborn: Statistical data visualization
    - pathlib: File path handling

Input Files (selected interactively):
    - Population data CSV (e.g., world_population.csv)
    - COVID-19 cases data CSV (e.g., time_series_covid_19_confirmed.csv)

Output Files:
    - data/merged_covid_population.csv: Merged dataset
    - data/covid_cases_per_100k.csv: Per capita analysis results
    - plots/covid_cases_per_100k_barplot.png: Visualization

Author: Deiwuz 
Version: 0.1.0
"""

from covid_etl import explore_data, merging_datasets, calculate_per_capita, visualize_results


def main():
    """
    Execute the complete COVID-19 ETL pipeline.

    This function runs all four steps of the pipeline sequentially:
    data exploration, merging, per capita calculation, and visualization.
    User interaction is required for dataset selection.

    Returns:
        None

    Raises:
        FileNotFoundError: If selected data files do not exist
        ValueError: If data format is invalid or country columns are missing
        KeyError: If required columns are not found in the datasets
    """
    print("="*60)
    print("Welcome to your COVID-19 ETL Pipeline!")
    print("="*60)

    user = input("\nEnter your name: ")

    # Step 1: Explore and load data
    print("\n" + "="*60)
    print("STEP 1: Data Exploration")
    print("="*60)
    population_df, covid_df = explore_data(user)

    # Step 2: Merge datasets
    print("\n" + "="*60)
    print("STEP 2: Merging Datasets")
    print("="*60)
    merged_df = merging_datasets(population_df, covid_df, False)

    # Step 3: Calculate per capita statistics
    print("\n" + "="*60)
    print("STEP 3: Calculating Cases per 100k Population")
    print("="*60)
    per_capita_df = calculate_per_capita(merged_df)

    # Step 4: Create visualization
    print("\n" + "="*60)
    print("STEP 4: Creating Visualization")
    print("="*60)
    visualization_path = visualize_results(per_capita_df, top_n=10)

    # Summary
    print("\n" + "="*60)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)
    print(f"Merged dataframe shape: {merged_df.shape}")
    print(f"Countries analyzed: {len(per_capita_df)}")
    print(f"Visualization saved to: {visualization_path}")
    print("\nThank you for using the COVID-19 ETL Pipeline!")


if __name__ == "__main__":
    main()