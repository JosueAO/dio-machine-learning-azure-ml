import json
import numpy as np
import joblib
from azureml.core.model import Model

def init():
    global model
    # Carrega o modelo
    model_path = Model.get_model_path('bike_rental_model')
    model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)['data']
    data = np.array(data)
    # Previsões
    predictions = model.predict(data)
    return json.dumps(predictions.tolist())

