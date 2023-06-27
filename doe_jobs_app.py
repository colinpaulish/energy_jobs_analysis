#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 08:37:20 2023

@author: colinpaulish
"""

import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the DOE jobs DataFrame
doe_jobs = pd.read_csv('data/doe_2020_explore.csv')

doe_jobs['CountyFIPS'] = doe_jobs['CountyFIPS'].astype('str')


# Load the county shapefile
county_shapefile = gpd.read_file("USA_Counties/USA_Counties.shp")
county_shapefile['FIPS'] = county_shapefile['FIPS'].astype('str')


# Merge the DataFrame and shapefile based on the county FIPS code
merged_data = county_shapefile.merge(doe_jobs, left_on="FIPS", right_on="CountyFIPS", how="left")

# Set up the Streamlit app
st.title("DOE Jobs by County")
st.write("Choropleth map of DOE jobs by county in the USA")

# Plot the choropleth map
fig, ax = plt.subplots(figsize=(12, 8))
merged_data.plot(column="clean_jobs_total", cmap="Blues", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True)
ax.set_axis_off()
st.pyplot(fig)