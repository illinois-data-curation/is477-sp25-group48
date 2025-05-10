# Final Project Preliminary Plan
Measuring the Impact of Remote Work on Transportation Emissions (Metro-Level Analysis 2022-2023)

## Overview
The overall goal is to quantify whether shifts towards remote and hybrid work in U.S metropolitan cities have reduced transportation related C02 emissions in comparison to cities that have lower remote work rates. Transportation accounts for roughly a quarter of carbon emission in the U.S. and I wanted to uncover whether if remote work has caused a regression in C02 emissions. If CO2 levels are still high in areas with more remote work, I'd want to identify what could be other causes for the high CO2 emissions. I'd also want to identify whether emissions benefit cities that have disproportionately more white collar jobs. Those types of jobs and the work they do allow the ability to even work from home.
## Research Questions
Did US metro areas with >30% remote workers between (2022-2023) see larger reductions in transportation emissions than commuting-heavy cities?

What type of transportation for commuting to work contributes the most to C02 emissions (train, bus, car)?

## Team
There are no other team members so I will be completing all of the project responsibilities myself
## Datasets
US Census LEHD WFH Data
Source: U.S. Census Bureau - LEHD Program
Format: CSV
License: Public Domain (U.S. Government)
The Longitudinal Employer-Household Dynamics (LEHD) program's Work Area Characteristics (WAC) dataset offers a rare look into telework trends in U.S. metropolitan areas. Created by the U.S. Census Bureau through a blend of unemployment insurance records, employer surveys, and data from the American Community Survey, this public dataset provides quarterly insights into employment arrangements across various geographic levels. For your research, the key elements to focus on include the detailed counts of telework-enabled jobs (identified as SA02 in the technical documentation) along with total employment numbers, which will enable you to calculate accurate work-from-home adoption rates. 

EPA Motor Vehical Emissions Simulator Data
Source: EPA MOVES Model
Format: API(JSON) + CSV exports
License: Public Domain
The Environmental Protection Agency's Motor Vehicle Emissions Simulator (MOVES) dataset stands out as the leading resource for monitoring transportation-related pollution across the United States. This advanced modeling system leverages millions of real-world data points gathered from emissions testing, traffic monitoring, and vehicle registration databases to estimate emissions for various vehicle types under different operating conditions. 

## Timeline
April 3rd - 7th
### Objectives:
Automate data acquisition from data sets that I will be using for the project; add checksum verification for downloaded files; implement data validation and storage.
April 8th - 14th
### Objectives:
assess data completeness and outliers; profile datasets and clean data if needed, start calculating descriptive statistics comparing high-WFH cities with low-WFH cities; create visuals to show results
Status report [Due April 15th]
April 15th - 21st
### Objectives:
convert scripts into an installable Python package, automate end-to-end workflow; create Makefile to run pieplines.
April 22nd - May 1st
### Objectives:
Ensure long-term reproducibility; write metadata; citations for data sources and tools
Final Project submission [May 1st]
