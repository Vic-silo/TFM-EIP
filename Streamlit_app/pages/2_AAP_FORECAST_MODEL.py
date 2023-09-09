"""
Modelo de predicción para Forecast
"""
import streamlit as st
from pages.page_styler.page_style import ForecastSetup
from forecast.forecast import ForecastModel


# Setup de los datos de la página
ForecastSetup()

# Introducción de datos
forecast_model = ForecastModel()

# Tabs con las secciones para introducir datos y mostrar resultados
list_of_tabs = ["DATOS CLIMATOLOGICOS", "DATOS TRIPULACIÓN", "DATOS VUELO",
                ":blue[RESULTADOS]"]
tabs = st.tabs(list_of_tabs)

with tabs[0]:
    forecast_model.data_forecast()

with tabs[1]:
    forecast_model.data_crew()

with tabs[2]:
    forecast_model.data_flight()

with tabs[3]:
    forecast_model.res_data()

# Handling query parameters
query = st.experimental_get_query_params()

try:
    index_tab = query["tab"][0]

    ## Click on that tab
    js = f"""<script>var tab = window.parent.document.getElementById(
'tabs-bui3-tab-{index_tab}');tab.click();</script>"""

    st.components.v1.html(js)

except Exception as e:
    print('[-] ', e)
