#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:07:22 2023

@author: colinpaulish
"""

#Get Census data to join
import pandas as pd
from census import Census

census_var_list = ["NAME","B01001_001E", "B02001_001E","B02001_002E","B02001_003E","B02001_004E",
           "B02001_005E","B02001_006E","B02001_007E","B02001_008E", "B06010_011E",
           ]
variable_names = [    "B01003_001E",    "B19013_001E",    "B17001_002E",    "B15003_022E",    "B23025_005E",    "B25064_001E",    "B25077_001E",    "B25003_002E",    "B22003_002E",    "B28002_004E",    "B28002_018E",    "C24010",    "B02001",    "B01002_001E",    "B25027_004E",    "B18101_003E",    "B12001",    "B11005_002E",    "B15003_017E",    "B05002_013E",    "B27001",    "B18120",    "B08006",    "B16001",    "C24010",    "B23025",    "B27010_004E",    "B27010_017E",    "B27010_030E",    "B27010_043E",    "B27010_056E"]


descriptions = [    "Total population",    "Median household income in the past 12 months",    "Number of individuals below the poverty level",    "Population 25 years and over with a bachelor's degree or higher",    "Unemployment rate",    "Median gross rent",    "Median value of owner-occupied housing units",    "Percentage of owner-occupied housing units",    "Percentage of households receiving SNAP benefits",    "Percentage of households with a computer and internet access",    "Percentage of households with a computer and internet access",    "Percentage of civilian labor force employed in different industries",    "Percentage of population by race and ethnicity",    "Median age",    "Percentage of households with a mortgage",    "Percentage of population with a disability",    "Percentage of population by marital status",    "Percentage of households with children under 18 years",    "Percentage of households with a high school diploma or higher",    "Percentage of population born outside the United States",    "Percentage of population by different types of health insurance coverage",    "Percentage of population by different types of disability",    "Percentage of population by means of transportation to work",    "Percentage of population by language spoken at home",    "Percentage of population by occupation",    "Percentage of population by employment status",    "Percentage of population with health insurance coverage through Medicaid",    "Percentage of population with health insurance coverage through employer-based plans",    "Percentage of population with health insurance coverage through direct-purchase plans",    "Percentage of population with health insurance coverage through Medicare",    "Percentage of population with health insurance coverage through military health care"]


column_descriptions = ['CountyName'
    "Totalpopulation",
    "Totalrace",
    "Whitealone",
    "BlackorAfricanAmericanalone",
    "AmericanIndianandAlaskaNativealone",
    "Asianalone",
    "NativeHawaiianandOtherPacificIslanderalone",
    "Someotherracealone",
    "Twoormoreraces",
    "MedianIncome"
]
c = Census('b8f3a3e4653e220861ba7aa5199099a492932401')


census_data = c.acs5.get((census_var_list), {'for': 'county:*'})

census_df = pd.DataFrame(census_data)

column_map = dict(zip(census_var_list, cenus_var_descriptions))

# Replace column names with descriptions
census_df = census_df.rename(columns=column_map)

census_df.columns

voting = pd.read_csv("Projects/energy_jobs/countypres_2000-2020.csv")
voting_subset = voting.iloc[0:100,:]

voting_subset.to_csv('Projects/energy_jobs/voting_explore.csv', index=False)
