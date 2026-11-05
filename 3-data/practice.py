import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-no-header.csv"
students = pd.read_csv(url, header=None, names =['Name','Grade','Year'])

st.dataframe(students)