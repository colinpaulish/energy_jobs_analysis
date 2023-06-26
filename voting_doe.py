#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:12:07 2023

@author: colinpaulish
"""
#Focus only on main republican and democratic candidate

import pandas as pd
import numpy as np

new_dir = "Projects/energy_jobs/presidential_voting_2000_to_2020.csv"


voting = pd.read_csv(new_dir, header = 0)
voting['party'] = voting['party'].astype(str)

voting_2020 = voting[voting['year'] == 2020]

voting_2020_mod = voting_2020[voting_2020['party'] == 'DEMOCRAT' | (voting_2020['party'] == 'REPUBLICAN') ] 

#df[(df['ColumnName'] == 'A') | (df['ColumnName'] == 'B')]