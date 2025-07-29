import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_bar_plots(filepath):
    """
    Reads an animal dataset and creates bar plots for the 'Diet' and 
    'Conservation Status' distributions.

    Args:
        filepath (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(filepath)

        sns.set_style("whitegrid")
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 16))
        fig.suptitle('Animal Data Distribution', fontsize=20, y=1.02)
        
        diet_counts = df['Diet'].value_counts()
        
        sns.barplot(x=diet_counts.index, y=diet_counts.values, ax=axes[0], palette='viridis')
        axes[0].set_title('Distribution by Diet Type', fontsize=16)
        axes[0].set_xlabel('Diet Type', fontsize=12)
        axes[0].set_ylabel('Number of Animals', fontsize=12)
        axes[0].tick_params(axis='x', rotation=45)


        conservation_counts = df['Conservation Status'].value_counts()

        sns.barplot(x=conservation_counts.index, y=conservation_counts.values, ax=axes[1], palette='plasma')
        axes[1].set_title('Distribution by Conservation Status', fontsize=16)
        axes[1].set_xlabel('Conservation Status', fontsize=12)
        axes[1].set_ylabel('Number of Animals', fontsize=12)
        axes[1].tick_params(axis='x', rotation=45)

        
        plt.tight_layout(rect=[0, 0, 1, 0.98])
        
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please check the file path.")
    except KeyError as e:
        print(f"Error: A required column is missing from the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file = 'Cleaned_Animal_Dataset.csv'
    
    create_bar_plots(csv_file)
