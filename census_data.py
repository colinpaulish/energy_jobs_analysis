#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:07:22 2023

@author: colinpaulish
"""

#Get Census data to join
import pandas as pd
from census import Census

census_vars = variable_names = ["GEO_ID",
    "B01003_001E",
    "B19013_001E",
    "B01002_001E",
    "B15003_017E",
    "B15003_022E",
    "B17001_001E",
    "B23025_005E",
    "B25003_002E",
    "B25003_003E",
    "B25077_001E",
    "B25064_001E",
    "B05006_001E",
    "B02001_002E",
    "B02001_003E",
    "B02001_005E",
    "B03001_003E",
    "B18101_001E",
    "B27001_001E",
    "B08013_001E",
    "B25010_001E"
]


cenus_var_descriptions = [ 'county_fips'
    "TotalPopulation",
    "MedianHouseholdIncome",
    "MedianAge",
    "EducationHighSchoolOrHigher",
    "EducationBachelorOrHigher",
    "PovertyStatus",
    "UnemploymentRate",
    "OwnerOccupiedHousingUnits",
    "RenterOccupiedHousingUnits",
    "MedianHouseValue",
    "MedianGrossRent",
    "ForeignBornPopulation",
    "RaceWhiteAlone",
    "RaceBlackAlone",
    "RaceAsianAlone",
    "RaceHispanicOrLatino",
    "DisabilityStatus",
    "HealthInsuranceCoverage",
    "CommuteTime",
    "MedianHouseholdSize"
]
c = Census('b8f3a3e4653e220861ba7aa5199099a492932401')


census_data = c.acs5.get((census_vars), {'for': 'county:*'})

census_df = pd.DataFrame(census_data)

column_map = dict(zip(census_vars, cenus_var_descriptions))

# Replace column names with descriptions
census_df = census_df.rename(columns=column_map)

census_df.columns

census_df.to_csv('Projects/energy_jobs/data/census_test.csv', index=False)
