"""
Clase
"""
import pandas as pd
import streamlit as st

SOURCE_DIRECTORY = 'source/forecast/'
MAPPED_DIC = f'{SOURCE_DIRECTORY}mapped_dictionary.csv'


def input_data():
    st.write('Hoola desde el modulo de forecast revisado')
