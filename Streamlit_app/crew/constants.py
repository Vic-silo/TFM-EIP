"""
Module created to contain the constant values
"""
# Directorio con fuente de datos
SOURCE_DIRECTORY = 'source/crew'
# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/mapped_dictionary.csv'
OHE_DIC = f'{SOURCE_DIRECTORY}/mapped_dictionary.csv'
# Leyenda de las columnas
COL_NAME_DICT = 'source/column_info.csv'
# Información de las columnas
HELP_INFO = 'forecast/help_columns.json'
# Normalizado y escalado
SCALER_1 = f'{SOURCE_DIRECTORY}/scaler_c61_c62_c31_c56.joblib'

SCALER_2 = f'{SOURCE_DIRECTORY}/scaler_c61_c62_c31_c56.joblib'#RELLENO BORRAR
# Modelo de predicción
MODEL = 'modelo_entrenado.pkl'