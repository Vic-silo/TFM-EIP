"""
Clase
"""
import pandas as pd
import streamlit as st
import numpy as np
import warnings
import json

warnings.filterwarnings('ignore')

# Directorio con fuente de datos
SOURCE_DIRECTORY = 'source/forecast'
# Diccionario para mapeo de datos categóricos
MAPPED_DIC = f'{SOURCE_DIRECTORY}/mapped_dictionary.csv'
OHE_DIC = f'{SOURCE_DIRECTORY}/cols_ohe.csv'
# Leyenda de las columnas
COL_NAME_DICT = 'source/column_info.csv'
# Información de las columnas
HELP_INFO = 'forecast/help_columns.json'


class ForecastModel:
    """
    Clase para el análisis del modelo de predicción Forecast
    """
    # Dataframe de datos a predecir
    _input_df: pd.DataFrame
    # Dataframe leyenda de datos
    _cols_name_df: pd.DataFrame
    # Columnas esperadas por el modelo
    _cols = ['c7', 'c10', 'c31', 'c20', 'c21', 'c108', 'c110', 'c113', 'c114',
             'c240', 'c241', 'c41', 'c49', 'c56', 'c96', 'c106', 'c112', 'c115']
    # Tipo datos columnas
    _num_cols = ['c31', 'c20', 'c21', 'c113', 'c240', 'c241', 'c56']
    _cat_cols = ['c7', 'c10', 'c110', 'c106', 'c108', 'c112', 'c114', 'c115',
                 'c41', 'c49', 'c96']
    _special_cols = ['c7', 'c10', 'c110', 'c20', 'c21']
    # Columnas One Hot Encoder
    _cols_ohe = ['c96', 'c106', 'c112', 'c115']
    # Columnas por campo semántico
    _cols_forecast = ['c113', 'c114', 'c240', 'c241', 'c112', 'c115']
    _cols_crew = ['c41', 'c49', 'c56']
    _cols_airplane = ['c31']
    _cols_flight = ['c106', 'c96', 'c108', 'c20', 'c21', 'c7', 'c10', 'c110']

    def __init__(self):
        # Imprimir el nombre de las columnas del dataset
        self._cols_name_df = cols_info(cols=self._cols)

        # Crear el dataframe de resultados
        self._input_df = pd.DataFrame(columns=self._cols)

    def _col_name(self, col: str) -> str:
        """
        Obtener la descirpción de la columna deseada
        :param col:
        :return:
        """
        info = self._cols_name_df.loc[col]["Descripcion"]

        return f'{col}\t{info}'

    def data_forecast(self):
        """
        Introducir los datos para las condiciones climáticas
        :return:
        """
        columns = self._cols_forecast
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def data_crew(self):
        """
        Introducir datos para las condicoines de la tripulacion
        :return:
        """
        columns = self._cols_crew
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def data_airplane(self):
        """
        Introducir datos para las condicoines del avión
        :return:
        """
        columns = self._cols_airplane
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def data_flight(self):
        """
        Introducir datos para las condicoines de la tripulacion
        :return:
        """
        columns = self._cols_flight

        # Zona de vuelo
        self._plot_map()

        # Hora de vuelo
        self._datetime()

        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        # INFO
        st.markdown('### AUXILIAR')
        st.write('Datos auxiliares del vuelo')

        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def res_data(self):
        """
        Realiza la predicción del modelo
        :return:
        """
        # Revisión de los datos
        st.markdown('### Revisión de datos')
        st.write('Revise los datos introducidos')
        st.dataframe(self._input_df)

        # Botón de predicción
        predict_do = st.button(label=":blue[PREDICCIÓN]")

        if predict_do:
            self.prediction()

    def prediction(self):
        """
        Calculos para la predicción
        :return:
        """
        st.write('Se desea realizar una predicción')

    def _get_attributes(self, col: str) -> list:
        """
        Obtener la lista de valores que tiene una columna
        :param column:
        :param col_type:
        :return:
        """
        if col in self._cols_ohe:  # Columnas One Hot Encoder
            df = load_csv(OHE_DIC)
            attrs = list(df[col].dropna().unique())

        else:  # Columnas categoricas
            df = load_csv(MAPPED_DIC)
            attrs = list(df.loc[col])
            attrs = [attr for attr in attrs if attr != '-']

        return attrs

    def _input_numeric_col(self, columns: list) -> None:
        """
        Campos para introducir datos numéricos
        :param columns:
        :return:
        """
        unused_cols = self._special_cols.copy()
        unused_cols.extend(self._cat_cols)

        for col in columns:
            if col in unused_cols:
                continue

            # Campo para introducir datos. Añadir datos a la columna del
            # dataframe a predecir
            self._input_df.loc[0, col] = st.number_input(
                label=self._col_name(col), step=1, help=self._help(col))

    def _input_categorical_col(self, columns: list) -> None:
        """
        Campos para introducir datos categoricos
        :param columns:
        :return:
        """
        unused_cols = self._special_cols.copy()
        unused_cols.extend(self._num_cols)

        for col in columns:
            if col in unused_cols:
                continue

            # Campo para introducir datos. Añadir datos a la columna del
            # dataframe a predecir
            self._input_df.loc[0, col] = st.selectbox(
                label=self._col_name(col), options=self._get_attributes(col),
                help=self._help(col))

    def _plot_map(self):
        """
        Representar mapa de la zona de vuelo del avión
        :return:
        """
        with st.container():
            # INFO
            st.markdown('### ZONA DE VUELO')
            st.write('Zona indicada por la que el avión realiza su vuelo.')

            # DATOS
            c1, c2 = st.columns(spec=2)

            with c1:
                self._input_df.loc[0, 'c20'] = st.number_input(
                    label=self._col_name('c20'), help=self._help('c20'),
                    value=39.46975)
            with c2:
                self._input_df.loc[0, 'c21'] = st.number_input(
                    label=self._col_name('c21'), help=self._help('c21'),
                    value=-0.37739)

            location = {"LAT": self._input_df['c20'],
                        "LON": self._input_df['c21']}

            st.map(location, zoom=10)

    def _datetime(self):
        """
        Input de fecha y hora de vuelo
        :return:
        """
        with st.container():
            # INFO
            st.markdown('### FECHA Y HORA')
            st.write('Fecha y hora del vuelo.')

            # DATOS
            c1, c2 = st.columns(spec=2)

            with c1:
                date = st.date_input(label='Fecha del vuelo',
                                     help=self._help('c7'))
                self._input_df.loc[0, 'c7'] = int(date.strftime('%m'))

            with c2:
                hour = st.time_input(label='Hora del vuelo',
                                     help=self._help('c10'))
                self._input_df.loc[0, 'c10'] = int(hour.strftime('%H'))

    @staticmethod
    def _help(col: str) -> str:
        """
        Información de la introducción de datos para las columnas categoricas
        :param col:
        :return:
        """
        with open(HELP_INFO) as f:
            info = json.load(f)

        return info.get(col, 'Ayuda no disponible. Disculpe las molestias.')


@st.cache_data
def cols_info(cols: list) -> pd.DataFrame:
    """
    Mustra los nombres de las columnas del dataset
    :return:
    """
    # Obtener los datos
    df = pd.read_csv(COL_NAME_DICT)

    # Mostrar los datos
    dict_cols = {'Indice': [], 'Descripcion': []}
    for col in cols:
        if col not in cols:
            continue
        dict_cols["Indice"].append(col)
        dict_cols["Descripcion"].append(
            df[df["Column_name"] == col]["Description"].values[0])

    df_legend = pd.DataFrame(data=dict_cols["Descripcion"],
                             index=dict_cols["Indice"],
                             columns=["Descripcion"])

    # Desplegable con la leyenda de los datos a introducir por el usuario
    with st.expander("Leyenda de datos."):
        st.write("Leyenda de todos los datos a introducir por el usuario"
                 "para la predicción del modelo:")
        st.dataframe(df_legend, use_container_width=True)

    return df_legend


@st.cache_data
def load_csv(path: str, index_col: int = 0) -> pd.DataFrame:
    """
    Devuelve un datafraame con los datos según el path necesario
    :param index_col:
    :param path:
    :return:
    """
    df = pd.read_csv(path, index_col=index_col)

    return df
