## Challenge 2-2-1
# Write a streamlit to input a length and width of a rectangle, and output the permieter 2 x (L+W) 
# and area (L x W) of that rectangle use a "calculate" button and a "clear" button use `st.number_input()` for numbers

from narwhals import col
import streamlit as st

st.title("Challenge 2-2-1: Rectangle Calculator")
length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step=0.1)

col1, col2, col3 = st.columns([0.15, 0.15, 0.8])
with col1:
    clear = st.button("Clear")
with col2:
    calculate_button = st.button("Calculate")

if calculate_button:
    perimeter = 2 * (length + width)
    area = length * width
    st.success(f"Area: {area}, Perimeter: {perimeter}")

if clear:
    length = 0.0
    width = 0.0

