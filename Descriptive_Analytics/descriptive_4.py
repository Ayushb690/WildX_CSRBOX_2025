import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_pie_chart(filepath):
    """
    Reads an animal dataset and creates a pie chart for the 
    'Social Structure' distribution.

    Args:
        filepath (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(filepath)

        social_structure_counts = df['Social Structure'].value_counts()

        sns.set_style("whitegrid")
        
        plt.figure(figsize=(12, 10))

        colors = sns.color_palette('pastel')[0:len(social_structure_counts)]
        
        plt.pie(social_structure_counts, labels=social_structure_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
        
        plt.title('Distribution of Animals by Social Structure', fontsize=18, pad=20)
        
        plt.axis('equal')  

        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please check the file path.")
    except KeyError as e:
        print(f"Error: A required column is missing from the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Main execution ---
if __name__ == "__main__":
    csv_file = 'Cleaned_Animal_Dataset.csv'
    
    create_pie_chart(csv_file)
