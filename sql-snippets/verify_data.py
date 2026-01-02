"""
Utility script to interactively verify and preview CSV files in the data directory.
 Lists available CSV files and allows the user to select one to print to the console.
"""
import pandas as pd
from pathlib import Path

data_folder = Path('../data')
# data_folder = Path('C:/Users/DEIWUZ/Desktop/covid_project/data')


def select_file():
    possible_csvs = {i: path for i, path in enumerate(data_folder.iterdir()) if path.suffix == '.csv'}
    
    if not possible_csvs:
        return None

    while True:
        # Print all available CSV files
        for i in possible_csvs.keys():
            print(f"{i}: {possible_csvs[i]}")
        
        try:                                                                
            selection = int(input("Please select the CSV file you want to load: "))
            selected_csv = possible_csvs[selection]
            break
        except (ValueError, IndexError, KeyError):
            print(f"Invalid input. Please enter a number between 0 and {len(possible_csvs) - 1}.")
            continue
    return selected_csv

def verify_data(selected_csv: Path):

    if selected_csv is None:
        print("No CSV files found in the data folder.")
        return
    # Read the CSV file into a DataFrame
    df = pd.read_csv(selected_csv)
    print(df.to_string())

if __name__ == "__main__":
    selected_csv = select_file()
    verify_data(selected_csv)


