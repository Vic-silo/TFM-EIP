"""
Modulo principal de ejecución para app Streamlit
"""
import streamlit as st

doc_url = 'https://github.com/Vic-silo/TFM-EIP/blob/main_new/Memoria/Trabajo%20final%20de%20master.pdf'
repo_url = 'https://github.com/Vic-silo/TFM-EIP'

# CONFIGURACIÓN PÁGINA PRINCIPAL
# Favicon
st.set_page_config(page_title="AAP - Home",)

# Introducción
st.markdown("# AAP - Aviation Accident Prediction")
st.markdown(f"""
Pagina inicial del TFM desarrollado para el estudio de riesgos en un vuelo dada
sus caracteristicas.

### Desarrollado por:

- Jose Cabecas
- Pablo Ruiz
- Victor Simo

### Documentación:

- <a href={doc_url} target="_self">Documentacion TFM</a>
- <a href={repo_url} target="_self">Repositorio GitHub</a>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("AAP - Aviation Accident Prediction")
st.sidebar.markdown("Modelo de predicción realizado para el Trabajo de Fin de"
                    "Master de Python Avanzado para Hacking, Big Data y Machine"
                    "Learning la Escuela Internacional de Postgrados (EIP).")
