rule all:
    input:
        "output/tuition_vs_happiness.png",
        "output/affordability_vs_happiness.png"

rule download_data:
    output:
        "datasets/cost-of-international-education/International_Education_Costs.csv",
        "datasets/world-happiness/2019.csv"
    script:
        "scripts/download_data.py"
rule clean:
    input:
        costs="datasets/cost-of-international-education/International_Education_Costs.csv",
        happy="datasets/world-happiness/2019.csv"
    output:
        costs_clean="cleaned_data/cleaned_International_Education_Costs.csv",
        happy_clean="cleaned_data/cleaned_2019_happiness.csv"
    script:
        "scripts/clean.py"
rule integration:
    input:
        costs_clean="cleaned_data/cleaned_International_Education_Costs.csv",
        happy_clean="cleaned_data/cleaned_2019_happiness.csv"
    output:
        "datasets/merged.csv"
    script:
        "scripts/integration.py"
rule analyze:
    input:
        "datasets/merged.csv"
    output:
        tuition_png="output/tuition_vs_happiness.png",
        afford_png="output/affordability_vs_happiness.png"
    script:
        "scripts/analyze.py"