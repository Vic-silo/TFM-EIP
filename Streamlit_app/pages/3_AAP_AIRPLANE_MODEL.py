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
list_of_tabs = ["DATOS GENERALES", "DATOS DEL MOTOR", "DATOS DE VUELO",
                ":blue[RESULTADOS]"]
tabs = st.tabs(list_of_tabs)

with tabs[0]:
    airplane_model.data_general()

with tabs[1]:
    airplane_model.data_motor()

with tabs[2]:
    airplane_model.data_vuelo()

with tabs[3]:
    airplane_model.res_data()

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
