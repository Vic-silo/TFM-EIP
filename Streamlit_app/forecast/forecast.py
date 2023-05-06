"""
Clase
"""
import pandas as pd
import streamlit as st

SOURCE_DIRECTORY = 'source/forecast/'
MAPPED_DIC = f'{SOURCE_DIRECTORY}mapped_dictionary.csv'


class ForecastModel:
    country_selector = 'Ninguno'

    def input_data(self):
        st.write('Hoola desde el modulo de forecast revisado')
        self.country_selector = st.selectbox('Selecciona el pais deseado.',
                                             ['España', 'Holanda'])

    def res_data(self):
        st.button('Hola')
        st.write(f'Tu pais favorito es: {self.country_selector}')
