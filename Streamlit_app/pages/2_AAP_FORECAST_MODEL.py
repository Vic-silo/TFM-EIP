"""
Modelo de predicción para Forecast
"""
import streamlit as st
from pages.page_styler.page_style import ForecastSetup
from forecast.forecast import ForecastModel

# Setup de los datos de la página
ForecastSetup()

# CONTROL DE ACCIONES
forecast_model = ForecastModel()
tab_data, tab_res = st.tabs(["Introducción datos", "Resultados"])
# Iniciar la introducción de los datos
with tab_data:
    forecast_model.input_data()

with tab_res:
    forecast_model.res_data()
