"""
Modelo de predicción para Airplane
"""
import streamlit as st
from pages.page_styler.page_style import AirplaneSetup
from airplane.airplane import AirplaneModel

# Setup de los datos de la página
AirplaneSetup()

# MODELO AIRPLANE
# Instancia de clase para introducir datos y predecir
airplane_model = AirplaneModel()

# Tabs con las secciones para introducir datos y mostrar resultados
# tab_forecast, tab_crew, tab_flight, tab_aux, tab_res = st.tabs([
tab_general, tab_motor, tab_vuelo, tab_res = st.tabs([
    "DATOS GENERALES", "DATOS DEL MOTOR", "DATOS DE VUELO", ":blue[RESULTADOS]"])
#    "DATOS AUXLIARES", ":blue[RESULTADOS]"])

with tab_general:
    airplane_model.data_general()

with tab_motor:
    airplane_model.data_motor()

with tab_vuelo:
    airplane_model.data_vuelo()

#with tab_aux:
#    airplane_model.data_aux()

with tab_res:
    airplane_model.res_data()