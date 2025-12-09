"""
COVID-19 Cases per 100k Population - Visualization (Refactored)

This module generates publication-quality visualizations of COVID-19 infection rates
per capita. It creates horizontal bar charts to display countries ranked by their
infection rates, using accessible color schemes and clear formatting.

Visualization Design:
    - Horizontal bar orientation for improved country name readability
    - Viridis color palette for colorblind-friendly gradients
    - Configurable number of top countries to display
    - Tight layout to prevent label cutoff
    - High-resolution PNG output suitable for reports and presentations

Process:
    1. Load pre-calculated cases per 100k data
    2. Select top N countries by infection rate
    3. Create horizontal bar chart with color gradient
    4. Apply formatting and labels
    5. Save visualization as PNG file

Functions:
    visualize_results: Generate and save bar chart visualization

Output Files:
    plots/covid_cases_per_100k_barplot.png: Bar chart visualization

Dependencies:
    - matplotlib: Core plotting functionality
    - seaborn: Enhanced statistical visualizations
    - pandas: Data manipulation
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_results(per_capita_df: pd.DataFrame, top_n: int = 10) -> Path:
    """
    Create a horizontal bar chart visualizing countries with highest COVID-19 infection rates.

    This function generates a publication-quality horizontal bar chart showing the top N
    countries ranked by COVID-19 cases per 100,000 inhabitants. The visualization uses
    the Viridis color palette for accessibility and includes proper labels and formatting.

    Args:
        per_capita_df (pd.DataFrame): DataFrame with infection rate data.
            Required columns:
            - 'Cases_per_100k': Normalized infection rate
            - 'Country': Country name
            Data should be pre-sorted by Cases_per_100k (descending)
        top_n (int, optional): Number of top countries to display. Defaults to 10.
            Must be positive and not exceed DataFrame length.

    Returns:
        Path: Absolute path to the saved visualization file (PNG format)

    Output Files:
        plots/covid_cases_per_100k_barplot.png: The generated bar chart

    Visualization Settings:
        - Figure size: 14 x 6 inches
        - Color palette: Viridis (colorblind-friendly)
        - Format: PNG with tight layout
        - DPI: Matplotlib default (typically 100)

    Example:
        >>> df = pd.read_csv('data/covid_cases_per_100k.csv')
        >>> plot_path = visualize_results(df, top_n=15)
        >>> print(f"Visualization saved to: {plot_path}")
    """
    # Define path for output visualization
    covid_19_barplot_path = Path('plots/covid_cases_per_100k_barplot.png')

    # Create directories if they don't exist
    # parents=True creates parent directories if needed
    # exist_ok=True prevents errors if directory already exists
    covid_19_barplot_path.parent.mkdir(parents=True, exist_ok=True)

    # Select the top N countries with the highest infection rates
    # Data should already be sorted in descending order
    top_countries = per_capita_df.head(top_n)

    # Create a figure with specified size (width=14 inches, height=6 inches)
    plt.figure(figsize=(14, 6))

    # Create horizontal bar plot using seaborn
    # x='Cases_per_100k': values determine bar length
    # y='Country': country names on y-axis
    # hue='Country': assigns different colors to each country
    # palette='viridis': uses colorblind-friendly color gradient
    # legend=False: hides legend (redundant since country names are on y-axis)
    sns.barplot(x='Cases_per_100k', y='Country', data=top_countries, hue='Country', palette='viridis', legend=False)

    # Add descriptive axis label
    plt.xlabel('Cases per 100,000 Inhabitants')

    # Add chart title
    plt.title(f'Top {top_n} Countries with Highest COVID-19 Cases per 100,000 Inhabitants')

    # Adjust layout to prevent labels from being cut off
    plt.tight_layout()

    # Save the figure as PNG file
    plt.savefig(covid_19_barplot_path)

    # Close the plot to free memory
    plt.close()

    print(f"\nVisualization saved to: {covid_19_barplot_path}")
    print(f"Top country: {top_countries.iloc[0]['Country']} with {top_countries.iloc[0]['Cases_per_100k']:.2f} cases per 100k")

    return covid_19_barplot_path


# Script mode: if run directly, load from CSV and create visualization
if __name__ == "__main__":
    print("Running visualization module in standalone mode...")

    # Define path for input data
    covid_19_path = Path('../data/covid_cases_per_100k.csv')

    # Read the pre-calculated COVID-19 cases per 100k data
    covid_19_df = pd.read_csv(covid_19_path)

    # Create visualization
    output_path = visualize_results(covid_19_df, top_n=10)

    print(f"\nVisualization complete! Open {output_path} to view the chart.")