"""
Resultado global de modelos de predicción
"""
import streamlit as st
from pages.page_styler.page_style import ResultSetup
import json
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import streamlit as st
import json
import matplotlib.pyplot as plt

# Setup de los datos de la página
ResultSetup()


def obtener_frecuencia(valores):
    return valores.count("A") if valores else 0

def obtener_probabilidad_accidente(frecuencia_crew, frecuencia_forecast, frecuencia_airplane):
    contador_a = frecuencia_crew + frecuencia_forecast + frecuencia_airplane
    if contador_a == 1:
        return "Probabilidad de accidente baja"
    elif contador_a == 2:
        return "Probabilidad de accidente media"
    elif contador_a >= 3:
        return "Probabilidad de accidente alta"
    elif contador_a == 0:
        return "No existe probabilidad de accidente"

def obtener_color(probabilidad_accidente):
    if probabilidad_accidente == "Probabilidad de accidente baja":
        return "blue"
    elif probabilidad_accidente == "Probabilidad de accidente media":
        return "orange"
    elif probabilidad_accidente == "Probabilidad de accidente alta":
        return "#aa1c0d"  # Tono más claro de rojo
    elif probabilidad_accidente == "No existe probabilidad de accidente":
        return "green"

# Carga el archivo JSON automáticamente
ruta_json = 'source/results.json'

# Lee el contenido del archivo JSON
with open(ruta_json, 'r') as archivo:
    datos = json.load(archivo)

# Extrae los valores de las claves "crew", "forecast" y "airplane"
valores_crew = datos.get("crew", "")
valores_forecast = datos.get("forecast", "")
valores_airplane = datos.get("airplane", "")

# Calcula las frecuencias
frecuencia_crew = obtener_frecuencia(valores_crew)
frecuencia_forecast = obtener_frecuencia(valores_forecast)
frecuencia_airplane = obtener_frecuencia(valores_airplane)

# Determina la probabilidad de accidente
probabilidad_accidente = obtener_probabilidad_accidente(frecuencia_crew, frecuencia_forecast, frecuencia_airplane)
color = obtener_color(probabilidad_accidente)

# Crea el gráfico de barras con el color correspondiente
fig, ax = plt.subplots()
categorias = ["crew", "forecast", "airplane"]
frecuencias = [frecuencia_crew, frecuencia_forecast, frecuencia_airplane]
colores = [color if f > 0 else "gray" for f in frecuencias]
ax.bar(categorias, frecuencias, color=colores)
ax.set_xlabel("Clave")
ax.set_ylabel("Frecuencia")
ax.set_title("Frecuencia de valores 'A'")
plt.xticks(rotation=45)

# Muestra el gráfico en Streamlit
st.pyplot(fig)

# Establece el estilo del mensaje con un fondo de color
mensaje_html = f"<h2 style='background-color:{color}; padding: 10px; border-radius: 10px; color: white;'>{probabilidad_accidente}</h2>"
st.markdown(mensaje_html, unsafe_allow_html=True)