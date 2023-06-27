#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:12:07 2023

@author: colinpaulish
"""
#Focus only on main republican and democratic candidate

import pandas as pd
import numpy as np

new_dir = "Projects/energy_jobs/data/presidential_voting_2000_to_2020.csv"


voting = pd.read_csv(new_dir, header = 0, 
                     dtype = {"party" : str})

voting['party_str'] = voting['party'].astype(str)


voting['pct_vote'] = voting['candidatevotes'] / voting['totalvotes']

voting_sub = voting[voting['party'].isin(["DEMOCRAT", "REPUBLICAN"])]

voting_2020 = voting_sub[voting_sub['year'] == 2020][['party', 'pct_vote', 'year', 'county_fips']]

voting_2008 = voting_sub[voting_sub['year'] == 2008][['party', 'pct_vote', 'year', 'county_fips']]

voting_change = pd.merge(voting_2020, voting_2008,
                         on = ['county_fips', 'party'])

col_rename = ['party', 'pct_vote_2020', 'year_2020', 'county_fips',
              'pct_vote_2008', 'year_2008']

voting_change.columns = col_rename
voting_change['delta'] = voting_change['pct_vote_2020'] - voting_change['pct_vote_2008']


#NEXT STEP IS TO MAKE THIS DATAFRAME ONE ROW FOR EACH FIPS
# # Reshape the DataFrame
# voting_change_test = voting_change.pivot(index='county_fips', columns='political_party', values=['percent_vote_2008', 'percent_vote_2020'])

# # Flatten the column names
# new_df.columns = [f'{col[0]}_{col[1]}' for col in new_df.columns]

# # Reset the index
# new_df.reset_index(inplace=True)

# #voting_2020_mod = voting_2020[voting_2020['party'] == 'DEMOCRAT' | (voting_2020['party'] == 'REPUBLICAN') ] 

voting_change.to_csv('Projects/energy_jobs/data/vote_test.csv', index=False)
