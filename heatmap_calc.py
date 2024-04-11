import pandas as pd

# Load the CSV data to understand its structure
file_path = 'C:/Users/admin/downloads/BUS496_Int_Sum.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

import seaborn as sns
import matplotlib.pyplot as plt

# Set the index to the categories of interviewees for better visualization
data.set_index('Unnamed: 0', inplace=True)

# Creating the heat map
plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(data, annot=True, cmap='coolwarm', fmt="d")
heatmap.set_title('Interview Feedback Heatmap', fontdict={'fontsize':18}, pad=12)
heatmap.set_xlabel('Feedback Type', fontsize=14)
heatmap.set_ylabel('Interviewee Category', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
output_file_path = 'C:/Users/admin/downloads/interview_feedback_heatmap.png'
plt.savefig(output_file_path)

output_file_path
plt.show()

