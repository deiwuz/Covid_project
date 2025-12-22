# COVID-19 ETL Pipeline

A robust Extract, Transform, Load (ETL) pipeline designed to analyze COVID-19 infection rates normalized by population. This project processes raw COVID-19 case data and population statistics to produce meaningful insights and publication-quality visualizations.

## Features

- **Interactive Data Exploration**: Validates and previews input datasets before processing.
- **Intelligent Merging**: Automatically standardizes country names to ensure accurate data integration across different sources.
- **Per Capita Analysis**: Calculates cases per 100,000 inhabitants to allow fair comparisons between countries of varying sizes.
- **Visualization**: Generates clear, colorblind-friendly horizontal bar charts of the top affected countries.
- **Dockerized**: Fully containerized for consistent execution across different environments.

## Getting Started

### Prerequisites

- **Python 3.14+** (if running locally)
- **Docker & Docker Compose** (for containerized execution)

### Installation

#### Option 1: Docker (Recommended)

Run the entire pipeline in an isolated container without installing dependencies locally.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/deiwuz/Covid_project
    cd Covid_project
    ```

2.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

#### Option 1.1: Quick Run with Docker Run

Alternatively, you can build and run a disposable container manually:

```bash
# 1. Pull the pre-built image (Optional - if you don't want to build locally)
docker pull deiwuz/covid_project:general

# OR Build the image locally
docker build -t covid-project .

# 2. Run container (removes itself after exit to save space)
# Note: Volume mounting (-v) ensures outputs are saved to your local machine

# If you built locally (tag: covid-project):
# On Windows PowerShell:
docker run --rm -it -v ${PWD}/data:/app/data -v ${PWD}/plots:/app/plots covid-project

# If you pulled from Docker Hub (tag: deiwuz/covid_project:general):
# docker run --rm -it -v ${PWD}/data:/app/data -v ${PWD}/plots:/app/plots deiwuz/covid_project:general
```

[View on Docker Hub](https://hub.docker.com/repository/docker/deiwuz/covid_project/general)

#### Option 2: Local Installation

Using [uv](https://github.com/astral-sh/uv) (fast Python package installer) or standard pip.

1.  **Install dependencies**:
    ```bash
    # Using pip
    pip install .

    # Using uv
    uv pip install . --system
    ```

2.  **Run the application**:
    ```bash
    python main.py
    ```

## Usage

The pipeline runs interactively by default. Follow the on-screen prompts to:

1.  **Select Data**: Choose your Population and COVID-19 CSV files from the `data/` directory.
2.  **Standardize**: If country columns are not automatically detected, you will be asked to identify them.
3.  **Process**: The pipeline will automatically merge data, calculate statistics, and generate plots.

### Automated Mode

You can also run the pipeline non-interactively by passing file paths as arguments:

```bash
python main.py <Username> <folder_path_population> <folder_path_covid>
```
*Note: Ensure the paths point to the specific CSV files if the script supports it, or rely on the interactive mode for precise selection.*

## Project Structure

```
Covid_project/
├── covid_etl/              # Core ETL package
│   ├── __init__.py         # Package initialization
│   ├── calculate_per_capita.py # Logic for per capita calculations
│   ├── data_exploration.py # Data loading and preview functions
│   ├── data_merging.py     # Merging and country name standardization
│   └── visualize_results.py# Plotting and visualization logic
├── data/                   # Input and Output data directory
│   ├── covid_cases_per_100k.csv  # Generated Results
│   └── merged_covid_population.csv # Intermediate merged data
├── plots/                  # Generated visualizations
│   └── covid_cases_per_100k_barplot.png
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── main.py                 # Application entry point
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project documentation
```

## Outputs

The pipeline generates the following artifacts:

1.  **`data/merged_covid_population.csv`**: A clean dataset combining COVID-19 cases with population data.
2.  **`data/covid_cases_per_100k.csv`**: A ranked list of countries by infection rate, useful for further analysis.
3.  **`plots/covid_cases_per_100k_barplot.png`**: A high-resolution bar chart showing the top countries with the highest cases per capita.

## Tech Stack

- **Pandas**: For high-performance data manipulation.
- **Matplotlib & Seaborn**: For static data visualization.
- **Python**: Core programming language.

## Author

**Deiwuz**  
Version: 0.1.0
