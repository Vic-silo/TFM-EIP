"""
Modulo principal de ejecución para app Streamlit
"""
import streamlit as st


# CONFIGURACIÓN PÁGINA PRINCIPAL
# Favicon
st.set_page_config(page_title="AAP - Home",)

# Introducción
st.markdown("# AAP -Aviation Accident Prediction")
st.markdown("""
Pagina inicial del TFM desarrollado para el estudio de riesgos en un vuelo dada
sus caracteristicas.

Desarrollado por:

- Jose Cabecas
- Pablo Ruiz
- Victor Simo
""")

# Sidebar
st.sidebar.header("AAP -Aviation Accident Prediction")
st.sidebar.markdown("Modelo de predicción realizado para el Trabajo de Fin de"
                    "Master de Python Avanzado para Hacking, Big Data y Machine"
                    "Learning la Escuela Internacional de Postgrados (EIP).")
