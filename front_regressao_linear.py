import streamlit as st
import json
import requests

# Título da Aplicação
st.title("Modelo de Predição de Classe de Sensores")

# Input do Usuário
st.write("Informe a leitura do sensor: ")
leitura = st.slider("Leitura", min_value=-1.0, max_value=1.0, value=0.000001, step=0.000001)

# Preparar dados da API
input_features = {'leitura_sensor' : leitura}

# Criar um botão e capturar um eveno deste botão para disparar a API
if st.button('Estimar Classe do Sensor'):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data=json.dumps(input_features))
    res_json = json.loads(res.text)
    classe = round(res_json['classe_predita'], 2)
    st.subheader(f'A classe predita do Sensor é {classe}')

    # Imprimir resposta no console
    st.write("Resposta da API:", res_json)