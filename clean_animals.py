import pandas as pd
import numpy as np

df = pd.read_csv("Animal Dataset.csv")

def convert_range_to_avg(value):
    if isinstance(value, str):
        value = value.replace("(", "").replace(")", "").replace("usually", "")
        parts = value.strip().split("-")
        numbers = [float(p.strip()) for p in parts if p.strip().replace('.', '', 1).isdigit()]
        if len(numbers) == 2:
            return round(sum(numbers) / 2, 2)
        elif len(numbers) == 1:
            return numbers[0]
    return np.nan

range_cols = ['Height (cm)', 'Weight (kg)', 'Lifespan (years)', 
              'Average Speed (km/h)', 'Gestation Period (days)', 
              'Top Speed (km/h)', 'Offspring per Birth']

for col in range_cols:
    df[col + ' (Cleaned)'] = df[col].apply(convert_range_to_avg)

df_cleaned = df.drop(columns=range_cols)

print(df_cleaned.head())

df_cleaned.to_csv("Cleaned_Animal_Dataset.csv", index=False)
