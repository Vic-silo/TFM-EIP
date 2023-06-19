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
list_of_tabs = ["DATOS CLIMATOLOGICOS", "DATOS TRIPULACIÓN", "DATOS VUELO",
                "DATOS AUXLIARES", ":blue[RESULTADOS]"]
tabs = st.tabs(list_of_tabs)

with tabs[0]:
    crew_model.data_forecast()

with tabs[1]:
    crew_model.data_crew()

with tabs[2]:
    crew_model.data_flight()

with tabs[3]:
    crew_model.data_aux()

with tabs[4]:
    crew_model.res_data()

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
