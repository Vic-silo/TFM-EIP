import streamlit as st


class ForecastSetup:
    def __init__(self):
        # Favicon
        st.set_page_config(page_title="AAP - Forecast", )

        # Introducción
        st.markdown("# MODELO DE PREDICCIÓN FORECAST")
        st.markdown("Para la predicción, introduzca a continuación los campos "
                    "requeridos que se le muestran.")
        st.divider()

        # Sidebar
        st.sidebar.header("MODELO DE PREDICCIÓN: FORECAST")
        st.sidebar.markdown(
            "En esta sección, se presenta la predicción de accidente para un"
            "vuelo teniendo en cuenta las condiciones climáticas y las "
            "caracteristicas del piloto.")


class AirplaneSetup:
    def __init__(self):
        # Favicon
        st.set_page_config(page_title="AAP - Airplane", )

        # Introducción
        st.markdown("# MODELO DE PREDICCIÓN AIRPLANE")

        # Sidebar
        st.sidebar.header("MODELO DE PREDICCIÓN: AIRPLANE")
        st.sidebar.markdown(
            "En esta sección, se presenta la predicción de accidente para un"
            "vuelo [...].")


class CrewSetup:
    def __init__(self):
        # Favicon
        st.set_page_config(page_title="AAP - Forecast", )

        # Introducción
        st.markdown("# MODELO DE PREDICCIÓN FORECAST")
        st.markdown("Para la predicción, introduzca a continuación los campos "
                    "requeridos que se le muestran.")
        st.divider()

        # Sidebar
        st.sidebar.header("MODELO DE PREDICCIÓN: FORECAST")
        st.sidebar.markdown(
            "En esta sección, se presenta la predicción de accidente para un"
            "vuelo teniendo en cuenta las condiciones climáticas y las "
            "caracteristicas del piloto.")
