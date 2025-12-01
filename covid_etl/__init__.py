"""
COVID-19 ETL Pipeline

This package provides a complete ETL pipeline for analyzing COVID-19 cases
per capita across countries.

Modules:
    01_data_exploration: Initial data exploration and validation
    02_data_merging: Merge COVID-19 and population datasets
    03_calculate_per_capita: Calculate cases per 100k population
    04_visualize_results: Create visualizations of the analysis

Usage:
    # Run individual steps
    from covid_etl import data_exploration, data_merging

    # Or import specific functionality (when we refactor to use functions)
"""

__version__ = "0.1.0"

# Import functions from modules to make them available at package level
from .data_exploration import explore_data, load_data, display_data_summary

# When you add functions to other modules, you can expose them here like:
# from .data_merging import merge_datasets
# from .calculate_per_capita import calculate_per_capita
# from .visualize_results import create_visualization

__all__ = [
    # List what should be available when someone does: from covid_etl import *
    'explore_data',
    'load_data',
    'display_data_summary',
]
