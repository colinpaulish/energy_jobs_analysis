#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:36:46 2023

@author: colinpaulish
"""
#Load in the data and observe the top rows
import pandas as pd
import random
from IPython.display import display

under_ten_start = 1
under_ten_end = 9

new_dir = "Projects/energy_jobs/doe_2020.csv"

doe_2021 = pd.read_csv(new_dir ,header = 1)

doe_2021.head()

#Columns and column values have weird spaces before and after the values
doe_2021.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
doe_2021 = doe_2021.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#Maniplate data so anything unnamed is deleted -- these were formatted columns
unnamed_columns = [col for col in doe_2021.columns if 'Unnamed' in col]
doe_2021 = doe_2021.drop(columns=unnamed_columns)

#Add a leading zero to county FIPs whose state fips are <10 
doe_2021['CountyFIPS'] = doe_2021['CountyFIPS'].astype(str)

doe_2021['CountyFIPS'] = doe_2021['CountyFIPS'].apply(lambda x: '0' + x if len(x) <= 4 else x)


#Manipulate the data so that anything with a dash is 0
doe_2021 = doe_2021.replace("-", 0)

#Remove commas from the numerical figures
doe_2021 = doe_2021.apply(lambda x: x.str.replace(',', ''))
doe_2021 = doe_2021.apply(lambda x: x.str.replace(' ', ''))



#wherever the value is "< 10" replace with a value between 1-10
def under10_replace(x):
    if isinstance(x, str) and x.strip() == "<10":
        return random.randint(under_ten_start, under_ten_end)
    return x

# Apply the function to the entire DataFrame
doe_2021 = doe_2021.applymap(under10_replace)



#Get Census data to join
from census import Census

c =Census('b8f3a3e4653e220861ba7aa5199099a492932401')
census_data = c.acs5.get(('NAME', 'B01001_001E'), {'for': 'county:*'})

# Convert the data to a pandas DataFrame
import pandas as pd
pop_data = pd.DataFrame(census_data)

pop_data['CountyFIPS'] = pop_data['state'] + pop_data['county'] 

#Join populdation data to energy data

doe_census = pd.merge(doe_2021, pop_data, on = 'CountyFIPS', how = 'left')

display(doe_census)

#Rename ambiguous columns
doe_census = doe_census.rename(columns={'B01001_001E': 'county_pop'})
doe_census = doe_census.rename(columns={'Other': 'OtherElectricPower'})
doe_census = doe_census.rename(columns={'Other.1': 'OtherFuels'})
doe_census = doe_census.rename(columns={'Other.2': 'OtherEnergyEfficiency'})
doe_census = doe_census.rename(columns={'Coal': 'CoalElectricPower'})
doe_census = doe_census.rename(columns={'Coal.1': 'CoalFuels'})
doe_census = doe_census.rename(columns={'NaturalGas': 'NaturalGasElectricPower'})
doe_census = doe_census.rename(columns={'NaturalGas.1': 'NaturalGasFuels'})




object_to_numeric = ['Solar', 'Wind', 'Hydroelectric', 'Low-ImpactHydroelectric', 
                     'NaturalGasFuels', 
                     'CoalElectricPower', 'Oil&OtherFF', 
                     #'OtherElectricPower', 
                     'OtherEnergyEfficiency',
                     'TraditionalTDS', 'Storage', 'SmartGrid', 
                     'MicroGrid', 'OtherGridMod', 'CoalFuels', 'Petroleum', 
                    'NaturalGasElectricPower', 
                    'WoodyBiomass', 'CornEthanol', 'OtherCleanFuels', 'OtherElectricPower', 
                     'ENERGYSTAR&EfficientLighting', 'TraditionalHVAC', 
                    'HighEfficiencyHVAC&RenewableH&C', 'AdvancedMaterials&Insulation', 
                     'OtherFuels', 'MV', 'EPG', 'TDS', 'Fuels', 'EE']

#doe_census.to_csv('doe_explore.csv', index=False)


doe_census['OtherElectricPower'] = pd.to_numeric(doe_census['OtherElectricPower'])

doe_census[object_to_numeric] = doe_census[object_to_numeric].astype(float)


numeric_columns = doe_census.select_dtypes(include=[int, float]).columns

# Calculate the percentage based on county_pop for each numeric column
for col_name in numeric_columns:
    if col_name != 'county_pop':  # Skip 'Column1'
        new_col_name = col_name + '_prop'
        doe_census[new_col_name] = (doe_census[col_name] / doe_census['county_pop'])
        
#Need to revisit this 
clean_jobs = ['Solar', 'Wind', 'Hydroelectric', 'Low-ImpactHydroelectric', 'OtherEnergyEfficiency',
              'Storage', 'SmartGrid', 'MicroGrid', 'OtherGridMod', 'OtherCleanFuels',
              'ENERGYSTAR&EfficientLighting', 'HighEfficiencyHVAC&RenewableH&C','AdvancedMaterials&Insulation']

dirty_jobs = [x for x in object_to_numeric if x not in clean_jobs]

doe_census['clean_jobs_total'] = doe_census[clean_jobs].sum(axis = 1)
doe_census['dirty_jobs_total'] = doe_census[dirty_jobs].sum(axis = 1)

        
        
doe_census.to_csv('Projects/energy_jobs/doe_2020_explore.csv', index=False)
