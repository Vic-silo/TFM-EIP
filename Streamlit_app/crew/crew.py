import pandas as pd
import streamlit as st
import warnings
import json
import joblib
from functools import lru_cache
from pycaret.classification import load_model, predict_model
from . import constants as c

warnings.filterwarnings('ignore')


class CrewModel:
    """
    Clase para el análisis del modelo de predicción Forecast
    """
    # Dataframe de datos a predecir
    _input_df: pd.DataFrame
    _final_df: pd.DataFrame
    # Dataframe leyenda de datos
    _cols_name_df: pd.DataFrame
    # Columnas esperadas por el modelo
    _cols = ['c62', 'c31', 'c56','c7', 'c151', 'c65', 'c10',
             'c144', 'c106', 'c108', 'c51', 'c101', 'c109',
             'c35', 'c117', 'c128', 'c156', 'c49', 'c41', 'c30']
    # Tipo datos columnas
    _num_cols = [ 'c62', 'c31', 'c56','c65']
    _cat_cols = ['c7', 'c151', 'c10', 'c144', 'c106', 'c108', 'c51',
                 'c101', 'c109', 'c35', 'c117',
                 'c128', 'c156', 'c49', 'c41', 'c30']


    _special_cols = ['c7', 'c10'] # borrar esta linea
    _label_col = 'c1'

    # Columnas One Hot Encoder
    #_cols_oe = ['c144', 'c106', 'c108', 'c51', 'c101', 'c109', 'c132', 'c141', 'c35', 'c117', 'c122', 'c126', 'c128', 'c130', 'c84', 'c123', 'c156', 'c49', 'c41', 'c30']
    _cols_lbl_encoder = ['c7','c10','c144', 'c106', 'c108', 'c51', 'c101',
                         'c109', 'c35', 'c117',
                         'c128','c156', 'c49', 'c41', 'c30','c151']



    # Columnas por campo semántico añadir columnas para que queden separadas por tipo y sea mas visual
    _cols_forecast = ["c109","c117"]
    _cols_crew = ['c51', 'c62', 'c56','c49', 'c41','c65']#Genera error con columnas c65 ya que es float y en el input se meten como int
    _cols_flight = ['c7','c106','c108','c128', 'c144', 'c10',
                    'c156', 'c10', 'c35', 'c101', 'c31', 'c30', 'c151']

    # Columnas a normalizar o escalar
    _cols_scaler_1 = [ 'c62', 'c31', 'c56','c65']



    def __init__(self):
        # Imprimir el nombre de las columnas del dataset
        self._cols_name_df = cols_info(cols=self._cols)

        # Crear el dataframe de resultados
        self._input_df = pd.DataFrame(columns=self._cols)

        self._final_df = pd.DataFrame(columns=self._cols)#añadido para pruebas
    # PUBLIC METHODS

    def data_forecast(self) -> None:
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

    def data_crew(self) -> None:
        """
        Introducir datos para las condicoines de la tripulacion
        :return:
        """
        # Zona de vuelo
        self._float_input()

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

    def data_flight(self) -> None:
        """
        Introducir datos para las condicoines de la tripulacion
        :return:
        """
        columns = self._cols_flight


        # Hora de vuelo
        self._datetime_input()

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
            st.dataframe(self._final_df)#añadido para pruebas
    # PRIVATE METHODS

    def _cat_input(self, col: str) -> None:
        """
        Crear campo categórico de introducción de datos
        :return:
        """
        key = f"{col}_selectbox"  # Genera una clave única para cada selectbox
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

    #def _create_ohe_columns(self, col: str) -> None:
    #    """
    #    Crea las nuevas columnas teniendo en cuenta el valor seleccionado en el
    #    input
    #    :param col:
    #    :return:
    #    """
        # Valor introducido por usuario
        #input_value = self._input_df.loc[0, col]

        # Obtener valores de la columna
        #attrs = self._cat_col_ohe_attributes(col=col)

        # Lista de columnas a añadir
        #ohe_columns = [f'{col}_{attr}' for attr in attrs]

        # Añadir columnas con valor
        #for col in ohe_columns:
        #    value = 1.0 if input_value in col else 0.0
        #    self._final_df[col] = value

        # Renombrar columnas NaN
        #self._final_df.columns = self._final_df.columns.str.replace('_NAN', '_nan')

    def _datetime_input(self) -> None:
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
                self._input_df.loc[0, 'c7'] = str(int(date.strftime('%m')))

            with c2:
                time = st.time_input(label='Hora del vuelo',
                                     help=self._help('c10'))
                self._input_df.loc[0, 'c10'] = self._get_hour(time=time)

    def _do_scale(self, cols: list, scaler) -> None:
        """
        Realiza el escalado de los valores en la lista 1
        :param cols:
        :param scaler:
        :return:
        """
        self._final_df[cols] = scaler.transform(self._input_df[cols])

    #def _encode_ohe_columns(self) -> None:
        """
        Codifica los valores para las columnas OHE. Crea las columnas necesarias
        y elimina la columna padre
        :return:
        """
     #   list(map(lambda col: (
                 # Eliminar columna
     #            self._final_df.pop(col),
                 # Añadir columnas según el valor en el input
     #            self._create_ohe_columns(col=col)),
     #            self._cols_oe))

    def _encode_no_ohe_columns(self) -> None:
        """
        Codifica los valores para el resto de columnas no OHE.
        :return:
        """
        map_df = load_csv(c.MAPPED_DIC)

        for col in self._cols_lbl_encoder:

            # Valor introducido por usuario
            input_value = self._input_df.loc[0, col]

            # Obtener valor mapeado
            map_value = map_df.loc[col].eq(input_value)
            map_value = map_value.idxmax() if map_value.any() else None

            try:
            #    if map_value is not None:
            #        self._final_df[col] = int(map_value)
            #    else:
            #        self._final_df[col] = 0
                self._final_df[col] = int(map_value)

            except (ValueError, NameError) as e:
                print(f'ERROR\t{e}')

    def _encode_values(self) -> None:
        """
        Codifica los valores categóricos según su codificación esperada
        :return:
        """
        # Columnas OHE
    #    self._encode_ohe_columns()

        # Columnas LabelEncoder
        self._encode_no_ohe_columns()

    def _get_attributes(self, col: str) -> list:
        attrs = self._cat_col_attributes(col=col)
        return attrs

    def _get_scaler(self, scaler_type: int) -> None:
        """
        Realiza el escalado de los valores en la lista 1
        :param scaler_type:
        :return:
        """
        try:

            scaler = joblib.load(c.SCALER_1)
            cols = self._cols_scaler_1

            self._do_scale(cols=cols, scaler=scaler)

        except Exception as e:
            print("[-] ERROR\t", e)
            print('Valores no definidos')

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

    def _float_input(self) -> None:
        """
        Número de miembros de la tripulación de vuelo a bordo
        :return:
        """
        with st.container():
            # INFO
            st.markdown('### ZONA DE VUELO')
            st.write('Zona indicada por la que el avión realiza su vuelo.')

            # DATOS
            c1 = st.columns(spec=1)[0]

            self._input_df.loc[0, 'c65'] = st.number_input(
                label=self._col_name('c65'), help=self._help('c65'),
                value=39.46975)

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
        self._scale_values()

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
            st.info(f'{result} ,probabilidad de accidente.')

        else:
            st.warning(f'{result},{map_value},{prediction} probabilidad de accidente.')

    def _scale_values(self) -> None:
        """
        Escala los valores numéricos según el entrenamiento
        :return:
        """
        # Iterar sobre los tipos de scalers definidos en el entrenamiento
        list(map(lambda x: self._get_scaler(scaler_type=x), [1]))

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
    def _cat_col_ohe_attributes(col: str) -> list:
        """
        Devuelve los atributos de una columna OHE
        :param col:
        :return:
        """
        df = load_csv(c.OHE_DIC)
        return list(df[col].dropna().unique())

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
    model = load_model(f'{c.SOURCE_DIRECTORY}/{c.MODEL}')
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
