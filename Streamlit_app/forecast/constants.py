"""
Module created to contain the constant values
"""
# Directorio con fuente de datos
SOURCE_DIRECTORY = 'Streamlit_app/source/forecast'
# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/mapped_dictionary.csv'
OHE_DIC = f'{SOURCE_DIRECTORY}/cols_ohe.csv'
# Leyenda de las columnas
COL_NAME_DICT = 'Streamlit_app/source/column_info.csv'
# Información de las columnas
HELP_INFO = 'Streamlit_app/forecast/help_columns.json'
# Normalizado y escalado
SCALER_1 = f'{SOURCE_DIRECTORY}/scaler_c20_c241.joblib'
SCALER_2 = f'{SOURCE_DIRECTORY}/scaler_c21_c113_c56.joblib'
# Modelo de predicción
MODEL = 'Forecast_model_20230512_1239'