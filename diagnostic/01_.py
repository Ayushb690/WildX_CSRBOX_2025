import pandas as pd

df = pd.read_csv('Cleaned_Animal_Dataset.csv')

diet_types = ['Herbivore', 'Carnivore', 'Insectivore']
filtered_df = df[df['Diet'].isin(diet_types)]

lifespan_by_diet = filtered_df.groupby('Diet')['Lifespan (years) (Cleaned)'].mean().reset_index()

lifespan_by_diet.columns = ['Diet', 'Average Lifespan (years)']

print("Comparison of Average Lifespans by Diet:")
print(lifespan_by_diet)