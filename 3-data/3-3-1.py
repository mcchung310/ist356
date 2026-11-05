# Challenege 3-3-1 

import streamlit as st
import pandas as pd
import numpy as np
import requests

# use requests to read in this as json data
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employee_data = response.json()

st.write(employee_data)

# loop over each key, create dataframe, display it 
for key in employee_data.keys():
    st.write(f"Data for {key}:")
    #employee_data is the json, [key] is the specific section of the JSON being displayed (ex. 'marketing' is list)
    df = pd.DataFrame(employee_data[key]) 
    st.dataframe(df)

# This right below is the root of what we are solving 
dfs = []
for key in employee_data.keys():
    df = pd.DataFrame(employee_data[key])
    df['department'] = key # add a new colum for department (lineage)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined DataFrame:")
st.dataframe(combined_df)


filename = "3-data/combined_employee_data.jsonl"
combined_df.to_json(filename, orient="records", lines=True) 
    # orient="records" -> represented list like (one row for each item)
    # lines=True -> json L format (no brackets) [{}] vs just {}
st.write(f"Combined DataFrame saved to '{filename}' in JSON Lines format.")