import pandas as pd
import numpy as np 
import streamlit as st

st.title("Concat")
fall   = pd.DataFrame({"Name": ["Abby", "Bette"], "Grade": [90, 85]})
spring = pd.DataFrame({"Name": ["Chris", "Dan"],  "Grade": [70, 95]})

st.subheader("Fall Table")
st.write(pd.DataFrame(fall))

st.subheader("Spring Table")
st.write(pd.DataFrame(spring))

st.subheader("Fall and Spring concat")
fall_spring = pd.concat([fall, spring])
st.write(fall_spring)

st.subheader("Fall and Spring, ingore_index = TRUE")
st.write(pd.concat([fall, spring], ignore_index=True))


clubs = pd.DataFrame({"Name": ["Eve", "Fay"], "Club": ["Chess", "Art"]})

st.subheader("Fall and Clubs Table")
st.write(pd.concat([fall, clubs], ignore_index=True))

st.subheader("Name/Grades Table")
a = pd.DataFrame({"Name": ["Abby", "Bette"],  "Grade": [90, 85]})
b = pd.DataFrame({"Name": ["Bette", "Chris"], "Grade": [60, 70]})

combined = pd.concat([a, b], ignore_index=True)
st.write(combined) 

st.write("drop_duplicates()")
st.write(combined.drop_duplicates()) 
st.write("drop_duplicates, subset ='Name'")
st.write(combined.drop_duplicates(subset="Name"))

st.title("Merge")
students = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Abby", "Bette", "Chris"]})
grades   = pd.DataFrame({"ID": [1, 2, 4], "Grade": [90, 85, 70]})

st.subheader("Students Table")
st.write(students)
st.subheader("Grades Table")
st.write(grades)

st.subheader("Inner Join") #only the rows that match on both sides
inner = pd.merge(students, grades, on="ID", how="inner")
st.write(inner)

st.subheader("Left Join") #all of the left table, plus matches
left = pd.merge(students, grades, on="ID", how="left")
st.write(left)

st.subheader("Right Join") #all of the right table, plus matches
right = pd.merge(students, grades, on="ID", how="right")
st.write(right)

st.subheader("Outer Join") #everything from both
outer = pd.merge(students, grades, on="ID", how="outer")
st.write(outer)


st.header("Merge Practice")

customers = pd.DataFrame({
    "Customer": ["Abby", "Bette", "Chris", "Dan"],
    "City":     ["Syracuse", "Syracuse", "Albany", "Boston"],
    "Points":   [120, 80, 45, 60]
})

stores = pd.DataFrame({
    "Store":    ["Downtown", "Mall", "Plaza", "Harbor"],
    "Location": ["Syracuse", "Syracuse", "Albany", "Buffalo"]
})

stores2 = stores.rename(columns={"Location": "City"})

merge1 = pd.merge(customers, stores, 
                  left_on = "City", right_on = "Location", how = "inner")
st.write(merge1)


sales = pd.DataFrame({
    "Store": ["Downtown", "Downtown", "Mall", "Harbor"],
    "Month": ["Jan", "Feb", "Jan", "Feb"],
    "Sales": [100, 150, 80, 60]
})
st.write(sales)

st.subheader("Pivot")
pivot = sales.pivot(index="Store", columns="Month", values="Sales")
st.write(pivot)

st.subheader("Melt")
melt = sales.melt()


wide = pd.DataFrame({
    "Store": ["Downtown", "Mall"],
    "Jan":   [100, 80],
    "Feb":   [150, 120],
    "Mar":   [130, 90]
})
st.write(wide)

wide.melt(value)