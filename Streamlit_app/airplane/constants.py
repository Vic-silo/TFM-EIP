"""
Module created to contain the constant values
"""
import os


# Directorio con fuente de datos
SOURCE_DIRECTORY = 'Streamlit_app/source'

# Información de las columnas
HELP_INFO = 'Streamlit_app/airplane/help_columns.json'

if not os.path.exists(SOURCE_DIRECTORY):
    SOURCE_DIRECTORY = 'source'

    # Información de las columnas
    HELP_INFO = 'airplane/help_columns.json'

# Modelo da datos
_model = 'airplane'

# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/{_model}/mapped_dictionary.csv'

# Leyenda de las columnas
COL_NAME_DICT = f'{SOURCE_DIRECTORY}/column_info.csv'

# Modelo de predicción
MODEL = f'{SOURCE_DIRECTORY}/{_model}/Airplane_model'

# Directorio de resultados
RESULTS = f'{SOURCE_DIRECTORY}/results.json'