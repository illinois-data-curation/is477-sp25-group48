import pandas as pd
import os
costs = pd.read_csv("cleaned_data/cleaned_International_Education_Costs.csv")
happiness_c = pd.read_csv("cleaned_data/cleaned_2019_happiness.csv")

costs['Country'] = costs['Country'].replace({'USA':'United States', 'UK':'United Kingdom'})
avg_tuition = costs.groupby('Country')['Tuition_USD'].mean().reset_index(name='Average_Tuition')

happiness_index = happiness_c[['Country or region', 'Score', 'GDP per capita']]
happiness_index.columns = ['Country', 'Happiness_Score', 'GDP_per_capita']

merge = pd.merge(avg_tuition, happiness_index, on='Country', how='inner')

out_dir = "datasets"
os.makedirs(out_dir, exist_ok=True)
merge.to_csv(f"{out_dir}/merged.csv", index=False)