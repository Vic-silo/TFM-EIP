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
            "vuelo teniendo en cuenta las características de la aeronave.")


class CrewSetup:
    def __init__(self):
        # Favicon
        st.set_page_config(page_title="AAP - Crew", )

        # Introducción
        st.markdown("# MODELO DE PREDICCIÓN CREW")
        st.markdown("Para la predicción, introduzca a continuación los campos "
                    "requeridos que se le muestran.")
        st.divider()

        # Sidebar
        st.sidebar.header("MODELO DE PREDICCIÓN: CREW")
        st.sidebar.markdown(
            "En esta sección, se presenta la predicción de accidente para un"
            "vuelo teniendo en cuenta las caracteristicas de la tripulación, "
            "visibilidad del piloto, características de la aeronave y  "
            "datos auxiliares de vuelo.")


class ResultSetup:
    def __init__(self):
        # Favicon
        st.set_page_config(page_title="AAP - Prediction result", )

        # Introducción
        st.markdown("# RESULTADO DE PREDICCIÓN GLOBAL")
        st.markdown("Resultado de los diferentes modelos creados.")
        st.divider()

        # Sidebar
        st.sidebar.header("RESULTADOS DE PREDICCIÓN")
        st.sidebar.markdown("Para el conjunto de predicciones realizadas, se "
                            "presenta de forma conjunta el resultado de todos "
                            "los modelos. De este modo, se premite visualizar "
                            "el riesgo de accidente teniendo en cuenta todas "
                            "las variables.")
