import streamlit as st
import pickle
import pandas as pd

# Cargar el diccionario desde un archivo pkl
with open('myDictionary.pkl', 'rb') as f:
    cat_dict = pickle.load(f)

# Cargar el modelo entrenado desde un archivo pkl
with open('modelo_entrenado.pkl', 'rb') as f:
    modelo = pickle.load(f)
prediccion=3
options = {}
for col in cat_dict:
    option = st.selectbox(f'Selecciona un valor para {col}', options=cat_dict[col].values())
    index = list(cat_dict[col].values()).index(option)
    options[col] = index
    
number_input61 = st.number_input('c61', value=0)
number_input62 = st.number_input('c62', value=0)
number_input53 = st.number_input('c53', value=0)
number_input54 = st.number_input('c54', value=0)
number_input55 = st.number_input('c55', value=0)
number_input56 = st.number_input('c56', value=0)

if st.button('Predecir'):
    # Crear un DataFrame con los datos introducidos por el usuario
    data = {'c1': [options['c1']], 'c6': [options['c6']], 'c7': [options['c7']],
            'c8': [options['c8']], 'c11': [options['c11']], 'c110': [options['c110']],
            'c65': [options['c65']], 'c68': [options['c68']], 'c41': [options['c41']],
            'c45': [options['c45']], 'c49': [options['c49']], 'c50': [options['c50']],
            'c52': [options['c52']], 'c130': [options['c130']], 'c96': [options['c96']],
            'c48': [options['c48']], 'c51': [options['c51']], 'c23': [options['c23']],
            'c24': [options['c24']], 'c61': [number_input61], 'c62': [number_input62],
            'c53': [number_input53], 'c54': [number_input54], 'c55': [number_input55],
            'c56': [number_input56]}
    df = pd.DataFrame(data)
    # Mostrar el dataframe generado
    st.write('Datos seleccionados:')
    st.write(df)
    # Realizar la predicción con el modelo entrenado
    prediccion = modelo.predict(df)
    
    # Mostrar el resultado de la predicción
    #st.write('El resultado de la predicción es:')
    #st.write(prediccion)
 
 # Mostrar el resultado de la predicción
if prediccion == 1:
    st.warning('PELIGRO RIESGO DE ACCIDENTE')
elif prediccion ==3:
    st.error('INTRODUCE LOS DATOS PARA PODER REALIZAR LA PREDICCION')
else:
    st.success('No hay riesgo de accidente')



