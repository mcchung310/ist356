import streamlit as st

st.title("Order Amount Accumulator")

# Note: the use case for session state is that you need to remember the value between interactions 

#initialize intro session state - only runs once, when the app/page is first loaded from that point on, the variables are there and static (they are remembered)
if 'total_order' not in st.session_state:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

amount = st.number_input(
    "Enter an amount", min_value=0.0)
add_to_order = st.button(
    "Add to Order", type="primary")
clear_order = st.button(
    "Clear Order", type="secondary")

# Order accumulation logic 
if add_to_order:
    st.session_state.total_order += amount # "+=: is shortcut for "st.session_state.total = st.session_state.total + amount"
    st.session_state.order_history.append(amount) # append adds it to a list 
if clear_order:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

st.text(
    f"Total Order: {st.session_state.total_order}")

for o in st.session_state.order_history:
    st.text(f"Order Item: {o}")





