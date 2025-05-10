import pandas as pd
import os

costs = pd.read_csv("datasets/cost-of-international-education/International_Education_Costs.csv")
happiness_c = pd.read_csv("datasets/world-happiness/2019.csv")

#for trimming white space
for i in (costs, happiness_c):
    header = i.select_dtypes(include='object').columns
    i[header] = i[header].apply(lambda col: col.str.strip())

#harmonizing/cremoving duplicates
costs["Country"] = costs["Country"].str.strip().replace({"USA": "United States", "UK": "United Kingdom"})
costs = costs.drop_duplicates()
happiness_c = happiness_c.drop_duplicates()
costs = costs.dropna(subset=["Country", "Tuition_USD"])
happiness_c = happiness_c.dropna(subset=["Country or region", "Score"])

out_dir = "cleaned_data"
os.makedirs(out_dir, exist_ok=True)

costs.to_csv(f"{out_dir}/cleaned_International_Education_Costs.csv", index=False)
happiness_c.to_csv(f"{out_dir}/cleaned_2019_happiness.csv", index=False)
