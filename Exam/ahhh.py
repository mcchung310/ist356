import pandas as pd
import streamlit as st

customers = pd.DataFrame({
    "Customer": ["Abby", "Bette", "Chris", "Dan"],
    "City":     ["Syracuse", "Syracuse", "Albany", "Boston"],
    "Points":   [120, 80, 45, 60]
})
st.write("Customers Table")
st.write(customers)

stores = pd.DataFrame({
    "Store":    ["Downtown", "Mall", "Plaza", "Harbor"],
    "Location": ["Syracuse", "Syracuse", "Albany", "Buffalo"]
})
st.write("Stores Table")
st.write(stores)

stores_1 = pd.DataFrame({
    "Store":    ["Downtown", "Mall", "Plaza", "Harbor"],
    "City": ["Syracuse", "Syracuse", "Albany", "Buffalo"]
})

inner = pd.merge(customers, stores_1, on="City", how="inner")
st.write("inner")
st.write(inner)

left = pd.merge(customers, stores, left_on="City", right_on="Location", how="left")
st.write("Left")
st.write(left)

right = pd.merge(customers, stores, left_on="City", right_on="Location", how="right")
st.write("Right")
st.write(right)

outer = pd.merge(customers, stores, left_on="City", right_on="Location", how="outer")
st.write("Outer")
st.write(outer)



grades = pd.DataFrame({
    "Student": ["Owen", "Meena", "Jon"],
    "Quiz1": ["90", "100", "95"],
    "Quiz2": ["80", "101", "85"],
    "Quiz3": ["99", "99", "100"]
})

melt = grades.melt(id_vars=["Student"], value_vars=["Quiz1", "Quiz2", "Quiz3"]) 
st.write(grades)
st.write(melt)