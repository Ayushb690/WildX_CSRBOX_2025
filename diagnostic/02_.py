import pandas as pd

# Loading the dataset
df = pd.read_csv('Cleaned_Animal_Dataset.csv')


print("Analysis of Conservation Status vs. Habitat:")
conservation_habitat = df.groupby(['Conservation Status', 'Habitat']).size().reset_index(name='Count')
print(conservation_habitat)
print("\n" + "="*50 + "\n") # Separator for clarity

print("Analysis of Conservation Status vs. Gestation Period:")

df['Gestation Period (days) (Cleaned)'] = pd.to_numeric(df['Gestation Period (days) (Cleaned)'], errors='coerce')
conservation_gestation = df.groupby('Conservation Status')['Gestation Period (days) (Cleaned)'].mean().reset_index()
conservation_gestation.columns = ['Conservation Status', 'Average Gestation Period (days)']
print(conservation_gestation)