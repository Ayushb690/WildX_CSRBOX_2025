import pandas as pd
import numpy as np

def calculate_family_averages(filepath):

    try:
        df = pd.read_csv(filepath)

        numeric_columns = [
            'Lifespan (years) (Cleaned)',
            'Weight (kg) (Cleaned)',
            'Height (cm) (Cleaned)'
        ]
        
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        family_averages = df.groupby('Family')[numeric_columns].mean()
        family_averages.columns = [
            'Average Lifespan (years)', 
            'Average Weight (kg)', 
            'Average Height (cm)'
        ]
        family_averages = family_averages.round(2)
        print("--- Average Lifespan, Weight, and Height per Animal Family ---")
        print(family_averages)

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please check the file path and try again.")
    except KeyError as e:
        print(f"Error: A required column is missing from the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file = 'Cleaned_Animal_Dataset.csv'
    calculate_family_averages(csv_file)
