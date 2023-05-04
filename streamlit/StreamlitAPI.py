'''
    Mudulo del modelo de la API
'''
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

DATA_ROOT = 'data/covid19.csv'


class API:
    def __init__(self):

        # Datos del DataFrame
        self.__dfBase = self.__LoadData()
        self.__paises = self.__dfBase['country'].unique()

        # Inicio de la intefaz de la API
        self.__StartAPI()

    def __StartAPI(self):
        # Crear caracteristicas de la API
        menu = st.sidebar.selectbox('Elije la ventana',
                                    ['Home', 'Data'])
        if menu == 'Home':
            self.__SetHome()
        elif menu == 'Data':
            self.__SetData()

    def __SetHome(self):
        '''
        Crea la vista de la pagina Home
        :return:
        '''
        # Mera informacion de la API
        st.header('COVID 19')
        st.subheader('API en Streamlit para visualizar datos de la pandemia.')
        st.write('En esta API se muestra los datos de la pandemia a nivel'
                 'global. La intencion es mediante el uso de Big Data'
                 'concienciar a quien pueda ver esta API.')

    def __SetData(self):
        '''
        Crea la vista de la pagina de Data
        :return:
        '''

        # Caracteristicas de la pagina
        st.header('DATOS DEL COVID')

        # Selectbox para escoger pais de visualizacion
        paisSelec = st.selectbox(
            'Selecciona el pais deseado.',
            self.__paises
        )

        # Mapa pais seleccionado
        geolocator = Nominatim(user_agent='busqueda')
        location = geolocator.geocode(paisSelec)
        mapa = dict(
            lat=[location.latitude],
            lon=[location.longitude]
        )
        mapa = pd.DataFrame(mapa)

        st.map(mapa, zoom=5)

        # Insertar Dataframe
        dfParametrizado = self.__DefineData(paisSelec)

        try:
            st.write(dfParametrizado)
            # Insertar gráfica
            st.subheader('Visualizacion de datos')

            grafico = st.radio(label='', options=dfParametrizado.columns)
            dfParametrizado = dfParametrizado[[grafico]]
            st.line_chart(dfParametrizado)

        except:
            st.write('No hay datos para los parametros seleccionados.')

    @st.cache
    def __LoadData(self):
        '''
        Cargar el DataFrame a nuestra aplicacion
        :return:
        '''

        df = pd.read_csv(DATA_ROOT, index_col=False, sep=';')
        df = df.drop(columns=['index', 'Unnamed: 0'])

        # Ordenar por fecha
        df['day'] = pd.to_datetime(df['time'])
        df.sort_values(by='time')

        return df

    # @st.cache(suppress_st_warning=True)
    def __DefineData(self, pais): #, fechaInicio, fechaFinal):
        '''
        Parametriza el Dataframe de acuerdo con los parametros de entrada
        :param pais:
        :param fechaInicio:
        :param fechaFinal:
        :return:
        '''

        df = self.__dfBase[['country', 'day', 'cases_active',
                            'cases_critical', 'cases_recovered',
                            'deaths_total', 'population']]

        # Ordenar por fecha
        df = df.sort_values(by='day')

        # Parametrizacion Dataframe por pais
        df = df.loc[df['country'] == pais]

        # Descripcion de la informacion
        poblacionInicial = df.iloc[0]['population']
        poblacionFinal = df.iloc[-1]['population']


        # Variable parametrizacion por fecha
        self.__fechas = df['day'].unique()
        self.__fechaInicio = df['day'].min()
        self.__fechaUltima = df['day'].max()

        # Slider para escoger las fechas de visualización
        startDate, endDate = st.select_slider(
            'Selecciona el rango de fechas de la pandemia.',
            options=self.__fechas,
            value=(self.__fechaInicio, self.__fechaUltima)
        )
        st.write(f'Fechas seleccionadas entre {startDate} y {endDate}')

        # Parametrizacion del dataframe
        df = df.loc[(df['day'] >= startDate) & (df['day'] <= endDate)]

        # df.to_csv(f'dfParametrizado_{pais}.csv')

        st.subheader(f'Datos de la pandemia para {pais}:')
        st.write(f'Población antes pandemia: {poblacionInicial}')
        st.write(f'Población despues pandemia: {poblacionFinal}')
        st.write(f'Total de decesos: {df.iloc[-1]["deaths_total"]}')

        # Presentacion dataframe
        df = df.drop(columns=['country', 'population'])
        df = df.set_index('day')

        return df
