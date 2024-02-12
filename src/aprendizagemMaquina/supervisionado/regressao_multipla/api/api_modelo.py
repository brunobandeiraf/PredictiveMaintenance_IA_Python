from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib
from typing import List

# Criar uma instância do FastAPI
app = FastAPI ()

# Criar um classe que terá os dados do request body para a API
class RequestBody(BaseModel):
    features: List[float]

# Carregar modelo para realizar a predição
modelo_pontuacao = joblib.load('api_modelo.pkl')

def predict(data: RequestBody):
    # Preparar os dados para predição
    input_feature = [data.features]

    # Realizar a predição
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
    return {'pontuacao_teste': y_pred.tolist()}

# Rota para a função de predição
@app.post("/predict")
async def get_prediction(data: RequestBody):
    prediction = predict(data)
    return prediction

# Executar a aplicação
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)