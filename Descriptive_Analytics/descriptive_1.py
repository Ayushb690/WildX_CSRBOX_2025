import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_animal_data(filepath):
    try:
        df = pd.read_csv(filepath)

        categorical_columns = [
            'Diet',
            'Habitat',
            'Family',
            'Conservation Status',
            'Social Structure',
            'Color'
        ]
        for col in categorical_columns:
            plt.figure(figsize=(10, 5))
            sns.countplot(data=df, y=col, order=df[col].value_counts().index, palette="Set2")
            plt.title(f"Count of Animals by {col}", fontsize=10)
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.tight_layout()
            plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file = 'Cleaned_Animal_Dataset.csv'
    analyze_animal_data(csv_file)
