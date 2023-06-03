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
forecast_model = CrewModel()

# Tabs con las secciones para introducir datos y mostrar resultados
tab_forecast, tab_crew, tab_flight, tab_res = st.tabs([
    "DATOS CLIMATOLOGICOS", "DATOS TRIPULACIÓN", "DATOS VUELO",
    ":blue[RESULTADOS]"])


with tab_forecast:
    forecast_model.data_forecast()

with tab_crew:
    forecast_model.data_crew()

with tab_flight:
    forecast_model.data_flight()

with tab_res:
    forecast_model.res_data()