import streamlit as st
import pandas as pd
import numpy as np

# Questions to ask yourself: Does it have a header? Is it a first row header? 
# What is the row delimiter? What is the cell field delimiter? Do I need to skip lines? 

st.title("Challenge 3-2-1: Data Practice")

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"
data = pd.read_csv(url, sep=' ', skiprows=3)

st.dataframe(data)
