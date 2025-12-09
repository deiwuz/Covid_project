"""
COVID-19 ETL Pipeline Package

This package provides a complete, modular ETL (Extract, Transform, Load) pipeline for
analyzing COVID-19 infection rates normalized by population. It processes raw COVID-19
case data and population statistics to produce meaningful visualizations and insights.

Pipeline Overview:
    1. Data Exploration: Interactive selection and validation of input datasets
    2. Data Merging: Country name standardization and dataset joining
    3. Per Capita Calculation: Normalize case counts by population (per 100k)
    4. Visualization: Generate publication-quality bar charts

Key Features:
    - Modular design with reusable functions
    - Interactive data file selection
    - Automatic country name standardization
    - Population-normalized infection rate calculations
    - Colorblind-friendly visualizations
    - Both programmatic and CLI interfaces

Modules:
    data_exploration: Interactive data loading and validation
    data_merging: Country name standardization and dataset merging
    calculate_per_capita: Per capita infection rate calculations
    visualize_results: Bar chart visualization generation

Exported Functions:
    explore_data: Load and preview COVID-19 and population datasets
    merging_datasets: Merge datasets with country name standardization
    calculate_per_capita: Calculate cases per 100,000 inhabitants
    visualize_results: Generate bar chart of top countries by infection rate

Usage Examples:
    # Import all pipeline functions
    from covid_etl import (
        explore_data,
        merging_datasets,
        calculate_per_capita,
        visualize_results
    )

    # Run complete pipeline
    population_df, covid_df = explore_data("User")
    merged_df = merging_datasets(population_df, covid_df)
    per_capita_df = calculate_per_capita(merged_df)
    plot_path = visualize_results(per_capita_df, top_n=10)

    # Or use the main.py script for the complete pipeline
    # python main.py

Requirements:
    - pandas >= 1.3.0
    - matplotlib >= 3.3.0
    - seaborn >= 0.11.0
    - pathlib (standard library)

Version: 0.1.0
Author: Data Analysis Team
"""

__version__ = "0.1.0"

# Import functions from modules to make them available at package level
from .data_exploration import explore_data
from .data_merging import merging_datasets
from .calculate_per_capita import calculate_per_capita
from .visualize_results import visualize_results

__all__ = [
    # List what should be available when someone does: from covid_etl import *
    'explore_data',
    'merging_datasets',
    'calculate_per_capita',
    'visualize_results'
]
