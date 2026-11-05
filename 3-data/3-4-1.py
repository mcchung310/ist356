import streamlit as st
import pandas as pd
import numpy as np

# Data Pipeline 

# Import from module
from check_functions import clean_currency, detect_whale

### Main code
st.title("Challenge 3-4-1: Modularizing")
checks = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv")

## Transformations
checks["total_amount_cleaned"] = checks["total amount of check"].apply(clean_currency)
# These two lines do the same thing 
# checks["gratuity_cleaned"] = checks['gratuity'].apply(clean_currency)
checks['gratuity_cleaned'] = checks.apply(lambda row: 
                                          clean_currency(row['gratuity']), axis = 1)

checks['price_per_item'] = checks['total_amount_cleaned']/checks['total items on check']
checks['price_per_person'] = checks['total_amount_cleaned']/checks['party size']
checks['items_per_person'] = checks['total items on check']/checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned']/checks['total_amount_cleaned']

#calculate the top percetile for the items per person and price per person
top_pctile_items_per_person = checks['items_per_person'].quantile(0.75)
top_pctile_price_per_person = checks['price_per_person'].quantile(0.75)

checks['customer_type'] = checks.apply(lambda row: detect_whale(
    row['items_per_person'],
    row['price_per_person'],
    top_pctile_items_per_person,
    top_pctile_price_per_person
), axis=1)

st.write('### Check Data')
st.write(f"Top percentile for items per person: {top_pctile_items_per_person}")
st.write(f"Top percentile for price per person: {top_pctile_price_per_person}")

customer_values = checks['customer_type'].value_counts()

cols = st.columns(len(customer_values))
for i, (customer_type, count) in 

st.dataframe(checks)