import pandas as pd
import streamlit as st
import streamlit.errors
import warnings
import json
import joblib
from functools import lru_cache
from pycaret.classification import load_model, predict_model
from . import constants as c

warnings.filterwarnings('ignore')


class AirplaneModel:
    """
    Clase para el análisis del modelo de predicción airplane
    """
    _model = 'airplane'
    # Dataframe de datos a predecir
    _input_df: pd.DataFrame
    _final_df: pd.DataFrame
    # Dataframe leyenda de datos
    _cols_name_df: pd.DataFrame
    # Columnas esperadas por el modelo
    _cols = ['c145','c147','c149','c153','c155', 'c33', 'c39', 'c102','c104']
    # Tipo datos columnas
    _num_cols = ['c31', 'c151']
    _cat_cols = ['c145', 'c147', 'c149', 'c153', 'c155', 'c33', 'c39', 'c102', 'c104']
    _special_cols = ['c7', 'c10']
    _label_col = 'c1'
    _cols_lbl_encoder = ['c145', 'c147', 'c149', 'c153', 'c155', 'c33', 'c39', 'c102', 'c104']
    # Columnas por campo semántico añadir columnas para que queden separadas por tipo y sea mas visual
    _cols_general = ['c33','c145','c147','c149']
    _cols_motor = ['c153', 'c155', 'c39']
    _cols_vuelo = ['c102', 'c104']
    
    def __init__(self):
        # Imprimir el nombre de las columnas del dataset
        self._cols_name_df = cols_info(cols=self._cols)

        # Crear el dataframe de resultados
        self._input_df = pd.DataFrame(columns=self._cols)

    # PUBLIC METHODS
    def data_general(self) -> None:
        """
        Introducir los datos para las condiciones climáticas y pista de aterrizaje
        :return:
        """
        columns = self._cols_general
        
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def data_motor(self) -> None:
        """
        Introducir datos para las condicoines de la tripulacion
        :return:
        """
        columns = self._cols_motor
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)

    def data_vuelo(self) -> None:
        """
        Introducir datos para las condiciones del avión
        :return:
        """
        columns = self._cols_vuelo
        # Columnas para introducir datos numericos y categóricos de un modo más
        # simple
        col1, col2 = st.columns(spec=2, gap='medium')

        # Introducción de datos numéricos
        with col1:
            self._input_numeric_col(columns=columns)

        # Intorucción de datos categóricos
        with col2:
            self._input_categorical_col(columns=columns)


    def res_data(self) -> None:
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
            self._predict()

    # PRIVATE METHODS
    def _cat_input(self, col: str) -> None:
        """
        Crear campo categórico de introducción de datos
        :return:
        """
        self._input_df.loc[0, col] = st.selectbox(
            label=self._col_name(col), options=self._get_attributes(col),
            help=self._help(col))

    def _col_name(self, col: str) -> str:
        """
        Obtener la descirpción de la columna deseada
        :param col:
        :return:
        """
        info = self._cols_name_df.loc[col]["Descripcion"]

        return f'{col}\t{info}'

    def _encode_no_ohe_columns(self, cols: list) -> None:
        """
        Codifica los valores para el resto de columnas no OHE.
        :return:
        """
        map_df = load_csv(c.MAPPED_DIC)

        for col in cols:
            # Valor introducido por usuario
            input_value = self._input_df.loc[0, col]

            # Obtener valor mapeado
            map_value = map_df.loc[col].eq(input_value)
            map_value = map_value.idxmax() if map_value.any() else None

            try:
                self._final_df[col] = int(map_value)

            except (ValueError, NameError) as e:
                print(f'ERROR\t{e}')

    def _encode_values(self) -> None:
        """
        Codifica los valores categóricos según su codificación esperada
        :return:
        """

        # Columnas LabelEncoder
        self._encode_no_ohe_columns(cols=self._cols_lbl_encoder)

    def _get_attributes(self, col: str) -> list:
        attrs = self._cat_col_attributes(col=col)
        return attrs

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
            self._cat_input(col)

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
            self._num_input(col)

    def _num_input(self, col: str) -> None:
        """
        Crear campo numérico de introducción de datos
        :return:
        """
        self._input_df.loc[0, col] = st.number_input(
            label=self._col_name(col), step=1, help=self._help(col))

    @lru_cache()
    def _predict(self) -> None:
        """
        Calculos para la predicción. Para ello se requiere normalizar los datos
        y codificar los valores categóricos
        :return:
        """
        # Crea una copia de los datos introducidos para su modificación
        self._final_df = self._input_df.copy()

        # Normalizacion y escalado de valores
        #self._scale_values()

        # Codificación de valores
        self._encode_values()

        # Predicción
        pred = do_prediction(input_data=self._final_df)
        self._print_prediction(prediction=pred)

    def _print_prediction(self, prediction: int) -> None:
        """
        Muestra por pantalla el resultado
        :param prediction:
        :return:
        """
        map_df = load_csv(c.MAPPED_DIC)

        # Obtener valor mapeado
        map_value = map_df.at[self._label_col, str(prediction)]

        result = 'No existe' if map_value == 'I' else 'Existe'

        if result == 'No existe':
            st.info(f'{result} probabilidad de accidente.')

        else:
            st.warning(f'{result} probabilidad de accidente.')

        # Guardar datos de la predicción
        self._save_prediction(prediction=map_value)

    def _separe_columns(self, columns: list) -> None:
        """
        Separar columnas en bloques de x
        :param columns:
        :return:
        """
        for col in columns:
            try:
                if col in self._cat_cols:
                    self._input_categorical_col(columns=columns)
                else:
                    self._input_numeric_col(columns=columns)

            except streamlit.errors.DuplicateWidgetID:
                print(f'COLUMN_EXISTS\t{col}')

    # STATIC METHODS
    @staticmethod
    def _cat_col_attributes(col: str) -> list:
        """
        Obtiene los valores de una columna categorica
        :param col:
        :return:
        """
        df = load_csv(c.MAPPED_DIC)
        attrs = list(df.loc[col])
        return [attr for attr in attrs if attr != '-']

    @staticmethod
    def _get_hour(time) -> str:
        """
        Selecciona la hora para el input de los datos según la hora y minutos
        seleccionados
        :param time:
        :return:
        """
        hour = int(time.strftime('%H'))
        minute = int(time.strftime('%M'))

        if minute >= 30:
            hour += 1

        if hour == 24:
            hour = 0

        return str(hour).zfill(2)

    @staticmethod
    def _help(col: str) -> str:
        """
        Información de la introducción de datos para las columnas categoricas
        :param col:
        :return:
        """
        with open(c.HELP_INFO) as f:
            info = json.load(f)

        return info.get(col, 'Ayuda no disponible. Disculpe las molestias.')

    def _save_prediction(self, prediction: str):
        """
        Guardar la predicción en un fichero para unir los resultados
        :param prediction:
        :return:
        """

        with open(c.RESULTS) as f:
            results: dict = json.load(f)

        results.update({self._model: prediction})

        with open(c.RESULTS, 'w') as f:
            json.dump(results, f)


@st.cache_data
def cols_info(cols: list) -> pd.DataFrame:
    """
    Mustra los nombres de las columnas del dataset
    :return:
    """
    # Obtener los datos
    df = pd.read_csv(c.COL_NAME_DICT)

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


@st.cache_resource
def do_prediction(input_data: pd.DataFrame) -> int:
    """
    Realiza una nueva predicción con los datos proporcionados
    :param input_data:
    :return:
    """
    model = load_model(c.MODEL)
    prediction = predict_model(model, data=input_data)

    return prediction.loc[0, "prediction_label"]


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