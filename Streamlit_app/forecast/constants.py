"""
Module created to contain the constant values
"""
import os

# Directorio con fuente de datos
SOURCE_DIRECTORY = 'Streamlit_app/source'

# Información de las columnas
HELP_INFO = 'Streamlit_app/forecast/help_columns.json'

if not os.path.exists(SOURCE_DIRECTORY):
    SOURCE_DIRECTORY = 'source'

    # Información de las columnas
    HELP_INFO = 'forecast/help_columns.json'

# Modelo da datos
_model = 'forecast'

# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/{_model}/mapped_dictionary.csv'
OHE_DIC = f'{SOURCE_DIRECTORY}/{_model}/cols_ohe.csv'

# Leyenda de las columnas
COL_NAME_DICT = f'{SOURCE_DIRECTORY}/column_info.csv'


# Normalizado y escalado
SCALER_1 = f'{SOURCE_DIRECTORY}/{_model}/scaler_c20_c241.joblib'
SCALER_2 = f'{SOURCE_DIRECTORY}/{_model}/scaler_c21_c113_c56.joblib'

# Modelo de predicción
MODEL = f'{SOURCE_DIRECTORY}/{_model}/Forecast_model_20230512_1239'

# Directorio de resultados
RESULTS = f'{SOURCE_DIRECTORY}/results.json'
