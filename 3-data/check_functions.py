import streamlit as st
import pandas as pd
import numpy as np

# This is the module
def clean_currency(value:str) -> float:
    '''
    This function takes a value and as str and removes the'$' and ',' and converts to a float.
    It returns the float value
    '''
    value = value.replace(',','')
    value = value.replace('$','')
    float_value = float(value)
    return float_value

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return ''