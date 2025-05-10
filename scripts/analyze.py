import matplotlib.pyplot as plt
import pandas as pd
import os

merged = pd.read_csv('datasets\merged.csv')

threshold = merged[merged['GDP_per_capita']> 1.25]

correlation = threshold['Average_Tuition'].corr(threshold['Happiness_Score'])

plt.figure()
plt.scatter(threshold['Average_Tuition'], threshold['Happiness_Score'])
plt.xlabel('Average Tuition (USD)')
plt.ylabel('Happiness Score (2019)')
plt.title('Tuition vs Happiness for GDPs per Capita above 1.25')
plt.tight_layout

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "tuition_vs_happiness.png")
plt.savefig(output_path)

print(f"Pearson correlation coefficient: {correlation:.3f}")

merged = merged[merged['Average_Tuition'] > 0].copy()

merged['Affordability_Index'] = merged['GDP_per_capita'] / merged['Average_Tuition']
corr1 = merged['Affordability_Index'].corr(merged['Happiness_Score'])

plt.figure()
plt.scatter(merged['Affordability_Index'], merged['Happiness_Score'])
plt.xlabel('Affordability Index (GDP per capita / Average Tuition)')
plt.ylabel('Happiness Score (2019)')
plt.title('Affordability vs Happiness')
plt.tight_layout()

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "affordability_vs_happiness.png")
plt.savefig(output_path)

print(f"Pearson correlation (Affordability vs Happiness): {corr1:.3f}")

