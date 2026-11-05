import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("Challenge 3-2-2: Nested JSON")

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

response = requests.get(url)
json_data = response.json()

data = pd.json_normalize(json_data, record_path = "employees", meta = "dept")

st.dataframe(data)