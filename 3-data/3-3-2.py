# Challenge 3-3-2

import streamlit as st
import pandas as pd
import numpy as np

# Inputs and Get url's
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ["jan", "feb", "mar", "apr"]
selected = st.selectbox("Select a month", months)
monthly_url = f"{base}purchases-{selected}.csv"
customer_url = f"{base}customers.csv"
st.write(monthly_url)

# Dataframes and Merges
orders = pd.read_csv(monthly_url)
customers = pd.read_csv(customer_url)
combined = pd.merge(orders, customers, 
                    left_on = "customer_id",
                    right_on = "customer_id",
                    how = "right")

# Slight manipulation to amke the data more accurate 
combined_filtered = combined[combined['order_id'].isnull()]
combined_filtered_cols = combined_filtered[
    ['customer_id', 'firstname', 'lastname']
]


# Outputs
st.title("Customers Table")
st.dataframe(customers)

st.title("Orders Table")
st.dataframe(orders)

st.title("Combined Table")
st.dataframe(combined)

st.title("Combined Filtered")
st.dataframe(combined_filtered)

st.title("Combined Filtered Columns")
st.dataframe(combined_filtered_cols)
