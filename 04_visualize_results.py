"""
COVID-19 Cases per 100k Population - Visualization

This script creates a horizontal bar chart visualizing the top 10 countries
with the highest COVID-19 infection rates per 100,000 inhabitants.

Process:
    1. Load pre-calculated cases per 100k data
    2. Select top 10 countries by infection rate
    3. Create horizontal bar chart with color gradient
    4. Save visualization as PNG

Input:
    - data/covid_cases_per_100k.csv: Countries ranked by infection rate

Output:
    - plots/covid_cases_per_100k_barplot.png: Bar chart visualization

Visualization Features:
    - Horizontal bars for better country name readability
    - Viridis color palette (colorblind-friendly gradient)
    - Tight layout to prevent label cutoff

Author: Zero Math Week 3 - Day 21
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Define paths for input data and output visualization
covid_19_path = Path('data/covid_cases_per_100k.csv')
covid_19_barplot_path = Path('plots/covid_cases_per_100k_barplot.png')

# Create directories if they don't exist
# parents=True creates parent directories if needed
# exist_ok=True prevents errors if directory already exists
covid_19_barplot_path.parent.mkdir(parents=True, exist_ok=True)
covid_19_path.parent.mkdir(parents=True, exist_ok=True)

# Read the pre-calculated COVID-19 cases per 100k data
covid_19_df = pd.read_csv(covid_19_path)

# Select the top 10 countries with the highest infection rates
# Data is already sorted in descending order from Day20.py
top_10_countries = covid_19_df.head(10)

# Create a figure with specified size (width=14 inches, height=6 inches)
plt.figure(figsize=(14, 6))

# Create horizontal bar plot using seaborn
# x='Cases_per_100k': values determine bar length
# y='Country': country names on y-axis
# hue='Country': assigns different colors to each country
# palette='viridis': uses colorblind-friendly color gradient
# legend=False: hides legend (redundant since country names are on y-axis)
sns.barplot(x='Cases_per_100k', y='Country', data=top_10_countries, hue='Country', palette='viridis', legend=False)

# Add descriptive axis label
plt.xlabel('Cases per 100,000 Inhabitants')

# Add chart title
plt.title('Top 10 Countries with Highest COVID-19 Cases per 100,000 Inhabitants')

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save the figure as PNG file
plt.savefig(covid_19_barplot_path)

print(f"Visualization saved to {covid_19_barplot_path}")
print(f"Top country: {top_10_countries.iloc[0]['Country']} with {top_10_countries.iloc[0]['Cases_per_100k']:.2f} cases per 100k")