"""
Modelo de predicción para Forecast
"""
import streamlit as st
from pages.page_styler.page_style import ForecastSetup
from forecast.forecast import input_data

# Setup de los datos de la página
ForecastSetup()

# Introducción de datos
input_data()
