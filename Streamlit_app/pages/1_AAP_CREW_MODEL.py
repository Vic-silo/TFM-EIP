"""
Modelo de predicción para Forecast
"""
import streamlit as st
from pages.page_styler.page_style import CrewSetup
from crew.crew import CrewModel


# Setup de los datos de la página
CrewSetup()

# MODELO FORECAST
# Instancia de clase para introducir datos y predecir
crew_model = CrewModel()

# Tabs con las secciones para introducir datos y mostrar resultados
tab_forecast, tab_crew, tab_flight, tab_aux, tab_res = st.tabs([
    "DATOS CLIMATOLOGICOS", "DATOS TRIPULACIÓN", "DATOS VUELO",
    "DATOS AUXLIARES", ":blue[RESULTADOS]"])

with tab_forecast:
    crew_model.data_forecast()

with tab_crew:
    crew_model.data_crew()

with tab_flight:
    crew_model.data_flight()

with tab_aux:
    crew_model.data_aux()

with tab_res:
    crew_model.res_data()
