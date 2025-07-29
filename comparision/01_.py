import pandas as pd

df = pd.read_csv('Cleaned_Animal_Dataset.csv')

df['Average Speed (km/h) (Cleaned)'] = pd.to_numeric(df['Average Speed (km/h) (Cleaned)'], errors='coerce')

df_cleaned_speed = df.dropna(subset=['Average Speed (km/h) (Cleaned)'])

df_cleaned_speed['Has_Predators'] = ~df_cleaned_speed['Predators'].isin(['Not Applicable', pd.NA]).fillna(False)

speed_comparison = df_cleaned_speed.groupby('Has_Predators')['Average Speed (km/h) (Cleaned)'].mean().reset_index()

speed_comparison['Category'] = speed_comparison['Has_Predators'].apply(
    lambda x: 'Animals with Listed Predators (Prey)' if x else 'Animals with No Listed Predators'
)

print("Comparison of Average Speed by Predator Status:")
print(speed_comparison[['Category', 'Average Speed (km/h) (Cleaned)']])