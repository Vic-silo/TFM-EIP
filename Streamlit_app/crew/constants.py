"""
Module created to contain the constant values
"""
import os

# Directorio con fuente de datos
SOURCE_DIRECTORY = 'Streamlit_app/source'

# Información de las columnas
HELP_INFO = 'Streamlit_app/crew/help_columns.json'

if not os.path.exists(SOURCE_DIRECTORY):
    SOURCE_DIRECTORY = 'source'

    # Información de las columnas
    HELP_INFO = 'crew/help_columns.json'

# Modelo de datos
_model = 'crew'

# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/{_model}/mapped_dictionary.csv'

# Leyenda de las columnas
COL_NAME_DICT = f'{SOURCE_DIRECTORY}/column_info.csv'

# Normalizado y escalado
SCALER_1 = f'{SOURCE_DIRECTORY}/{_model}/scaler_c62_c31_c56_c65.joblib'

# Modelo de predicción
MODEL = f'{SOURCE_DIRECTORY}/{_model}/modelo_entrenado'

# Directorio de resultados
RESULTS = f'{SOURCE_DIRECTORY}/results.json'
