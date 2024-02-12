from fastapi import FastAPI
import uvicorn 
from pydantic import BaseModel
import joblib 
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI ()

# Criar uma classe com os dados de entrada que virão no request body com o tipo 'media' esperado

class request_body(BaseModel):
    leitura_sensor: float

# Carregar model para realizar a predição
modelo_aprendizagem = joblib.load('./src/aprendizagemMaquina/supervisionado/regressao_linear/modelo_regressao_linear.pkl')

@app.post('/predict')
def predict(data : request_body):
    input_features = {
        'media': data.leitura_sensor
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    # Predição
    y_pred = modelo_aprendizagem.predict(pred_df)[0].astype(float)

    return {'classe_predita' : y_pred.tolist()}