from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path
import hashlib
import os
api = KaggleApi()
api.authenticate()

os.makedirs("datasets/cost-of-international-education", exist_ok=True)
os.makedirs("datasets/world-happiness",               exist_ok=True)

#df = 'adilshamim8/cost-of-international-education'
#path = './datasets'
#api.dataset_download_files(df, path=path, unzip=True)
#df2 = 'unsdsn/world-happiness'
#api.dataset_download_files(df2, path=path, unzip=True)

datasets = ["adilshamim8/cost-of-international-education", "unsdsn/world-happiness"]
base = Path('./datasets')
base.mkdir(exist_ok=True)

for i in datasets:
    name = i.split('/')[-1]
    dest = base / name
    api.dataset_download_files(i, path=str(dest), unzip=True)

sha = hashlib.sha256(open("datasets/cost-of-international-education/International_Education_Costs.csv", "rb").read()).hexdigest()
with open("datasets/cost-of-international-education/International_Education_Costs.sha256", "w") as f:
    f.write(f"{sha}  International_Education_Costs.csv")

sha = hashlib.sha256(open("datasets/world-happiness/2019.csv", "rb").read()).hexdigest()
with open("datasets/world-happiness/2019.sha256", "w") as f:
    f.write(f"{sha}  2019.csv")
