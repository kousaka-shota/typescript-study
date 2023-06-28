import streamlit as st
import pandas as pd

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'],)

st.write('You selected:', options)
