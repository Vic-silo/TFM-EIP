"""
Resultado global de modelos de predicción
"""
from pages.page_styler.page_style import ResultSetup
import streamlit as st
import os
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager

# Ruta a los resultados
RESULTS = 'Streamlit_app/source/results.json'

if not os.path.exists(RESULTS):
    RESULTS = 'source/results.json'


def _get_accident_prob(results_: dict):
    """
    Obtener la probabilidad de accidente
    :param results:
    :return:
    """
    res = {"msg": '', "plot_color": ''}
    accident_counter = sum([v for k, v in results_.items()])

    if accident_counter == 0:
        res["msg"] = 'No existe probabilidad de accidente'
        res["plot_color"] = '#317f43'

    elif accident_counter == 1:
        res["msg"] = 'Probabilidad de accidente baja'
        res["plot_color"] = '#65b3ff'

    elif accident_counter == 2:
        res["msg"] = 'Probabilidad de accidente media'
        res["plot_color"] = '#e16f00'

    else:
        res["msg"] = 'Probabilidad de accidente alta'
        res["plot_color"] = '#aa1c0d'

    return res


@st.cache_resource
def _link_models() -> None:
    """
    Crear un link a cada uno de los modelos de la aplicacion
    :return:
    """
    models = {'AIRPLANE': {"result_index": 3}, 'CREW': {"result_index": 4},
              'FORECAST': {"result_index": 3}}

    for model in models.keys():
        idx = models[model]['result_index']
        st.markdown(f'''<a href="AAP_{model}_MODEL?tab={idx}" target="_self">
                    Resultados modelo {model}</a>''', unsafe_allow_html=True)


def _map_value(value: str) -> int:
    """
    Obtener los resultados para cada uno de los modelos en formato numérico.
    Donde 1 es Accidente y 0 no accidente
    :return:
    """
    return 1 if value == 'A' else 0


def _plot_results(data: dict) -> None:
    """
    Representar los datos en formato de gráfico
    :param data:
    :return:
    """
    accident_data = _get_accident_prob(results_=data)
    color = _set_plot_color(predefined_color=accident_data["plot_color"])
    _plot_results_do(data=data, color=color)
    _text_result(data=accident_data)


@st.cache_resource
def _plot_results_do(data: dict, color: str) -> None:
    """
    Genera el grafico de barras con los resultados de las predicciones
    :param data:
    :param probability:
    :return:
    """
    values = [value for key, value in data.items()]

    fig, ax = plt.subplots()
    ax.bar(list(data.keys()), values, color=color)

    ax.set_ylabel("Accidente")
    ax.set_yticks([0, 1])

    ax.set_title("PREDICCION DE MODELOS", y=1.1)

    st.pyplot(fig)


def _result_loads() -> dict:
    """
    Obtener los resultados de los diferentes modelos mapeados a valores numéricos
    :return:
    """
    with open(RESULTS, 'r') as f:
        res = json.load(f)

    # Devolver valores en valor numérico
    return {key: _map_value(value) for key, value in res.items()}


def _set_plot_color(predefined_color: str) -> str:
    """
    Selecciona el color del grafico a gusto del usuario
    :param predefined_color:
    :return:
    """
    return st.color_picker('Pick A Color', predefined_color)


def _text_result(data: dict) -> None:
    """
    Muestra en texto la probabilidad global de accidente
    :param data:
    :return:
    """
    msg = data['msg']
    st.markdown(msg, unsafe_allow_html=True)


if __name__ == '__main__':
    # Setup de los datos de la página
    ResultSetup()

    with st.container():
        results = _result_loads()
        _plot_results(data=results)

    with st.container():
        st.divider()
        _link_models()
